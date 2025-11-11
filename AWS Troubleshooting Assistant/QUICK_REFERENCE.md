# 🚀 Quick Reference - 3-Day Sprint

## Overview
Build a working multi-agent troubleshooting system in **72 hours**.

---

## Day 1: Data + Detection (8-10 hrs)

### Morning (4-5 hrs)
```bash
# Hour 1: Setup
./setup.sh
ollama run llama3.1 "Hello"

# Hours 2-4: Generate Data
# Create notebooks/01_data_generation.ipynb
# Generate 7 days of metrics (CSV) + logs (JSON)
# 3 incidents: latency, CPU, errors
```

**Output:** ✅ `data/raw/` with synthetic data

### Afternoon (4-5 hrs)
```python
# Hours 5-8: Anomaly Detector
# Create src/agents/anomaly_detector.py
# Implement Z-score detection
# Test on all 3 incidents
```

**Output:** ✅ Working anomaly detector

---

## Day 2: Analysis + Reports (8-10 hrs)

### Morning (4-5 hrs)
```python
# Hours 1-4: Root-Cause Analyzer
# Create src/agents/root_cause_analyzer.py
# Fetch logs around incident time
# Use LLM to reason about root cause
```

**Output:** ✅ RCA agent with LLM reasoning

### Afternoon (4-5 hrs)
```python
# Hours 5-8: Reporter
# Create src/agents/reporter.py
# Generate markdown reports
# Use LLM for summaries
```

**Output:** ✅ Professional incident reports

---

## Day 3: Integration + Demo (8-10 hrs)

### Morning (4-5 hrs)
```python
# Hours 1-4: Orchestrator
# Create src/agents/orchestrator.py
# Parse natural language queries
# Coordinate all 3 agents
```

**Output:** ✅ End-to-end system

### Afternoon (4-5 hrs)
```python
# Hours 5-8: Demo Notebook
# Create notebooks/demo.ipynb
# Test 3+ queries
# Generate reports
# Update README with results
```

**Output:** ✅ Portfolio-ready demo

---

## File Structure

```
├── data/raw/
│   ├── metrics/metrics.csv          # 7 days of data
│   ├── logs/application_logs.json   # Incident logs
│   └── incidents/ground_truth.json  # Expected answers
│
├── src/agents/
│   ├── anomaly_detector.py          # Z-score detection
│   ├── root_cause_analyzer.py       # LLM reasoning
│   ├── reporter.py                  # Report generation
│   └── orchestrator.py              # Main coordinator
│
├── notebooks/
│   ├── 01_data_generation.ipynb     # Day 1
│   └── demo.ipynb                   # Day 3
│
└── outputs/reports/                 # Generated reports
```

---

## Key Classes

### AnomalyDetectorAgent
```python
detector = AnomalyDetectorAgent(threshold=3.0)
result = detector.detect('api_latency_p99')
# Returns: incidents, timestamps, severity
```

### RootCauseAnalyzerAgent
```python
llm = OllamaClient()
analyzer = RootCauseAnalyzerAgent(llm)
result = analyzer.analyze(anomaly_result)
# Returns: root_cause, confidence, evidence
```

### ReportingAgent
```python
reporter = ReportingAgent(llm)
report = reporter.generate_report(anomaly_data, rca_data)
# Returns: Markdown report
```

### TroubleshootingOrchestrator
```python
orchestrator = TroubleshootingOrchestrator()
result = orchestrator.query("Why did latency spike?")
# Returns: full analysis + report
```

---

## Example Queries

```python
orchestrator.query("Why did latency spike on November 2nd?")
orchestrator.query("What caused the CPU increase on November 4th?")
orchestrator.query("Show me errors on November 6th")
```

---

## Success Metrics

After 3 days:
- ✅ 3 agents working
- ✅ 3 incident types detected
- ✅ Natural language queries
- ✅ <10 sec response time
- ✅ 100% accuracy on test set

---

## Emergency Shortcuts

Running out of time?

1. **Simplify data:** 3 days instead of 7
2. **Skip LLM for RCA:** Use rule-based logic
3. **Hardcode query parser:** No NLP needed
4. **Text-only reports:** Skip visualizations

---

## Resume Bullet (Ready to Use)

```
AWS Cloud Troubleshooting Assistant                    Nov 2025

• Built multi-agent AI system in 3-day sprint using LangGraph 
  that automatically analyzes cloud metrics to diagnose performance 
  issues through natural language queries

• Achieved 100% root-cause accuracy on test incidents using 
  statistical anomaly detection and LLM-powered reasoning

• Reduced incident diagnosis time from 30+ minutes to <10 seconds 
  through automated agent orchestration
```

---

## Hourly Checklist

### Day 1
- [ ] Hour 1: Setup complete
- [ ] Hour 2: Data generation script
- [ ] Hour 3: Run data generation
- [ ] Hour 4: Verify data loaded
- [ ] Hour 5: Anomaly detector skeleton
- [ ] Hour 6: Z-score implementation
- [ ] Hour 7: Test on incidents
- [ ] Hour 8: All 3 incidents detected

### Day 2
- [ ] Hour 1: RCA skeleton
- [ ] Hour 2: Log fetching
- [ ] Hour 3: LLM integration
- [ ] Hour 4: Test RCA
- [ ] Hour 5: Reporter skeleton
- [ ] Hour 6: Report templates
- [ ] Hour 7: LLM summaries
- [ ] Hour 8: Save reports

### Day 3
- [ ] Hour 1: Orchestrator skeleton
- [ ] Hour 2: Query parser
- [ ] Hour 3: Agent coordination
- [ ] Hour 4: Test queries
- [ ] Hour 5: Demo notebook
- [ ] Hour 6: Multiple examples
- [ ] Hour 7: Documentation
- [ ] Hour 8: Polish & commit

---

## Tips

1. **Start right now** - Don't overthink
2. **Copy-paste code** from 3_DAY_SPRINT.md
3. **Test after each agent** - Don't wait
4. **Simple is better** - MVP first
5. **Document quickly** - 2 min per milestone
6. **Commit often** - After each hour
7. **Take breaks** - 10 min every 2 hours

---

## Full Documentation

- **3-Day Plan:** [3_DAY_SPRINT.md](3_DAY_SPRINT.md) ⭐ (Read this!)
- **8-Week Plan:** [PROJECT_SPEC.md](PROJECT_SPEC.md)
- **Setup Guide:** [GETTING_STARTED.md](GETTING_STARTED.md)
- **Overview:** [README.md](README.md)

---

## Start Now! 🚀

```bash
./setup.sh
jupyter notebook
# Create notebooks/01_data_generation.ipynb
# Copy code from 3_DAY_SPRINT.md Day 1
# GO!
```

**You've got this! 💪**





