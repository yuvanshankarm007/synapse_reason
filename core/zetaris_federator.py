"""
Zetaris Networked Data Fabric & Virtualization Connector
Allows the Reasoning Agent to execute zero-copy federated queries across 
heterogeneous enterprise silos (ERP SQL, CloudWatch JSON logs, Vendor Registry).
"""
import sqlite3
import pandas as pd
import json
from typing import Dict, Any, List
import config

class ZetarisFederator:
    """Virtualizes distributed data sources into a unified queryable fabric."""
    def __init__(self):
        self.conn = sqlite3.connect(":memory:", check_same_thread=False)
        self._initialize_virtual_fabric()

    def _initialize_virtual_fabric(self):
        """Mounts heterogeneous silos into the Zetaris virtual catalog."""
        # 1. Mount ERP Transactions (CSV Silo)
        erp_csv_path = config.DATA_DIR / "erp_transactions.csv"
        if erp_csv_path.exists():
            df_erp = pd.read_csv(erp_csv_path)
            df_erp.to_sql("erp_transactions", self.conn, index=False, if_exists="replace")

        # 2. Mount Cloud Audit Logs (JSON Silo)
        cloud_json_path = config.DATA_DIR / "cloud_audit_logs.json"
        if cloud_json_path.exists():
            with open(cloud_json_path, "r", encoding="utf-8") as f:
                logs_data = json.load(f)
            df_logs = pd.DataFrame(logs_data)
            df_logs.to_sql("cloud_audit_logs", self.conn, index=False, if_exists="replace")

        # 3. Mount Vendor Procurement Contracts (JSON Silo)
        vendor_json_path = config.DATA_DIR / "vendor_contracts.json"
        if vendor_json_path.exists():
            with open(vendor_json_path, "r", encoding="utf-8") as f:
                vendor_data = json.load(f)
            df_vendor = pd.DataFrame(vendor_data)
            df_vendor.to_sql("vendor_contracts", self.conn, index=False, if_exists="replace")

    def list_catalog(self) -> List[Dict[str, Any]]:
        """Returns the virtualized schemas available in the Zetaris Fabric."""
        return [
            {
                "virtual_table": "zetaris.erp_transactions",
                "origin_system": "SAP S/4HANA Finance Node (US-East)",
                "record_count": 8,
                "columns": ["tx_id", "timestamp", "vendor_id", "vendor_name", "amount_usd", "approver_id", "status", "bank_routing"]
            },
            {
                "virtual_table": "zetaris.cloud_audit_logs",
                "origin_system": "AWS CloudTrail & Okta Auth Stream (Global)",
                "record_count": 6,
                "columns": ["event_id", "timestamp", "user_id", "action", "target_resource", "source_ip", "geo_country", "is_vpn_or_tor", "mfa_authenticated"]
            },
            {
                "virtual_table": "zetaris.vendor_contracts",
                "origin_system": "Coupa Procurement Compliance Vault (EU-Central)",
                "record_count": 4,
                "columns": ["vendor_id", "legal_name", "contract_status", "single_tx_limit_usd", "monthly_cap_usd", "verified_bank_routing", "risk_score"]
            }
        ]

    def execute_federated_query(self, query: str) -> Dict[str, Any]:
        """
        Executes a zero-copy federated SQL query across mounted enterprise silos.
        Normalizes 'zetaris.' table prefixes for local federated execution.
        """
        clean_query = query.replace("zetaris.", "").replace("ZETARIS.", "")
        try:
            df = pd.read_sql_query(clean_query, self.conn)
            records = df.to_dict(orient="records")
            return {
                "status": "SUCCESS",
                "fabric_provider": "Zetaris Networked Data Fabric",
                "query": query,
                "row_count": len(records),
                "columns": list(df.columns),
                "data": records,
                "silos_accessed": [
                    silo for silo in ["erp_transactions", "cloud_audit_logs", "vendor_contracts"]
                    if silo in clean_query.lower()
                ]
            }
        except Exception as e:
            return {
                "status": "ERROR",
                "fabric_provider": "Zetaris Networked Data Fabric",
                "query": query,
                "error_message": str(e)
            }
