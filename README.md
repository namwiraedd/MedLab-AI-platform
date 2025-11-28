# MedLab-AI-platform
End-to-end, cloud-based laboratory &amp; referral platform (chemistry, hematology, digital pathology, forensic chain-of-custody) — staging-ready with synthetic data, MLflow notebooks, IaC, CI/CD, and role-based portals.
This repository demonstrates the complete workflow on synthetic data and includes:

Terraform IaC (AWS example) for networking, EKS cluster, RDS (Postgres) and S3 bucket

Docker Compose for local/staging orchestration (FastAPI app, MLflow, MinIO, Postgres, Keycloak)

FastAPI backend implementing LIMS APIs, FHIR/HL7 shim, sample intake and referral endpoints, Keycloak JWT validation

Minimal frontend placeholders (React) for role-based portals (lab staff / clinician / specialist / police/army)

ML service (PyTorch) with MLflow instrumented training & inference server (TorchScript example)

Notebook-style reproducible MLflow training script + dataset generator (synthetic data + whole-slide image placeholder)

Referral engine microservice (simple rules+capacity matcher) and notification stubs (email + webhook)

Chain-of-custody evidence store pattern (immutable metadata anchoring) and simple audit logs

CI/CD (GitHub Actions): lint/test, build & push container, terraform plan/apply (placeholder), and deploy to staging

Tests (pytest) and load/perf script (locust stub)

Security: Keycloak integration sample, TLS pointers, AES-256 encryption hooks for sensitive blobs

Compliance checklist (ISO 15189, HIPAA/GDPR mapping) and audit-report generator stub
