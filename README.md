# AWS Cost Monitor — Jenkins CI/CD Pipeline

Automated AWS cost monitoring pipeline built with Jenkins, integrated with AWS Cost Explorer API for daily cost tracking and threshold-based alerting.

## ✅ Pipeline Status: SUCCESS

Successfully tested and verified — pipeline fetches live AWS cost data and runs end-to-end without errors.

**Sample Output (Build #6):**

    AWS Cost (Last 30 days): $0.00 USD
    OK: Cost $0.00 is within limit $10.00
    Pipeline completed!
    Cost check passed!
    Finished: SUCCESS

## Features
- Daily automated cost checks via Jenkins cron trigger
- Real-time AWS Cost Explorer API integration
- Threshold-based alerting system
- Secure IAM role-based authentication (no hardcoded credentials)
- Clean pipeline stages: Checkout → Setup → Fetch Cost → Report

## Tech Stack
- **CI/CD:** Jenkins (deployed on AWS EC2)
- **Cloud:** AWS EC2, IAM, Cost Explorer API
- **Language:** Python (boto3)
- **Version Control:** Git & GitHub

## Pipeline Stages
| Stage | Description |
|-------|-------------|
| Checkout | Pull latest code from GitHub repository |
| Setup | Install Python dependencies |
| Fetch & Analyze Cost | Query AWS Cost Explorer and check against threshold |
| Report | Output summary of cost status |

## Architecture
GitHub Repo → Jenkins Pipeline (EC2) → AWS Cost Explorer API → Threshold Check → Alert/Report

## Key Learnings
- Setting up Jenkins on AWS EC2 from scratch (manual WAR-based installation)
- Configuring IAM roles for secure, credential-free AWS API access
- Writing declarative Jenkins pipelines with multi-stage execution
- Troubleshooting GPG/repository and Java version compatibility issues
- CI/CD automation for cloud cost governance (FinOps practice)

## Author
**Amit Dorwekar** — Aspiring DevOps/Cloud Engineer
