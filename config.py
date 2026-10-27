"""
SynapseReason Configuration & Runtime Settings
Supports seamless switching between SAMPLE_MODE (zero keys needed) and LIVE_MODE.
"""
import os
from pathlib import Path
from dotenv import load_dotenv

# Base Directory Paths
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

# Load .env if present
load_dotenv(BASE_DIR / ".env")

# Runtime Execution Mode
# If SAMPLE_MODE is True, use high-fidelity benchmark simulator for automated tests
SAMPLE_MODE = os.getenv("SAMPLE_MODE", "false").lower() in ("true", "1", "yes")

# Sponsor API Configurations
NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY", "")
NVIDIA_BASE_URL = os.getenv("NVIDIA_BASE_URL", "https://integrate.api.nvidia.com/v1")
NVIDIA_MODEL = os.getenv("NVIDIA_MODEL", "nvidia/nemotron-3.5-lightning-30b-a3b")

# Ollama Local LLM Configuration (Real-time dynamic generation, zero keys required)
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://127.0.0.1:11434/v1")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "qwen2.5:7b")

# Active LLM Provider Selection: "auto", "ollama", "nvidia", "custom"
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "auto")

# Zetaris Networked Data Virtualization / Fabric Endpoint
ZETARIS_ENDPOINT = os.getenv("ZETARIS_ENDPOINT", "https://fabric.zetaris.cloud/api/v1")
ZETARIS_API_KEY = os.getenv("ZETARIS_API_KEY", "zetaris_live_sample_token_7721")

# Meterless Serverless Cost, Token & Budget Governance
METERLESS_ENDPOINT = os.getenv("METERLESS_ENDPOINT", "https://api.meterless.io/v1/telemetry")
METERLESS_API_KEY = os.getenv("METERLESS_API_KEY", "meterless_live_sample_token_8892")
METERLESS_BUDGET_CAP_USD = float(os.getenv("METERLESS_BUDGET_CAP_USD", "0.50")) # Max $0.50 per investigation

# Bright Data Web Scraping / SERP Bounty Endpoint
BRIGHTDATA_API_KEY = os.getenv("BRIGHTDATA_API_KEY", "brightdata_sample_token_1092")

# Token Cost Benchmarks (NVIDIA NIM Llama-3.1-70B rates)
INPUT_TOKEN_COST_PER_MILLION = 0.70   # $0.70 per 1M input tokens
OUTPUT_TOKEN_COST_PER_MILLION = 0.90  # $0.90 per 1M output tokens
ZETARIS_QUERY_COST_ESTIMATE = 0.002   # $0.002 per federated virtual query
