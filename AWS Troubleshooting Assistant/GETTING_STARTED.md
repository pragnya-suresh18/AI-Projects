# Getting Started - AWS Cloud Troubleshooting Assistant

> 🎓 **100% Free Student Implementation** - No AWS account or API costs required!

## What You've Got

This project specification gives you everything needed to build a professional multi-agent AI system:

1. **Complete Architecture** - Multi-agent design with orchestrator pattern
2. **Free Implementation** - Uses Ollama (local LLM), no cloud costs
3. **8-Week Roadmap** - Step-by-step implementation guide
4. **Synthetic Data** - Generate realistic cloud metrics and logs locally
5. **Portfolio-Ready** - Impressive resume project

## Project Files

```
📁 Your Project
├── 📄 README.md                  ← Project overview
├── 📄 PROJECT_SPEC.md            ← 80-page detailed specification ⭐
├── 📄 GETTING_STARTED.md         ← You are here!
├── 📄 requirements.txt           ← Python dependencies
├── 📄 config.yaml.example        ← Configuration template
├── 📄 .gitignore                 ← Git ignore rules
├── 🔧 setup.sh                   ← Auto-setup script (Mac/Linux)
└── 🔧 setup.bat                  ← Auto-setup script (Windows)
```

## Quick Start (Choose Your Path)

### Option A: Automated Setup (Recommended) ⚡

**Mac/Linux:**
```bash
./setup.sh
```

**Windows:**
```batch
setup.bat
```

This automatically:
- ✅ Installs Ollama
- ✅ Downloads Llama 3.1 model
- ✅ Creates Python virtual environment
- ✅ Installs all dependencies
- ✅ Sets up project structure

**Time:** ~10-15 minutes (depending on download speed)

---

### Option B: Manual Setup 🛠️

If you prefer to do it manually:

#### 1. Install Ollama

**Mac:**
```bash
brew install ollama
```

**Linux:**
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

**Windows:**
Download from [ollama.com/download](https://ollama.com/download)

#### 2. Download AI Models

```bash
ollama pull llama3.1          # Main reasoning model (~4.7GB)
ollama pull nomic-embed-text  # Embeddings for RAG (~274MB)
```

#### 3. Set Up Python Environment

```bash
# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate  # Mac/Linux
# OR
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt
```

#### 4. Configure Project

```bash
# Copy config template
cp config.yaml.example config.yaml

# Edit config.yaml if needed (defaults work fine)
```

---

## What's Next? Your 8-Week Journey

### Week 1: Data Foundation ✅
**Goal:** Generate synthetic datasets

**Tasks:**
1. Create data generation scripts
2. Generate 30 days of synthetic metrics (CSV)
3. Generate synthetic logs (JSON)
4. Create 5 incident scenarios with ground truth
5. Build data readers

**Notebook:** `01_data_generation.ipynb`

**Output:** ~100MB of realistic cloud monitoring data

---

### Week 2: Anomaly Detection Agent 🔍
**Goal:** Build first agent

**Tasks:**
1. Implement Z-score detection
2. Implement IQR method
3. Create baseline calculation
4. Build AnomalyDetectorAgent class
5. Test on synthetic incidents

**Notebook:** `03_anomaly_detection.ipynb`

**Target:** >80% detection accuracy

---

### Week 3: Root-Cause Analysis Agent 🧠
**Goal:** Log analysis and reasoning

**Tasks:**
1. Log parsing and filtering
2. Error pattern extraction
3. Metric-log correlation
4. LLM prompt design
5. Hypothesis generation

**Notebook:** `04_root_cause_analysis.ipynb`

**Target:** >85% correct root cause identification

---

### Week 4: Reporting Agent 📊
**Goal:** Generate professional reports

**Tasks:**
1. Markdown report templates
2. Visualization generation
3. Timeline creation
4. Recommendation engine
5. Sample reports

**Notebook:** Reports generated in `outputs/`

---

### Week 5: Multi-Agent Orchestration 🎭
**Goal:** Connect all agents

**Tasks:**
1. Choose framework (LangGraph recommended)
2. Build Orchestrator agent
3. Natural language query parsing
4. Agent routing logic
5. Context management

**Notebook:** `05_agent_orchestration.ipynb`

**Milestone:** End-to-end working system!

---

### Week 6: Knowledge Base (RAG) 📚
**Goal:** Add domain knowledge

**Tasks:**
1. Create knowledge documents
2. Set up ChromaDB
3. Generate embeddings
4. Implement retrieval
5. Integrate with RCA agent

**Enhancement:** More accurate diagnoses with historical patterns

---

### Week 7: Evaluation & Optimization 📈
**Goal:** Measure performance

**Tasks:**
1. Create test suite
2. Measure accuracy metrics
3. Compare to baseline
4. Optimize prompts
5. Add guardrails

**Notebook:** `06_evaluation.ipynb`

**Deliverable:** Performance report

---

### Week 8: Demo & Documentation 🎬
**Goal:** Polish for portfolio

**Tasks:**
1. Create comprehensive demo
2. Multiple example queries
3. Before/after comparison
4. Architecture documentation
5. Setup guide

**Notebook:** `07_demo.ipynb`

**Deliverable:** Portfolio-ready project!

---

## System Architecture (What You're Building)

```
                    ┌─────────────────────┐
                    │   User Query        │
                    │ "Why did latency    │
                    │  spike this AM?"    │
                    └──────────┬──────────┘
                               │
                    ┌──────────▼──────────┐
                    │  Orchestrator       │
                    │  - Parse query      │
                    │  - Route to agents  │
                    │  - Synthesize       │
                    └──┬────────┬────────┬┘
                       │        │        │
         ┌─────────────┘        │        └─────────────┐
         │                      │                      │
    ┌────▼─────┐         ┌─────▼──────┐        ┌─────▼─────┐
    │ Anomaly  │         │Root-Cause  │        │ Reporting │
    │ Detector │         │ Analyzer   │        │   Agent   │
    │          │         │            │        │           │
    │• Z-score │         │• Log parse │        │• Summary  │
    │• IQR     │         │• Correlate │        │• Charts   │
    │• Baseline│         │• LLM reason│        │• Actions  │
    └────┬─────┘         └─────┬──────┘        └─────┬─────┘
         │                     │                      │
         └─────────────┬───────┴──────────────────────┘
                       │
              ┌────────▼─────────┐
              │   Local Data     │
              │  • metrics/*.csv │
              │  • logs/*.json   │
              │  • incidents/    │
              └──────────────────┘
```

## Example Usage (Once Built)

```python
from src.agents.orchestrator import TroubleshootingOrchestrator

# Initialize system
assistant = TroubleshootingOrchestrator()

# Natural language queries
response = assistant.query("Why did latency spike this morning?")

print(response.summary)
print(response.root_cause)
print(response.recommendations)

# View generated report
response.generate_report(output_dir="./outputs/reports/")
```

## Learning Outcomes 🎓

By completing this project, you'll learn:

✅ **Multi-Agent Systems**
- Agent coordination patterns
- Task decomposition
- Inter-agent communication

✅ **AI/ML Techniques**
- Anomaly detection algorithms
- Time-series analysis
- LLM prompt engineering
- Retrieval-Augmented Generation (RAG)

✅ **Software Engineering**
- System architecture design
- Data pipeline creation
- API design
- Testing strategies

✅ **Domain Knowledge**
- Cloud troubleshooting
- Root-cause analysis
- Performance monitoring
- Incident management

## Resume Impact 💼

**Before:**
```
• Worked with Python and data analysis
```

**After:**
```
AWS Cloud Troubleshooting Assistant                    Aug 2025

• Built multi-agent AI system using LangGraph that automatically 
  analyzes cloud metrics to diagnose performance issues through 
  natural language queries

• Designed and orchestrated 3 specialized agents (anomaly detection, 
  root-cause analysis, reporting) achieving 85%+ diagnostic accuracy

• Reduced manual debugging time by 60% through statistical anomaly 
  detection and LLM-powered reasoning with RAG knowledge retrieval
```

## Cost Breakdown 💰

| Component | Cost |
|-----------|------|
| Ollama (Local LLM) | **$0** |
| Python + Libraries | **$0** |
| Data Storage (Local) | **$0** |
| Agent Frameworks | **$0** |
| ChromaDB | **$0** |
| **TOTAL** | **$0** ✅ |

**No credit card required. No API limits. Unlimited experimentation.**

## Common Questions ❓

### Q: Do I need a GPU?
**A:** No! Llama 3.1 (8B) runs fine on CPU. 8GB RAM minimum, 16GB recommended.

### Q: Can I use this offline?
**A:** Yes! Once models are downloaded, everything runs locally.

### Q: How long does this take?
**A:** 4-6 weeks part-time (10-15 hours/week). Can be done faster full-time.

### Q: Can I add AWS later?
**A:** Absolutely! Phase 9 covers AWS migration. Apply for AWS Educate for $100-300 credits.

### Q: What if I get stuck?
**A:** PROJECT_SPEC.md has detailed explanations for every component. Each phase includes specific deliverables and success criteria.

### Q: Is this suitable for beginners?
**A:** You should know Python basics and understand ML concepts. The spec walks through everything else.

## Support & Resources 📚

- **Full Spec:** `PROJECT_SPEC.md` (80 pages, everything you need)
- **LangGraph Docs:** [langchain-ai.github.io/langgraph](https://langchain-ai.github.io/langgraph/)
- **Ollama Docs:** [ollama.com/docs](https://ollama.com/docs)
- **AWS Educate:** [aws.amazon.com/education/awseducate](https://aws.amazon.com/education/awseducate)

## Project Status Tracking

Create a simple tracking system:

```markdown
# My Progress

## ✅ Completed
- [x] Setup environment
- [x] Read specification

## 🚧 In Progress
- [ ] Generate synthetic data

## 📅 Upcoming
- [ ] Build anomaly detector
- [ ] Build RCA agent
- [ ] Build reporter
- [ ] Orchestrate agents
- [ ] Add knowledge base
- [ ] Evaluate performance
- [ ] Create demo
```

## Ready to Start? 🚀

1. **Run setup script** (if you haven't)
   ```bash
   ./setup.sh  # or setup.bat on Windows
   ```

2. **Activate environment**
   ```bash
   source venv/bin/activate
   ```

3. **Start Jupyter**
   ```bash
   jupyter notebook
   ```

4. **Open first notebook**
   - Navigate to `notebooks/`
   - Create `01_data_generation.ipynb`
   - Start building!

5. **Read PROJECT_SPEC.md**
   - Section 11: Implementation Phases
   - Follow week-by-week guide

## Tips for Success 💡

1. **Start Small:** Get data generation working first before moving to agents
2. **Test Often:** Validate each component before integrating
3. **Document:** Add markdown cells in notebooks explaining your thinking
4. **Version Control:** Commit frequently with good messages
5. **Iterate:** First version doesn't need to be perfect
6. **Ask Questions:** LLMs can help debug and explain concepts
7. **Have Fun:** This is a learning project, experiment freely!

---

**You're all set!** 🎉

This is a challenging but rewarding project. Take it one phase at a time, and you'll have an impressive portfolio piece in 4-6 weeks.

Good luck! 🚀

---

*Need help? Check PROJECT_SPEC.md for detailed guidance on every component.*





