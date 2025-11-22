
AWS Incident Assistant

A lightweight multi-agent on-call companion that analyzes real AWS CloudWatch logs and metrics, detects anomalies, and generates a clear incident summary with the most likely root cause and next steps.

Built using AWS Strands Agents, Amazon Q Developer, Amazon Kiro, AWS Lambda, CloudWatch, and Bedrock — all within the AWS Free Tier.

⸻

What It Does
	•	Polls CloudWatch metrics to detect latency spikes, error bursts, memory issues, and retry storms.
	•	Fetches logs for the alert window and identifies patterns (timeouts, slow downstream calls, OOM events, retries).
	•	Combines signals to produce a concise root cause explanation.
	•	Shows a transparent analysis trace so engineers understand why a conclusion was reached.
	•	Provides a simple UI with:
	•	Alerts View
	•	Incident View
	•	Logs, metrics, agent summaries, and full reasoning steps.

⸻

How It Works

Lambda → CloudWatch Logs + Metrics
        ↓
Metrics Analyst Agent → alerts
        ↓
Log Investigator Agent
        ↓
Root Cause & Fix Agent
        ↓
Incident View UI

A demo Lambda generates realistic operational behavior so the system works with real AWS signals.

⸻

Built With AWS AI Tools

Amazon Q Developer

Used for:
	•	scaffolding agent code
	•	generating CloudWatch queries
	•	validating boto3 calls
	•	writing deployment scripts

Amazon Kiro

Used for:
	•	spec-driven workflows
	•	multi-step agent logic
	•	code generation and refinement

Screenshots included in submission.

⸻

Project Structure

aws-incident-assistant/
  agents/
  tools/
  orchestrator/
  lambda/
  ui/
  docs/
  README.md


⸻

Setup

Deploy Lambda

cd lambda
sh deploy.sh

Run Strands Agents

strands agents run

Open the UI

Open alerts.html in a browser or serve via Flask.

⸻

Why This Project Matters
	•	Uses real AWS telemetry in a practical way
	•	Shows meaningful multi-agent collaboration
	•	Provides explainability (thinking log)
	•	Helpful to real on-call engineers
	•	Free-tier friendly and easy to extend

