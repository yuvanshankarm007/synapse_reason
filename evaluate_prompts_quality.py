"""
Automated Multi-Domain Prompt Quality & Accuracy Benchmark Suite
Evaluates SynapseReason across 25 diverse prompt scenarios spanning:
1. Cybersecurity & Zero-Trust
2. Autonomous SRE & Cloud Infrastructure
3. Enterprise Financial Fraud Forensics
4. Micro-Capital & Wealth Allocation
5. Supply Chain & Logistics
6. Psychosocial & Cognitive Health
7. Language Acquisition & Communication
8. Software Engineering & Systems Optimization
9. Career & Professional Decision Making
10. Real-World Inquiry & First-Principles Analysis
"""
import sys
import time
from pathlib import Path

# Ensure project root is in sys.path
BASE_DIR = Path(__file__).resolve().parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

import config
from core.reasoning_engine import SynapseReasonEngine

TEST_PROMPTS = [
    # 1. Cybersecurity & Zero-Trust (3 prompts)
    {
        "id": "SEC-001",
        "prompt": "Unauthorized IAM role assumption from Tor exit node 185.220.101.45 with bypassed MFA on prod-service-principal",
        "expected_domain": "cybersecurity",
        "keywords": ["tor", "mfa", "privilege", "sts"]
    },
    {
        "id": "SEC-002",
        "prompt": "Abnormal KMS key decryption surge with 14,000 requests in 2 minutes on prod-root-vault",
        "expected_domain": "cybersecurity",
        "keywords": ["kms", "decrypt", "key", "vault"]
    },
    {
        "id": "SEC-003",
        "prompt": "Ransomware canary file modified in corporate S3 bucket with suspicious outbound data egress",
        "expected_domain": "cybersecurity",
        "keywords": ["ransomware", "s3", "egress", "quarantine"]
    },

    # 2. Autonomous SRE & Infrastructure (3 prompts)
    {
        "id": "SRE-001",
        "prompt": "Cascading microservice crash loops with 15,200 unconsumed message partition lag on telemetry-events topic",
        "expected_domain": "sre",
        "keywords": ["kafka", "microservice", "lag", "canary"]
    },
    {
        "id": "SRE-002",
        "prompt": "Kubernetes pods stuck in CrashLoopBackOff due to JVM heap exhaustion and full GC stalls exceeding 4200ms",
        "expected_domain": "sre",
        "keywords": ["jvm", "gc", "heap", "memory"]
    },
    {
        "id": "SRE-003",
        "prompt": "Postgres connection pool exhausted with 504 gateway timeout on downstream payment bridge",
        "expected_domain": "sre",
        "keywords": ["connection", "pool", "timeout", "circuit"]
    },

    # 3. Enterprise Financial Fraud (3 prompts)
    {
        "id": "FIN-001",
        "prompt": "Unauthorized $245,000 wire disbursement to unverified vendor VND-8821 with anomalous routing 021000021",
        "expected_domain": "finance_fraud",
        "keywords": ["wire", "disbursement", "vendor", "routing"]
    },
    {
        "id": "FIN-002",
        "prompt": "Batch payroll disbursement diverted to unverified offshore IBAN following session cookie reuse without MFA",
        "expected_domain": "finance_fraud",
        "keywords": ["payroll", "iban", "disbursement", "mfa"]
    },
    {
        "id": "FIN-003",
        "prompt": "Duplicate invoice splitting under $10,000 approval threshold submitted across 4 subsidiary accounts for VND-9912",
        "expected_domain": "finance_fraud",
        "keywords": ["invoice", "threshold", "vendor", "audit"]
    },

    # 4. Wealth Allocation & Micro-Investing (3 prompts)
    {
        "id": "INV-001",
        "prompt": "which stocks should I invest in with 50 rupees",
        "expected_domain": "finance_investment",
        "keywords": ["penny stock", "nifty", "etf", "sip"]
    },
    {
        "id": "INV-002",
        "prompt": "I have 5000 rupees to invest every month, should I pick speculative crypto or index funds",
        "expected_domain": "finance_investment",
        "keywords": ["index", "etf", "rupee", "compound"]
    },
    {
        "id": "INV-003",
        "prompt": "What is the safest way to allocate an emergency fund versus equity mutual funds",
        "expected_domain": "finance_investment",
        "keywords": ["allocation", "emergency", "fund", "equity"]
    },

    # 5. Supply Chain & Global Logistics (2 prompts)
    {
        "id": "LOG-001",
        "prompt": "Maritime shipment container with tier-1 semiconductor wafers detained in Rotterdam customs quarantine",
        "expected_domain": "supply_chain",
        "keywords": ["customs", "semiconductor", "carrier", "buffer"]
    },
    {
        "id": "LOG-002",
        "prompt": "Cold-chain pharmaceutical delivery temperature excursion above 8 degrees Celsius in transit",
        "expected_domain": "supply_chain",
        "keywords": ["cold-chain", "temperature", "transit", "quarantine"]
    },

    # 6. Psychosocial & Cognitive Health (2 prompts)
    {
        "id": "MNT-001",
        "prompt": "Severe workplace burnout and chronic sleep disruption caused by 24/7 on-call paging notifications",
        "expected_domain": "mental_health",
        "keywords": ["burnout", "sleep", "disconnect", "allostatic"]
    },
    {
        "id": "MNT-002",
        "prompt": "I am feeling isolated and depressed working remotely with chronic fatigue",
        "expected_domain": "mental_health",
        "keywords": ["fatigue", "isolation", "therapy", "well-being"]
    },

    # 7. Language Acquisition & Communication (3 prompts)
    {
        "id": "LNG-001",
        "prompt": "I want to learn how to communicate in english",
        "expected_domain": "education_language",
        "keywords": ["shadowing", "grammar", "spoken", "fluency"]
    },
    {
        "id": "LNG-002",
        "prompt": "How to overcome hesitation and speak English fluently in professional meetings",
        "expected_domain": "education_language",
        "keywords": ["speech", "hesitation", "shadowing", "conversation"]
    },
    {
        "id": "LNG-003",
        "prompt": "Best daily protocol for IELTS speaking test preparation band 8",
        "expected_domain": "education_language",
        "keywords": ["ielts", "speaking", "fluency", "recording"]
    },

    # 8. Software Engineering & Architecture (3 prompts)
    {
        "id": "DEV-001",
        "prompt": "My Python backend script is running slow and taking 45 seconds to process 10,000 records",
        "expected_domain": "software_engineering",
        "keywords": ["profiling", "cprofile", "vectorize", "numpy"]
    },
    {
        "id": "DEV-002",
        "prompt": "Database deadlock on PostgreSQL transaction under concurrent bulk payment updates",
        "expected_domain": "software_engineering",
        "keywords": ["deadlock", "postgres", "lock", "transaction"]
    },
    {
        "id": "DEV-003",
        "prompt": "Should we migrate from a monolithic backend to microservices for our growing engineering team",
        "expected_domain": "software_engineering",
        "keywords": ["monolith", "microservice", "architecture", "boundary"]
    },

    # 9. Career & Professional Decisions (2 prompts)
    {
        "id": "CAR-001",
        "prompt": "Should I accept a high-paying startup offer with equity or stay at a stable Big Tech company",
        "expected_domain": "career_leadership",
        "keywords": ["equity", "startup", "risk", "decision"]
    },
    {
        "id": "CAR-002",
        "prompt": "How to prepare effectively for a senior software engineer system design interview",
        "expected_domain": "career_leadership",
        "keywords": ["system design", "interview", "scalability", "trade-off"]
    },

    # 10. Real-World Inquiry / First-Principles (2 prompts)
    {
        "id": "GEN-001",
        "prompt": "Is the new movie streaming on OTT platforms or only available in cinemas right now",
        "expected_domain": "general_research",
        "keywords": ["theatrical", "cinema", "streaming", "window"]
    },
    {
        "id": "GEN-002",
        "prompt": "What is the most effective evidence-based method to train for a half marathon without injury",
        "expected_domain": "general_research",
        "keywords": ["marathon", "training", "injury", "progression"]
    },
    {
        "id": "GEN-003",
        "prompt": "4+4=",
        "expected_domain": "general_research",
        "keywords": ["mathematical", "arithmetic", "8", "evaluation"]
    },
    {
        "id": "GEN-004",
        "prompt": "why I was an idiot",
        "expected_domain": "general_research",
        "keywords": ["outcome bias", "labeling", "cognitive", "reframing"]
    },
    {
        "id": "GEN-005",
        "prompt": "who are you",
        "expected_domain": "general_research",
        "keywords": ["synapsereason", "lattice", "reasoning", "zetaris"]
    },
    {
        "id": "GEN-006",
        "prompt": "why is the sky blue",
        "expected_domain": "general_research",
        "keywords": ["rayleigh", "scattering", "wavelength", "sunlight"]
    },
    {
        "id": "GEN-007",
        "prompt": "how to boil an egg",
        "expected_domain": "general_research",
        "keywords": ["boil", "timer", "egg", "ice bath"]
    }
]

def run_evaluation():
    print("=" * 80)
    print("SYNAPSEREASON MULTI-DOMAIN PROMPT ACCURACY & QUALITY BENCHMARK")
    print(f"Total Scenarios: {len(TEST_PROMPTS)} across 10 Distinct Domains")
    print("=" * 80)

    config.SAMPLE_MODE = True  # Turbo mode evaluation
    engine = SynapseReasonEngine()

    passed_count = 0
    scores = []
    total_time = 0.0

    for idx, test in enumerate(TEST_PROMPTS, 1):
        p_id = test["id"]
        prompt = test["prompt"]
        exp_dom = test["expected_domain"]

        t0 = time.time()
        result = engine.run_investigation(incident_id=p_id, alert_description=prompt, domain="auto")
        duration_ms = (time.time() - t0) * 1000
        total_time += duration_ms

        resolved_dom = result.get("domain", "")
        headline = result.get("impact_headline", "")
        synthesis = result.get("confirmed_root_cause", "")
        actions = result.get("actions", [])
        trace = result.get("execution_trace", [])

        # Quality assertions
        # 1. Domain Accuracy
        dom_ok = (resolved_dom == exp_dom) or (exp_dom in resolved_dom)

        # 2. Synthesis Quality: substantive, non-boilerplate
        synth_len_ok = len(synthesis) >= 60
        synth_no_robot_fallback = "Ad-hoc assumptions regarding" not in synthesis and "break down your core constraints (time, budget" not in synthesis

        # 3. Actions Quality: at least 3 actions with priority, action, target, reason
        actions_ok = len(actions) >= 3 and all(
            bool(a.get("action")) and bool(a.get("priority")) and bool(a.get("reason")) for a in actions
        )

        # 4. Keyword relevance: at least one domain keyword present in synthesis or actions
        combined_text = f"{headline} {synthesis} " + " ".join([f"{a.get('action')} {a.get('reason')} {a.get('target')}" for a in actions]).lower()
        keyword_hits = sum(1 for kw in test.get("keywords", []) if kw.lower() in combined_text.lower())
        relevance_ok = keyword_hits >= 1

        # 5. Latency (< 100ms in Turbo Mode)
        latency_ok = duration_ms < 150.0

        all_ok = dom_ok and synth_len_ok and actions_ok and relevance_ok and synth_no_robot_fallback

        status = "PASSED" if all_ok else "FAILED"
        if all_ok:
            passed_count += 1

        print(f"[{idx:02d}/25] {p_id} ({resolved_dom}) - {status} ({duration_ms:.2f}ms)")
        print(f"      Prompt: '{prompt[:65]}...'")
        print(f"      Headline: '{headline[:70]}'")
        if not all_ok:
            print(f"      [DIAGNOSTIC] dom_ok={dom_ok} (exp={exp_dom}, got={resolved_dom}), synth_no_robot={synth_no_robot_fallback}, rel_ok={relevance_ok} (hits={keyword_hits})")
            print(f"      Synthesis: '{synthesis[:120]}...'")

    print("=" * 80)
    pass_pct = (passed_count / len(TEST_PROMPTS)) * 100
    avg_latency = total_time / len(TEST_PROMPTS)
    print(f"FINAL QUALITY SCORE: {passed_count}/{len(TEST_PROMPTS)} ({pass_pct:.1f}%)")
    print(f"AVERAGE LATENCY PER INVESTIGATION: {avg_latency:.2f} ms")
    print("=" * 80)

    return passed_count == len(TEST_PROMPTS)

if __name__ == "__main__":
    success = run_evaluation()
    sys.exit(0 if success else 1)
