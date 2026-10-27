"""
Zetaris AI Data Harness & AgentFlow Virtualization Connector
Allows the Reasoning Agent to execute zero-copy in-place federated queries across 
heterogeneous enterprise silos (ERP SQL, CloudTrail JSON logs, Vendor Registry)
governed by Zetaris AgentFlow workspaces and access policies.
"""
import sqlite3
import pandas as pd
import json
import time
from typing import Dict, Any, List
import config

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
                df_erp = pd.read_csv(erp_csv_path)
                df_erp.to_sql("erp_transactions", self.conn, index=False, if_exists="replace")
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
                df_logs = pd.DataFrame(logs_data)
                df_logs.to_sql("cloud_audit_logs", self.conn, index=False, if_exists="replace")
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
                df_vendor = pd.DataFrame(vendor_data)
                df_vendor.to_sql("vendor_contracts", self.conn, index=False, if_exists="replace")
            else:
                self._load_fallback_vendor()
        except Exception as e:
            print(f"[ZetarisFederator] Warning loading Vendor JSON ({e}), loading fallback.")
            self._load_fallback_vendor()

    def _load_fallback_erp(self):
        fallback = [
            {"tx_id": "TX-90214", "timestamp": "2026-10-26T14:10:00Z", "vendor_id": "VND-8821", "vendor_name": "Acrobatics Logistics LLC", "amount_usd": 184500.0, "approver_id": "USR-9912", "status": "SETTLED_WIRE", "bank_routing": "021000021"},
            {"tx_id": "TX-90219", "timestamp": "2026-10-27T09:15:00Z", "vendor_id": "VND-8821", "vendor_name": "Acrobatics Logistics LLC", "amount_usd": 245000.0, "approver_id": "USR-9912", "status": "PENDING_SETTLEMENT", "bank_routing": "021000021"}
        ]
        pd.DataFrame(fallback).to_sql("erp_transactions", self.conn, index=False, if_exists="replace")

    def _load_fallback_cloud(self):
        fallback = [
            {"event_id": "EVT-88102", "timestamp": "2026-10-27T09:12:00Z", "user_id": "USR-9912", "action": "APPROVE_DISBURSEMENT", "target_resource": "TX-90219", "source_ip": "185.220.101.45", "geo_country": "SC (Seychelles)", "is_vpn_or_tor": 1, "mfa_authenticated": 0}
        ]
        pd.DataFrame(fallback).to_sql("cloud_audit_logs", self.conn, index=False, if_exists="replace")

    def _load_fallback_vendor(self):
        fallback = [
            {"vendor_id": "VND-8821", "legal_name": "Acrobatics Logistics LLC", "contract_status": "ACTIVE_STANDARD", "single_tx_limit_usd": 50000.0, "monthly_cap_usd": 200000.0, "verified_bank_routing": "011000015", "risk_score": 0.88}
        ]
        pd.DataFrame(fallback).to_sql("vendor_contracts", self.conn, index=False, if_exists="replace")

    def list_catalog(self) -> List[Dict[str, Any]]:
        """Returns the virtualized schemas available in the Zetaris AI Data Harness."""
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
            df = pd.read_sql_query(clean_query, self.conn)
            records = df.to_dict(orient="records")
            duration_ms = (time.time() - t0) * 1000
            return {
                "status": "SUCCESS",
                "harness_provider": "Zetaris AI Data Harness (AgentFlow)",
                "workspace_id": self.agentflow_workspace_id,
                "execution_mode": "ZERO_COPY_IN_PLACE_FEDERATION",
                "query": query,
                "row_count": len(records),
                "columns": list(df.columns),
                "data": records,
                "duration_ms": round(duration_ms, 2),
                "silos_accessed": [
                    silo for silo in ["erp_transactions", "cloud_audit_logs", "vendor_contracts"]
                    if silo in clean_query.lower()
                ]
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
