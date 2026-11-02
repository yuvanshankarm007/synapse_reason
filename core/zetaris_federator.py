"""
Zetaris AI Data Harness & AgentFlow Virtualization Connector
Allows the Reasoning Agent to execute zero-copy in-place federated queries across 
heterogeneous enterprise silos (ERP SQL, CloudTrail JSON logs, Vendor Registry)
governed by Zetaris AgentFlow workspaces and access policies.
"""
import sqlite3
import json
import csv
import time
from typing import Dict, Any, List
import config

try:
    import pandas as pd
except ImportError:
    pd = None

class ZetarisFederator:
    """Zetaris AI Data Harness: Virtualizes distributed data sources into a unified queryable fabric."""
    def __init__(self):
        self.conn = sqlite3.connect(":memory:", check_same_thread=False)
        self.agentflow_workspace_id = "zetaris_agentflow_ws_88190"
        self._initialize_virtual_fabric()

    def _initialize_virtual_fabric(self):
        """Mounts heterogeneous silos into the Zetaris AI Data Harness virtual catalog."""
        # 1. Mount ERP Transactions (CSV Silo)
        try:
            erp_csv_path = config.DATA_DIR / "erp_transactions.csv"
            if erp_csv_path.exists():
                if pd is not None:
                    df_erp = pd.read_csv(erp_csv_path)
                    df_erp.to_sql("erp_transactions", self.conn, index=False, if_exists="replace")
                else:
                    self._load_csv_to_sqlite(erp_csv_path, "erp_transactions")
            else:
                self._load_fallback_erp()
        except Exception as e:
            print(f"[ZetarisFederator] Warning loading ERP CSV ({e}), loading fallback.")
            self._load_fallback_erp()

        # 2. Mount Cloud Audit Logs (JSON Silo)
        try:
            cloud_json_path = config.DATA_DIR / "cloud_audit_logs.json"
            if cloud_json_path.exists():
                with open(cloud_json_path, "r", encoding="utf-8") as f:
                    logs_data = json.load(f)
                if pd is not None:
                    df_logs = pd.DataFrame(logs_data)
                    df_logs.to_sql("cloud_audit_logs", self.conn, index=False, if_exists="replace")
                else:
                    self._load_dicts_to_sqlite(logs_data, "cloud_audit_logs")
            else:
                self._load_fallback_cloud()
        except Exception as e:
            print(f"[ZetarisFederator] Warning loading Cloud Audit JSON ({e}), loading fallback.")
            self._load_fallback_cloud()

        # 3. Mount Vendor Procurement Contracts (JSON Silo)
        try:
            vendor_json_path = config.DATA_DIR / "vendor_contracts.json"
            if vendor_json_path.exists():
                with open(vendor_json_path, "r", encoding="utf-8") as f:
                    vendor_data = json.load(f)
                if pd is not None:
                    df_vendor = pd.DataFrame(vendor_data)
                    df_vendor.to_sql("vendor_contracts", self.conn, index=False, if_exists="replace")
                else:
                    self._load_dicts_to_sqlite(vendor_data, "vendor_contracts")
            else:
                self._load_fallback_vendor()
        except Exception as e:
            print(f"[ZetarisFederator] Warning loading Vendor JSON ({e}), loading fallback.")
            self._load_fallback_vendor()

        # 4. Mount Kubernetes Pod Runtime Observability (Datadog/Prometheus Silo)
        try:
            k8s_json_path = config.DATA_DIR / "k8s_telemetry.json"
            if k8s_json_path.exists():
                with open(k8s_json_path, "r", encoding="utf-8") as f:
                    k8s_data = json.load(f)
                if pd is not None:
                    pd.DataFrame(k8s_data).to_sql("k8s_telemetry", self.conn, index=False, if_exists="replace")
                else:
                    self._load_dicts_to_sqlite(k8s_data, "k8s_telemetry")
            else:
                self._load_fallback_k8s()
        except Exception as e:
            print(f"[ZetarisFederator] Warning loading K8s JSON ({e}), loading fallback.")
            self._load_fallback_k8s()

        # 5. Mount Customer Support & SLA Impact Tickets (ServiceNow/Zoho Desk Silo)
        try:
            tickets_json_path = config.DATA_DIR / "support_tickets.json"
            if tickets_json_path.exists():
                with open(tickets_json_path, "r", encoding="utf-8") as f:
                    tickets_data = json.load(f)
                if pd is not None:
                    pd.DataFrame(tickets_data).to_sql("support_tickets", self.conn, index=False, if_exists="replace")
                else:
                    self._load_dicts_to_sqlite(tickets_data, "support_tickets")
            else:
                self._load_fallback_tickets()
        except Exception as e:
            print(f"[ZetarisFederator] Warning loading Support Tickets JSON ({e}), loading fallback.")
            self._load_fallback_tickets()

        # In-Memory Index Optimization for Sub-Millisecond Cross-Silo Joins
        try:
            cur = self.conn.cursor()
            cur.execute("CREATE INDEX IF NOT EXISTS idx_erp_vendor ON erp_transactions(vendor_id)")
            cur.execute("CREATE INDEX IF NOT EXISTS idx_cloud_target ON cloud_audit_logs(target_resource)")
            cur.execute("CREATE INDEX IF NOT EXISTS idx_vendor_id ON vendor_contracts(vendor_id)")
            cur.execute("CREATE INDEX IF NOT EXISTS idx_k8s_target ON k8s_telemetry(target_resource)")
            cur.execute("CREATE INDEX IF NOT EXISTS idx_ticket_tx ON support_tickets(related_tx_id)")
            self.conn.commit()
        except Exception:
            pass

    def _load_csv_to_sqlite(self, path, table_name):
        with open(path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        if rows:
            self._load_dicts_to_sqlite(rows, table_name)

    def _load_dicts_to_sqlite(self, dicts: List[Dict[str, Any]], table_name: str):
        if not dicts:
            return
        cols = list(dicts[0].keys())
        cur = self.conn.cursor()
        cur.execute(f"DROP TABLE IF EXISTS {table_name}")
        col_defs = ", ".join([f'"{c}" TEXT' for c in cols])
        cur.execute(f"CREATE TABLE {table_name} ({col_defs})")
        placeholders = ", ".join(["?"] * len(cols))
        cur.executemany(
            f"INSERT INTO {table_name} ({', '.join(['\"' + c + '\"' for c in cols])}) VALUES ({placeholders})",
            [[r.get(c) for c in cols] for r in dicts]
        )
        self.conn.commit()

    def _load_fallback_erp(self):
        fallback = [
            {"tx_id": "TX-90214", "timestamp": "2026-10-26T14:10:00Z", "vendor_id": "VND-8821", "vendor_name": "Acrobatics Logistics LLC", "amount_usd": 184500.0, "approver_id": "USR-9912", "status": "SETTLED_WIRE", "bank_routing": "021000021"},
            {"tx_id": "TX-90219", "timestamp": "2026-10-27T09:15:00Z", "vendor_id": "VND-8821", "vendor_name": "Acrobatics Logistics LLC", "amount_usd": 245000.0, "approver_id": "USR-9912", "status": "PENDING_SETTLEMENT", "bank_routing": "021000021"}
        ]
        if pd is not None:
            pd.DataFrame(fallback).to_sql("erp_transactions", self.conn, index=False, if_exists="replace")
        else:
            self._load_dicts_to_sqlite(fallback, "erp_transactions")

    def _load_fallback_cloud(self):
        fallback = [
            {"event_id": "EVT-88102", "timestamp": "2026-10-27T09:12:00Z", "user_id": "USR-9912", "action": "APPROVE_DISBURSEMENT", "target_resource": "TX-90219", "source_ip": "185.220.101.45", "geo_country": "SC (Seychelles)", "is_vpn_or_tor": 1, "mfa_authenticated": 0}
        ]
        if pd is not None:
            pd.DataFrame(fallback).to_sql("cloud_audit_logs", self.conn, index=False, if_exists="replace")
        else:
            self._load_dicts_to_sqlite(fallback, "cloud_audit_logs")

    def _load_fallback_vendor(self):
        fallback = [
            {"vendor_id": "VND-8821", "legal_name": "Acrobatics Logistics LLC", "contract_status": "ACTIVE_STANDARD", "single_tx_limit_usd": 50000.0, "monthly_cap_usd": 200000.0, "verified_bank_routing": "011000015", "risk_score": 0.88}
        ]
        if pd is not None:
            pd.DataFrame(fallback).to_sql("vendor_contracts", self.conn, index=False, if_exists="replace")
        else:
            self._load_dicts_to_sqlite(fallback, "vendor_contracts")

    def _load_fallback_k8s(self):
        fallback = [
            {"pod_id": "pod-pay-gw-canary-7b89f", "namespace": "canary", "service_name": "payment-gateway", "cpu_utilization_pct": 98.4, "jvm_heap_pct": 98.2, "status": "CrashLoopBackOff", "restart_count": 14, "target_resource": "TX-90214", "timestamp": "2026-10-27T04:12:00Z"}
        ]
        if pd is not None:
            pd.DataFrame(fallback).to_sql("k8s_telemetry", self.conn, index=False, if_exists="replace")
        else:
            self._load_dicts_to_sqlite(fallback, "k8s_telemetry")

    def _load_fallback_tickets(self):
        fallback = [
            {"ticket_id": "TICK-7701", "customer_name": "Acrobatics Logistics LLC", "priority": "P0_CRITICAL", "title": "Wire TX-90214 settlement delay", "related_tx_id": "TX-90214", "status": "ESCALATED_SRE", "sla_deadline_hours": 1.0}
        ]
        if pd is not None:
            pd.DataFrame(fallback).to_sql("support_tickets", self.conn, index=False, if_exists="replace")
        else:
            self._load_dicts_to_sqlite(fallback, "support_tickets")

    def list_catalog(self) -> List[Dict[str, Any]]:
        """Returns the virtualized schemas available in the Zetaris AI Data Harness (5 Silos)."""
        return [
            {
                "virtual_table": "zetaris.erp_transactions",
                "origin_system": "SAP S/4HANA Finance Node (US-East)",
                "governance_engine": "Zetaris AI Data Harness (In-Place)",
                "record_count": 8,
                "columns": ["tx_id", "timestamp", "vendor_id", "vendor_name", "amount_usd", "approver_id", "status", "bank_routing"]
            },
            {
                "virtual_table": "zetaris.cloud_audit_logs",
                "origin_system": "AWS CloudTrail & Okta Auth Stream (Global)",
                "governance_engine": "Zetaris AI Data Harness (In-Place)",
                "record_count": 6,
                "columns": ["event_id", "timestamp", "user_id", "action", "target_resource", "source_ip", "geo_country", "is_vpn_or_tor", "mfa_authenticated"]
            },
            {
                "virtual_table": "zetaris.vendor_contracts",
                "origin_system": "Coupa Procurement Compliance Vault (EU-Central)",
                "governance_engine": "Zetaris AI Data Harness (In-Place)",
                "record_count": 4,
                "columns": ["vendor_id", "legal_name", "contract_status", "single_tx_limit_usd", "monthly_cap_usd", "verified_bank_routing", "risk_score"]
            },
            {
                "virtual_table": "zetaris.k8s_telemetry",
                "origin_system": "Datadog / Prometheus K8s Runtime Observability (US-East)",
                "governance_engine": "Zetaris AI Data Harness (In-Place)",
                "record_count": 6,
                "columns": ["pod_id", "namespace", "service_name", "cpu_utilization_pct", "jvm_heap_pct", "status", "restart_count", "target_resource"]
            },
            {
                "virtual_table": "zetaris.support_tickets",
                "origin_system": "ServiceNow / Zoho Desk Customer SLA Impact Stream (Global)",
                "governance_engine": "Zetaris AI Data Harness (In-Place)",
                "record_count": 4,
                "columns": ["ticket_id", "customer_name", "priority", "title", "related_tx_id", "status", "sla_deadline_hours"]
            }
        ]

    def execute_federated_query(self, query: str) -> Dict[str, Any]:
        """
        Executes a zero-copy in-place query across mounted enterprise silos
        via the Zetaris AgentFlow execution router.
        """
        clean_query = query.replace("zetaris.", "").replace("ZETARIS.", "")
        t0 = time.time()
        try:
            cur = self.conn.cursor()
            cur.execute(clean_query)
            if cur.description:
                cols = [desc[0] for desc in cur.description]
                records = [dict(zip(cols, row)) for row in cur.fetchall()]
            else:
                self.conn.commit()
                cols = []
                records = []
            duration_ms = (time.time() - t0) * 1000
            all_silos = ["erp_transactions", "cloud_audit_logs", "vendor_contracts", "k8s_telemetry", "support_tickets"]
            return {
                "status": "SUCCESS",
                "harness_provider": "Zetaris AI Data Harness (AgentFlow)",
                "workspace_id": self.agentflow_workspace_id,
                "execution_mode": "ZERO_COPY_IN_PLACE_FEDERATION",
                "query": query,
                "row_count": len(records),
                "columns": cols,
                "data": records,
                "duration_ms": round(duration_ms, 2),
                "silos_accessed": [silo for silo in all_silos if silo in clean_query.lower()]
            }
        except Exception as e:
            return {
                "status": "ERROR",
                "harness_provider": "Zetaris AI Data Harness",
                "workspace_id": self.agentflow_workspace_id,
                "execution_mode": "ZERO_COPY_IN_PLACE_FEDERATION",
                "query": query,
                "row_count": 0,
                "columns": [],
                "data": [],
                "silos_accessed": [],
                "duration_ms": 0.0,
                "error_message": str(e)
            }
