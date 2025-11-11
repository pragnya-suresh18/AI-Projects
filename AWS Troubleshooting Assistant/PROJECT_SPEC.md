# AWS Cloud Troubleshooting Assistant - Project Specification

## Executive Summary

An AI-powered troubleshooting system that uses multi-agent orchestration to automatically analyze cloud metrics and logs, detect anomalies, perform root-cause analysis, and generate actionable recommendations through natural language queries.

**Key Metrics:**
- 30% reduction in time-to-root-cause analysis
- 60% reduction in manual debugging steps
- Natural language query interface for non-technical stakeholders

---

##

**This project can be built completely free** using:
- ✅ **Local LLM** (Ollama with Llama 3) - No API costs
- ✅ **Local datasets** (CSV/JSON files) - No CloudWatch needed
- ✅ **Python frameworks** (LangGraph/CrewAI) - Free & open source
- ✅ **Local development** - Runs on your laptop
- ✅ **Total cost: $0** - Perfect for students!

**Learning Outcomes:**
- Multi-agent system design patterns
- Agent coordination and orchestration
- Anomaly detection algorithms
- Root-cause analysis techniques
- LLM prompt engineering
- Data-driven troubleshooting

**Time Investment:** 4-6 weeks part-time

---

## Two Implementation Paths

### Path 1: Free Student Version (Recommended) 🎓
- Local development with Ollama
- Static datasets (CSV/JSON)
- Python-based agent framework
- **Cost: $0**
- **Best for:** Learning multi-agent patterns

### Path 2: AWS Production Version ☁️
- AWS Bedrock Agents
- Live CloudWatch data
- Lambda functions
- **Cost: $50-70/month** (free with AWS student credits)
- **Best for:** Production deployment

**This spec covers both paths!** Follow the 🎓 icons for free student approach.

---

## Quick Start (Student Version) 🚀

### Prerequisites
- **Laptop:** 8GB+ RAM (16GB recommended for better performance)
- **Python:** 3.11 or higher
- **OS:** macOS, Linux, or Windows with WSL
- **Disk Space:** ~10GB for Ollama models + data

### 5-Minute Setup

```bash
# 1. Install Ollama (macOS/Linux)
curl -fsSL https://ollama.com/install.sh | sh

# For Windows: Download from https://ollama.com/download

# 2. Download Llama 3.1 model (~4.7GB)
ollama pull llama3.1

# 3. Clone/create project directory
mkdir aws-troubleshooting-assistant
cd aws-troubleshooting-assistant

# 4. Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 5. Install Python dependencies
pip install pandas numpy matplotlib seaborn jupyter
pip install langgraph langchain chromadb  # Agent framework
pip install ollama  # Ollama Python client

# 6. Start Jupyter
jupyter notebook
```

### First Steps
1. **Week 1:** Follow Phase 1 to generate synthetic data
2. **Week 2-4:** Build individual agents (anomaly, RCA, reporting)
3. **Week 5:** Connect agents with orchestrator
4. **Week 6-8:** Add knowledge base, evaluate, and demo

**Estimated time commitment:** 10-15 hours/week

---

## 1. Project Overview

### 1.1 Objectives
- Build a multi-agent system for automated cloud troubleshooting
- Enable natural language queries for incident investigation
- Automate anomaly detection and root-cause analysis
- Generate actionable reports with recommended fixes
- Demonstrate multi-agent coordination patterns with AWS Bedrock

### 1.2 Use Cases
1. **Real-time Incident Investigation**: "Why did latency spike this morning?"
2. **Performance Analysis**: "What caused the CPU usage to increase last night?"
3. **Error Pattern Detection**: "Show me all API errors related to the payment service"
4. **Proactive Monitoring**: "Are there any anomalies in the last 24 hours?"

---

## 2. System Architecture

### 2.1 High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     User Interface Layer                     │
│              (Natural Language Query Input)                  │
└────────────────────┬────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│                  Orchestrator Agent                          │
│            (AWS Bedrock Agent - Supervisor)                  │
│  - Query interpretation                                      │
│  - Agent coordination                                        │
│  - Response synthesis                                        │
└─────┬──────────────┬──────────────┬────────────────────────┘
      │              │               │
┌─────▼─────┐  ┌────▼─────┐  ┌─────▼──────┐
│ Anomaly   │  │Root-Cause│  │ Reporting  │
│ Detection │  │ Analysis │  │   Agent    │
│  Agent    │  │  Agent   │  │            │
└─────┬─────┘  └────┬─────┘  └─────┬──────┘
      │              │               │
┌─────▼──────────────▼───────────────▼──────────────────────┐
│              Data Access Layer (Local Files)               │
│  - Metrics (CSV files)                                     │
│  - Logs (JSON files)                                       │
│  - Incident Catalog (Ground truth labels)                  │
│  - Knowledge Base (Common Issues & Fixes)                  │
└────────────────────────────────────────────────────────────┘
```

### 2.2 Agent Hierarchy

#### **Orchestrator Agent (Supervisor)**
- **Role**: Coordinator and decision-maker
- **Responsibilities**:
  - Parse and understand natural language queries
  - Route tasks to appropriate sub-agents
  - Maintain conversation context
  - Synthesize findings into coherent responses
  - Handle validation and error recovery

#### **Anomaly Detection Agent**
- **Role**: Pattern recognition and deviation detection
- **Responsibilities**:
  - Analyze metrics for statistical anomalies
  - Identify unusual patterns in logs
  - Time-series analysis (spikes, drops, trends)
  - Correlate multiple metrics
  - Return anomaly scores and affected resources

#### **Root-Cause Analysis Agent**
- **Role**: Diagnostic investigator
- **Responsibilities**:
  - Deep-dive into identified anomalies
  - Trace request flows and dependencies
  - Correlate events across services
  - Compare against baseline behavior
  - Generate hypotheses for failures

#### **Reporting Agent**
- **Role**: Communication and recommendation engine
- **Responsibilities**:
  - Generate human-readable summaries
  - Provide actionable recommendations
  - Format findings with visualizations
  - Link to relevant documentation
  - Create incident timelines

---

## 3. Technical Stack

### 3.1 Infrastructure Options

#### **🎓 Student/Free Option (Recommended)**
| Component | Implementation | Cost |
|-----------|---------------|------|
| **Data Storage** | Local CSV/JSON/Parquet files | **$0** |
| **LLM** | Ollama (local) or OpenAI free credits | **$0** |
| **Agent Framework** | Python (LangChain/LangGraph or custom) | **$0** |
| **Knowledge Base** | Local JSON files or vector DB (Chroma) | **$0** |
| **Reports** | Local HTML/Markdown files | **$0** |
| **Notebooks** | Jupyter for development & demo | **$0** |

**Total Cost: $0** ✅

---

#### **Production AWS Option (Optional - requires credits)**
| Service | Purpose |
|---------|---------|
| **AWS Bedrock** | Multi-agent orchestration and LLM inference |
| **Amazon Bedrock Agents** | Agent framework and workflow management |
| **Amazon Bedrock Knowledge Bases** | Store troubleshooting documentation |
| **CloudWatch Logs** | Log data storage and retrieval |
| **CloudWatch Metrics** | Metric data storage |
| **Lambda** | Agent action groups and custom logic |
| **DynamoDB** | Store synthetic data and incident history |
| **S3** | Store generated reports and data snapshots |
| **IAM** | Security and permissions |

### 3.2 Models - Free/Student Options

#### **🎯 Option 1: AWS STACK (Recommended for Amazon Interview Prep)**

**Strands Agents + Amazon Bedrock:**
- **Framework**: [Strands Agents](https://strandsagents.com/) - AWS's official multi-agent framework
- **Primary Model**: Claude 3.5 Sonnet (via Amazon Bedrock)
  - Best reasoning for root-cause analysis
  - Native integration with AWS services
- **Alternative Models**: 
  - Claude 3 Haiku (faster, cheaper for simple queries)
  - Anthropic Claude 3 Opus (most capable, use sparingly)
- **Embeddings**: Amazon Titan Embeddings (for knowledge base)

**Cost**: ~$20-40 for the full project
- First month often covered by free tier
- Apply for [AWS Educate](https://aws.amazon.com/education/awseducate/) for $100-300 credits

**Pros:**
- ✅ **Perfect for Amazon interviews** - Shows you know their tech
- ✅ Production-grade framework designed by AWS
- ✅ Native AWS integrations (CloudWatch, Lambda, etc.)
- ✅ Best model quality (Claude 3.5 Sonnet)
- ✅ Resume impact: "Built with AWS Strands Agents and Bedrock"

**Why This Matters for Amazon:**
- Shows initiative learning AWS-native tools
- Demonstrates understanding of production patterns
- Uses technologies Amazon engineers actually use
- Direct talking point: "I chose Strands Agents because..."

---

#### **Option 2: LOCAL (Free Fallback for Testing)**

**Ollama + Strands Agents:**
- **Framework**: Still use Strands Agents (supports Ollama!)
- **Model**: Llama 3.1 (8B) via Ollama
- **Installation**: `curl -fsSL https://ollama.com/install.sh | sh`
- **Cost**: $0

**Pros:**
- ✅ Completely free for development
- ✅ Still learn Strands Agents architecture
- ✅ Easy to switch to Bedrock later

**Use case**: 
- Prototype locally with Ollama
- Deploy to Bedrock for final version
- Best of both worlds!

---

#### **Option 3: OpenAI (Alternative)**

- **GPT-4o-mini**: Good for testing
- **Cost**: ~$5 with free credits
- **Note**: Less impressive for Amazon interviews than AWS stack

### 3.3 Development Tools (All Free!)

**Core Stack:**
- **Python 3.11+**: Primary programming language
- **Pandas**: Data manipulation and analysis
- **NumPy**: Statistical computations
- **Jupyter Notebook**: Development and interactive demo
- **Matplotlib/Seaborn**: Data visualization

**Multi-Agent Frameworks:**
- **Option 1: Strands Agents** (🎯 Recommended for Amazon)
  - **AWS's official multi-agent framework**
  - Production-ready, enterprise-grade
  - Native Bedrock integration
  - Built-in support for Agent-to-Agent (A2A), Swarms, Graph workflows
  - Excellent for AWS deployment (Lambda, EKS, EC2)
  - `pip install strands-agents`
  - [Documentation](https://strandsagents.com/)
  
- **Option 2: LangGraph** (Alternative)
  - Built for multi-agent workflows
  - Works with any LLM
  - `pip install langgraph langchain`
  - Good for learning, but less impressive for Amazon interviews
  
- **Option 3: Custom Python**
  - Build from scratch to deeply understand patterns
  - Educational but not recommended for interviews

**Vector Database (for Knowledge Base):**
- **ChromaDB**: Free, local, easy to use
- **Alternative**: FAISS (Meta)

**Testing & Development:**
- **Pytest**: Unit testing
- **Git**: Version control

---

## 4. Data Requirements

### 4.1 Synthetic Dataset Generation (Local Files)

**Output Format:** CSV/JSON files stored locally (no AWS needed!)

**File Structure:**
```
data/
├── metrics/
│   ├── api_latency.csv          # Time-series metrics
│   ├── cpu_utilization.csv
│   ├── memory_utilization.csv
│   ├── error_rates.csv
│   └── request_rates.csv
│
├── logs/
│   ├── application_logs.json     # Structured logs
│   ├── access_logs.json
│   └── system_logs.json
│
└── incidents/
    ├── incident_catalog.json     # Ground truth labels
    └── incident_timeline.json
```

#### **Metrics to Generate**
1. **Application Metrics**
   - API Latency (p50, p90, p99)
   - Request Rate (requests/sec)
   - Error Rate (%)
   - Response Codes (2xx, 4xx, 5xx)

2. **Infrastructure Metrics**
   - CPU Utilization (%)
   - Memory Utilization (%)
   - Network I/O (bytes/sec)
   - Disk I/O (ops/sec)

3. **Database Metrics**
   - Query Duration (ms)
   - Connection Pool Usage
   - Lock Wait Time
   - Deadlocks

#### **Log Types to Generate**
1. **Application Logs**
   - INFO: Normal operations
   - WARN: Degraded performance
   - ERROR: Failures and exceptions
   - Structured JSON format

2. **Access Logs**
   - HTTP requests/responses
   - Client IPs and user agents
   - Request paths and methods

3. **System Logs**
   - Service start/stop events
   - Configuration changes
   - Health check results

#### **Incident Scenarios**
1. **Latency Spike** (Duration: 30-45 min)
   - Trigger: Database slow query
   - Impact: P99 latency increases 5x
   - Additional signals: Connection pool exhaustion

2. **Error Rate Increase** (Duration: 15-20 min)
   - Trigger: Downstream service failure
   - Impact: 5xx errors increase to 15%
   - Additional signals: Timeout errors in logs

3. **CPU Saturation** (Duration: 1-2 hours)
   - Trigger: Memory leak or infinite loop
   - Impact: CPU sustained at 90%+
   - Additional signals: Slow response times

4. **Dependency Failure** (Duration: 10-15 min)
   - Trigger: External API unavailable
   - Impact: Cascading failures
   - Additional signals: Circuit breaker trips

5. **Normal Operations** (Baseline)
   - Healthy metrics
   - Expected variations
   - Background noise

### 4.2 Data Volume & Format

**Dataset Size:**
- **Time Range**: 30 days of historical data
- **Metrics Granularity**: 1-minute intervals (~43,200 data points per metric)
- **Log Volume**: ~10,000 log entries per day (~300K total)
- **Incidents**: 15-20 synthetic incidents with ground truth labels
- **Total Size**: ~50-100 MB (easily fits in GitHub, no cloud needed!)

**CSV Format (Metrics):**
```csv
timestamp,service,metric_name,value,unit
2024-10-06T00:00:00Z,api-service,latency_p99,145.2,ms
2024-10-06T00:01:00Z,api-service,latency_p99,142.8,ms
```

**JSON Format (Logs):**
```json
{
  "timestamp": "2024-10-06T08:15:23Z",
  "level": "ERROR",
  "service": "api-service",
  "message": "Database connection timeout",
  "trace_id": "abc-123",
  "metadata": {
    "endpoint": "/api/payments",
    "duration_ms": 5000
  }
}
```

**🎯 This approach:**
- ✅ Works completely offline
- ✅ Easy to version control (Git)
- ✅ Fast to load and process
- ✅ Shareable (can publish on GitHub)
- ✅ No AWS account required!

---

## 5. Agent Workflows

### 5.1 Query Processing Flow

```
User Query → Orchestrator Agent
    ↓
Parse Intent & Entities
(time range, service, metric type)
    ↓
Determine Required Sub-Agents
    ↓
Parallel Execution:
  ├→ Anomaly Detection Agent
  │   ├→ Fetch relevant metrics
  │   ├→ Statistical analysis
  │   └→ Return anomalies + scores
  │
  ├→ Root-Cause Analysis Agent
  │   ├→ Fetch correlated logs
  │   ├→ Analyze event sequences
  │   └→ Generate hypotheses
  │
  └→ Reporting Agent
      ├→ Synthesize findings
      ├→ Format recommendations
      └→ Generate visualizations
    ↓
Orchestrator Validates & Merges Results
    ↓
Return Coherent Response to User
```

### 5.2 Anomaly Detection Workflow

1. **Retrieve Metrics**: Fetch time-series data for requested period
2. **Baseline Calculation**: Calculate moving averages and standard deviations
3. **Anomaly Detection**: Apply statistical methods
   - Z-score analysis (threshold: ±3σ)
   - IQR method for outliers
   - Time-series decomposition (trend, seasonality, residuals)
4. **Correlation Analysis**: Identify concurrent anomalies across metrics
5. **Severity Scoring**: Assign severity (Low/Medium/High/Critical)
6. **Return Results**: JSON with anomalies, timestamps, affected resources

### 5.3 Root-Cause Analysis Workflow

1. **Context Gathering**: Collect all data around anomaly timeframe (±15 min)
2. **Log Analysis**: 
   - Extract error messages
   - Identify patterns (regex, frequency analysis)
   - Trace request IDs across services
3. **Dependency Mapping**: Check upstream/downstream services
4. **Hypothesis Generation**: Apply reasoning based on:
   - Error patterns
   - Metric correlations
   - Known issue patterns (from knowledge base)
5. **Confidence Scoring**: Rank hypotheses by evidence strength
6. **Return Results**: Ordered list of likely root causes with evidence

### 5.4 Reporting Workflow

1. **Aggregate Findings**: Collect outputs from other agents
2. **Structure Report**:
   - Executive Summary (2-3 sentences)
   - Incident Timeline
   - Affected Components
   - Root Cause (most likely)
   - Impact Assessment
   - Recommended Actions
   - Related Incidents
3. **Generate Visualizations**: 
   - Metric plots with anomaly markers
   - Heatmaps for correlations
   - Timeline charts
4. **Add Context**: Link to documentation, runbooks, similar incidents
5. **Format Output**: Markdown report with embedded charts

---

## 6. Agent Implementation Details

### 6.1 Orchestrator Agent

**Bedrock Agent Configuration:**
```yaml
agent_name: cloud-troubleshooting-orchestrator
model_id: anthropic.claude-3-5-sonnet-20241022-v2:0
instruction: |
  You are an expert cloud operations agent that helps diagnose and troubleshoot
  AWS infrastructure issues. You coordinate sub-agents to analyze CloudWatch
  data, detect anomalies, and provide actionable recommendations.
  
  When receiving a query:
  1. Parse the time range, affected services, and symptoms
  2. Determine which sub-agents to invoke
  3. Synthesize their findings into a clear, actionable response
  4. Maintain conversation context for follow-up questions
  
action_groups:
  - name: anomaly_detection
    description: Detect statistical anomalies in metrics
    lambda_arn: arn:aws:lambda:...
    
  - name: root_cause_analysis
    description: Analyze logs and determine root causes
    lambda_arn: arn:aws:lambda:...
    
  - name: generate_report
    description: Create formatted incident reports
    lambda_arn: arn:aws:lambda:...
```

**Prompt Template:**
```
You have access to the following sub-agents:
- anomaly_detection: Analyzes metrics for unusual patterns
- root_cause_analysis: Investigates logs and events
- generate_report: Creates structured reports

User Query: {user_query}

Think step by step:
1. What time range is relevant?
2. Which services/resources are mentioned?
3. What type of issue is this (latency, errors, resource usage)?
4. Which sub-agents should be invoked?
5. In what order should they execute?

Proceed with your analysis.
```

### 6.2 Anomaly Detection Agent

**Implementation:**
```python
class AnomalyDetectionAgent:
    def __init__(self, bedrock_client, data_source):
        self.bedrock = bedrock_client
        self.data_source = data_source
    
    def detect_anomalies(self, metrics, time_range, threshold=3.0):
        """
        Detect anomalies using statistical methods
        
        Args:
            metrics: List of metric names
            time_range: (start_time, end_time)
            threshold: Z-score threshold
        
        Returns:
            List of detected anomalies with metadata
        """
        pass
    
    def calculate_baseline(self, metric_data):
        """Calculate rolling mean and std deviation"""
        pass
    
    def zscore_detection(self, values, baseline):
        """Apply z-score anomaly detection"""
        pass
    
    def correlate_anomalies(self, anomaly_list):
        """Find correlated anomalies across metrics"""
        pass
```

**Action Group Schema:**
```json
{
  "name": "detect_anomalies",
  "description": "Detect statistical anomalies in CloudWatch metrics",
  "parameters": {
    "metrics": {
      "type": "array",
      "items": {"type": "string"},
      "description": "List of metric names to analyze",
      "required": true
    },
    "start_time": {
      "type": "string",
      "description": "Start time in ISO format",
      "required": true
    },
    "end_time": {
      "type": "string",
      "description": "End time in ISO format",
      "required": true
    },
    "sensitivity": {
      "type": "string",
      "enum": ["low", "medium", "high"],
      "description": "Detection sensitivity",
      "required": false
    }
  }
}
```

### 6.3 Root-Cause Analysis Agent

**Implementation:**
```python
class RootCauseAnalysisAgent:
    def __init__(self, bedrock_client, log_source):
        self.bedrock = bedrock_client
        self.log_source = log_source
    
    def analyze(self, anomalies, time_range):
        """
        Perform root cause analysis
        
        Args:
            anomalies: List of detected anomalies
            time_range: Time window to analyze
        
        Returns:
            Ranked list of likely root causes
        """
        pass
    
    def extract_error_patterns(self, logs):
        """Find common error patterns in logs"""
        pass
    
    def trace_dependencies(self, service_name, timestamp):
        """Map service dependencies and failures"""
        pass
    
    def generate_hypotheses(self, anomalies, logs, dependencies):
        """Generate and rank root cause hypotheses"""
        pass
```

**Prompt for LLM Reasoning:**
```
You are analyzing a cloud infrastructure incident. Your goal is to identify
the most likely root cause.

Given Data:
- Anomalies: {anomalies}
- Error Logs: {error_logs}
- Service Dependencies: {dependencies}
- Normal Baseline: {baseline}

Common Cloud Issues:
1. Resource exhaustion (CPU, memory, connections)
2. Dependency failures (downstream services)
3. Configuration changes
4. Database performance degradation
5. Network issues
6. Rate limiting / throttling

Analyze the evidence and:
1. List possible root causes
2. Rank them by likelihood (provide confidence %)
3. Explain the supporting evidence for each
4. Identify any contradictory evidence

Format as JSON:
{
  "hypotheses": [
    {
      "root_cause": "...",
      "confidence": 0.85,
      "evidence": ["...", "..."],
      "contradictions": ["..."]
    }
  ]
}
```

### 6.4 Reporting Agent

**Implementation:**
```python
class ReportingAgent:
    def __init__(self, bedrock_client):
        self.bedrock = bedrock_client
    
    def generate_report(self, anomalies, root_causes, metadata):
        """
        Generate formatted incident report
        
        Args:
            anomalies: Detected anomalies
            root_causes: RCA findings
            metadata: Additional context
        
        Returns:
            Formatted markdown report
        """
        pass
    
    def create_timeline(self, events):
        """Generate incident timeline"""
        pass
    
    def recommend_actions(self, root_cause):
        """Provide actionable recommendations"""
        pass
    
    def generate_visualizations(self, metrics):
        """Create charts and graphs"""
        pass
```

**Report Template:**
```markdown
# Incident Report: {incident_id}

## Executive Summary
{2-3 sentence summary of the incident}

**Status:** {Resolved/Ongoing}  
**Severity:** {Low/Medium/High/Critical}  
**Duration:** {start_time} to {end_time} ({duration})  
**Affected Services:** {service_list}

---

## Timeline
| Time | Event |
|------|-------|
| HH:MM | {event description} |

---

## Root Cause Analysis
**Most Likely Cause:** {root_cause}  
**Confidence:** {confidence_score}%

**Evidence:**
- {evidence_point_1}
- {evidence_point_2}

**Affected Components:**
- {component_1}: {impact}
- {component_2}: {impact}

---

## Impact Assessment
- **User Impact:** {description}
- **Requests Affected:** {count}
- **Error Rate:** {percentage}
- **Performance Degradation:** {details}

---

## Recommended Actions

### Immediate Actions
1. {action_1}
2. {action_2}

### Long-term Prevention
1. {prevention_1}
2. {prevention_2}

---

## Related Resources
- [Runbook: {title}]({link})
- [Similar Incident: {id}]({link})

---

## Visualizations
{embedded charts}
```

---

## 7. Knowledge Base

### 7.1 Structure
Store common troubleshooting patterns and solutions in Bedrock Knowledge Base:

**Categories:**
1. **High Latency Issues**
   - Database slow queries
   - Network congestion
   - Resource contention
   - Cold starts

2. **Error Patterns**
   - 5xx errors → service failures
   - 4xx errors → client issues
   - Timeout errors → dependency issues
   - Connection errors → network/DNS

3. **Resource Issues**
   - Memory leaks → gradual degradation
   - CPU spikes → expensive operations
   - Disk full → log accumulation

4. **Dependency Failures**
   - Circuit breaker patterns
   - Cascading failures
   - Retry storms

### 7.2 Document Format
```json
{
  "issue_id": "LAT-001",
  "title": "Database Slow Query Causing Latency Spike",
  "symptoms": [
    "p99 latency increased by 5x or more",
    "database connection pool exhaustion",
    "timeout errors in application logs"
  ],
  "root_causes": [
    "Missing database index",
    "Table lock contention",
    "Large table scan"
  ],
  "diagnostic_steps": [
    "Check database slow query log",
    "Review query execution plans",
    "Check index usage statistics"
  ],
  "remediation": [
    "Add appropriate indexes",
    "Optimize query",
    "Implement query caching"
  ],
  "prevention": [
    "Regular query performance monitoring",
    "Database query review process",
    "Automated index recommendations"
  ]
}
```

---

## 8. API Design

### 8.1 Query Interface

**Endpoint:** POST `/query`

**Request:**
```json
{
  "query": "Why did latency spike this morning?",
  "context": {
    "services": ["api-service", "database"],
    "time_hint": "2024-11-05T08:00:00Z"
  },
  "options": {
    "include_visualizations": true,
    "detail_level": "detailed"
  }
}
```

**Response:**
```json
{
  "query_id": "q-123456",
  "status": "complete",
  "summary": "Latency spike detected at 08:15 UTC caused by...",
  "findings": {
    "anomalies": [...],
    "root_cause": {...},
    "recommendations": [...]
  },
  "report_url": "s3://...",
  "visualizations": [...],
  "confidence": 0.89,
  "processing_time_ms": 3500
}
```

### 8.2 Follow-up Queries

The system maintains conversation context:
```
User: "Why did latency spike this morning?"
Agent: [Analyzes and responds]

User: "What about yesterday?"
Agent: [Understands context and compares]

User: "Show me the database metrics during that time"
Agent: [Provides specific details]
```

---

## 9. Validation and Guardrails

### 9.1 Input Validation
- **Time Range Limits**: Max 90 days lookback
- **Query Complexity**: Limit to 3 concurrent sub-agent invocations
- **Rate Limiting**: Max 10 queries per minute per user

### 9.2 Agent Guardrails
- **Context Window Management**: Limit context to 100K tokens
- **Timeout Handling**: 30s per sub-agent, 60s total
- **Fallback Mechanisms**: Graceful degradation if sub-agent fails
- **Confidence Thresholds**: Flag low-confidence responses (<0.6)

### 9.3 Response Validation
- **Factual Grounding**: All claims must reference data
- **Consistency Checks**: Cross-validate findings across agents
- **Hallucination Prevention**: Reject responses without data support

### 9.4 Error Recovery
```python
class OrchestratorValidation:
    def validate_response(self, response):
        """Validate agent response quality"""
        checks = [
            self.has_data_references(response),
            self.confidence_above_threshold(response),
            self.no_contradictions(response),
            self.actionable_recommendations(response)
        ]
        return all(checks)
    
    def fallback_strategy(self, failed_agent):
        """Handle agent failures gracefully"""
        if failed_agent == "anomaly_detection":
            return self.rule_based_anomaly_detection()
        elif failed_agent == "root_cause":
            return self.simplified_log_analysis()
        else:
            return self.generic_report()
```

---

## 10. Evaluation and Testing

### 10.1 Test Scenarios

| Scenario | Expected Behavior | Success Criteria |
|----------|------------------|------------------|
| Latency spike query | Identify database slow query | Correct root cause with >80% confidence |
| Error rate increase | Trace to downstream service | Identify dependency failure |
| Ambiguous query | Ask clarifying questions | No incorrect assumptions |
| Normal operations | Report no issues found | No false positives |
| Multiple concurrent issues | Prioritize by severity | All issues identified |

### 10.2 Performance Metrics

**Accuracy Metrics:**
- Root cause correctness: >85%
- False positive rate: <10%
- False negative rate: <5%

**Performance Metrics:**
- Query response time: <10s (p95)
- Agent orchestration overhead: <2s
- Data retrieval time: <5s

**User Experience:**
- Query understanding accuracy: >90%
- Follow-up context retention: >95%
- Actionable recommendation rate: >80%

### 10.3 Baseline Comparison

**Manual Process:**
1. Check CloudWatch dashboard (2-3 min)
2. Query logs (5-10 min)
3. Correlate metrics manually (10-15 min)
4. Research similar issues (5-10 min)
5. Document findings (5-10 min)

**Total:** 27-48 minutes

**AI System:**
1. Natural language query (30 sec)
2. Automated analysis (5-8 sec)
3. Report generation (2-3 sec)

**Total:** ~10 seconds (60-95% reduction)

---

## 11. Implementation Phases


### **Phase 1: Setup & Data Generation (Week 1)**

**Goal:** Set up environment and generate synthetic datasets

- [ ] Install Ollama and download Llama 3.1 model
- [ ] Set up Python virtual environment
- [ ] Install dependencies (pandas, numpy, matplotlib, langgraph/crewai)
- [ ] Create project structure
- [ ] **Generate synthetic metrics** (CSV files)
  - API latency, CPU, memory, error rates
  - 30 days of time-series data
- [ ] **Generate synthetic logs** (JSON files)
  - Application logs, access logs, system logs
- [ ] **Create incident scenarios** (5 types with ground truth)
- [ ] Build data readers (metrics_reader.py, logs_reader.py)

**Deliverable:** Working datasets in `data/raw/` folder

---

### **Phase 2: Anomaly Detection Agent (Week 2)**

**Goal:** Build the first agent that detects statistical anomalies

- [ ] Implement statistical analysis utilities
  - Z-score detection
  - IQR (Interquartile Range) method
  - Moving average/baseline calculation
- [ ] Create `AnomalyDetectorAgent` class
- [ ] Integrate with Ollama for interpretation
- [ ] Test on synthetic incidents
- [ ] Create evaluation metrics (precision, recall, F1)
- [ ] **Notebook:** `03_anomaly_detection.ipynb`

**Deliverable:** Agent that identifies anomalies with >80% accuracy

---

### **Phase 3: Root-Cause Analysis Agent (Week 3)**

**Goal:** Build agent that analyzes logs and determines root causes

- [ ] Implement log parsing and filtering
- [ ] Create error pattern extraction
- [ ] Build correlation analysis (metrics + logs)
- [ ] Create `RootCauseAnalyzerAgent` class
- [ ] Design prompts for LLM reasoning
- [ ] Test hypothesis generation
- [ ] Validate against ground truth labels
- [ ] **Notebook:** `04_root_cause_analysis.ipynb`

**Deliverable:** Agent that correctly identifies root cause >85% of time

---

### **Phase 4: Reporting Agent (Week 4)**

**Goal:** Build agent that generates human-readable reports

- [ ] Create report templates (markdown)
- [ ] Implement visualization generator
  - Time-series plots with anomaly markers
  - Correlation heatmaps
  - Timeline charts
- [ ] Create `ReporterAgent` class
- [ ] Integrate with LLM for summary generation
- [ ] Generate sample reports for each incident type
- [ ] Format recommendations

**Deliverable:** Professional incident reports with visualizations

---

### **Phase 5: Multi-Agent Orchestration (Week 5)**

**Goal:** Connect all agents and enable coordination

- [ ] Choose framework: LangGraph vs CrewAI vs Custom
- [ ] Implement `OrchestratorAgent`
- [ ] Design agent communication protocol
- [ ] Parse natural language queries
- [ ] Route queries to appropriate sub-agents
- [ ] Implement context management
- [ ] Add error handling and fallbacks
- [ ] **Notebook:** `05_agent_orchestration.ipynb`

**Deliverable:** End-to-end query → response workflow

---

### **Phase 6: Knowledge Base & RAG (Week 6)**

**Goal:** Add knowledge base for common issues

- [ ] Create knowledge base documents (JSON)
  - Latency issues
  - Error patterns
  - Resource issues
  - Dependency failures
- [ ] Set up ChromaDB for vector storage
- [ ] Generate embeddings (use Ollama embeddings)
- [ ] Implement retrieval system
- [ ] Integrate with RCA agent
- [ ] Test knowledge retrieval accuracy

**Deliverable:** Knowledge-augmented root cause analysis

---

### **Phase 7: Evaluation & Optimization (Week 7)**

**Goal:** Measure performance and optimize

- [ ] Create test suite with all incident scenarios
- [ ] Measure accuracy metrics
  - Root cause correctness
  - False positive/negative rates
  - Response times
- [ ] Compare against manual baseline
- [ ] Optimize prompts for better responses
- [ ] Add validation and guardrails
- [ ] **Notebook:** `06_evaluation.ipynb`

**Deliverable:** Performance report with metrics

---

### **Phase 8: Demo & Documentation (Week 8)**

**Goal:** Polish and prepare for presentation

- [ ] Create comprehensive demo notebook
- [ ] Add multiple example queries
- [ ] Generate before/after comparison
- [ ] Document architecture decisions
- [ ] Write setup guide for others
- [ ] Record demo video (optional)
- [ ] Create README with project highlights
- [ ] **Notebook:** `07_demo.ipynb`

**Deliverable:** Portfolio-ready project with full documentation

---

### ☁️ Optional Phase 9: AWS Migration (If you get credits)

- [ ] Set up AWS account and Bedrock access
- [ ] Migrate to Bedrock Agents
- [ ] Upload data to CloudWatch
- [ ] Create Lambda functions
- [ ] Deploy infrastructure
- [ ] Compare performance: local vs cloud

---

## 12. Cost Estimation

### 12.1 🎯 AWS Implementation (Recommended for Amazon Interviews)

**Using Strands Agents + Amazon Bedrock:**

| Service | Usage | Cost | Free Tier |
|---------|-------|------|-----------|
| **Amazon Bedrock** | Claude 3.5 Sonnet (~500K tokens) | $15-25 | Some free tier |
| **Amazon Bedrock** | Claude 3 Haiku (for simple queries) | $3-5 | Available |
| **CloudWatch Logs** | 5GB ingestion (synthetic data) | $0-5 | 5GB free |
| **CloudWatch Metrics** | 10 custom metrics | $0 | 10 free |
| **S3** | Storage + requests | $0-2 | 5GB free |
| **Lambda** | Development testing | $0 | 1M requests free |
| **Strands Agents** | Open source framework | $0 | Free |
| **Total** | | **$18-37/month** | |

**With AWS Student Credits ($100-300):**
- ✅ **Entire project covered** for free
- ✅ Apply at: [aws.amazon.com/education/awseducate](https://aws.amazon.com/education/awseducate)
- ✅ Lasts 3-6 months for this project

---

### 12.2 💡 Cost Optimization Strategies

**Development Phase (Keep it cheap):**
1. **Use Claude 3 Haiku** for development ($1/M tokens vs $15/M)
2. **Local data files** first, upload to CloudWatch later
3. **Limit synthetic data** to 7 days instead of 30
4. **Cache LLM responses** to avoid repeated calls
5. **Use Ollama locally** for testing, Bedrock for demo

**Estimated cost with optimization: $10-15 total for entire project**

---

### 12.3 🎓 Free Alternative (If No AWS Credits)

**Hybrid Approach - Best of Both Worlds:**

| Component | Development | Final Demo |
|-----------|------------|------------|
| **Framework** | Strands Agents | Strands Agents |
| **LLM** | Ollama (local) | Bedrock Claude |
| **Data** | Local CSV/JSON | Upload to CloudWatch |
| **Cost** | $0 | $10-20 for demo |

**Why This Works:**
1. ✅ Learn Strands Agents architecture (free)
2. ✅ Develop entire system locally ($0)
3. ✅ Deploy to Bedrock only for final demo
4. ✅ Resume still says "AWS Strands Agents + Bedrock"
5. ✅ Interview talking point: "Cost-optimized development"

---

### 12.4 🎯 For Amazon Interviews: Worth the Investment

**Value Proposition:**
- Investment: $10-40 (or $0 with credits)
- ROI: Amazon SDE salary ($150K+)
- Differentiator: "Built with AWS tech" > "Built with open source"
- Talking point: Shows you invested in learning AWS

**My Recommendation:** 
Apply for AWS Educate first. If approved, full AWS stack. If not, use hybrid approach (develop locally, deploy to Bedrock for demo).

---

## 13. Security and Compliance

### 13.1 IAM Policies
- Least privilege access for Lambda functions
- Bedrock agent roles with minimal permissions
- CloudWatch read-only access
- S3 bucket policies for reports

### 13.2 Data Privacy
- No PII in logs (synthetic data)
- Encryption at rest (S3, DynamoDB)
- Encryption in transit (HTTPS)
- Log retention policies (30 days)

### 13.3 Audit Trail
- Log all queries and responses
- Track agent invocations
- Monitor API usage
- Alert on anomalous patterns

---

## 14. Success Criteria

### 14.1 Technical Success
- ✅ System responds to queries in <10s
- ✅ Root cause accuracy >85%
- ✅ False positive rate <10%
- ✅ All sub-agents communicate successfully
- ✅ Guardrails prevent hallucinations

### 14.2 Business Success
- ✅ 30%+ reduction in time-to-root-cause
- ✅ 60%+ reduction in manual debugging
- ✅ Actionable recommendations in >80% of cases
- ✅ System handles 100+ queries/day
- ✅ User satisfaction >4/5

### 14.3 Demonstration Success
- ✅ Live demo with 5+ query types
- ✅ Clear visualization of multi-agent coordination
- ✅ Before/after comparison showing time savings
- ✅ Example reports generated
- ✅ Documentation complete

---

## 15. Future Enhancements

### 15.1 Phase 2 Features
- Real-time streaming analysis
- Predictive anomaly detection (ML models)
- Auto-remediation actions
- Integration with ticketing systems (Jira, ServiceNow)
- Slack/Teams bot interface

### 15.2 Advanced Capabilities
- Multi-cloud support (Azure, GCP)
- Custom metric definitions
- Collaborative troubleshooting (multi-user)
- Historical trend analysis
- Cost impact assessment

---

## 16. References and Resources

### 16.1 AWS Documentation
- [AWS Bedrock Agents](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html)
- [CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html)
- [Lambda Function URLs](https://docs.aws.amazon.com/lambda/latest/dg/lambda-urls.html)

### 16.2 Technical Papers
- Multi-agent systems design patterns
- Anomaly detection algorithms (Z-score, IQR, Isolation Forest)
- Root cause analysis methodologies

### 16.3 Tools and Libraries
- Boto3 (AWS SDK)
- Pandas (data manipulation)
- Matplotlib/Seaborn (visualization)
- NumPy (statistical analysis)

---

## Appendix A: File Structure

### 🎓 Student/Free Version (Local Development)

```
aws-troubleshooting-assistant/
├── README.md
├── PROJECT_SPEC.md
├── requirements.txt
├── .env.example                     # Config for Ollama/API keys
│
├── data/                            # All data stored locally
│   ├── raw/                         # Generated synthetic data
│   │   ├── metrics/
│   │   │   ├── api_latency.csv
│   │   │   ├── cpu_utilization.csv
│   │   │   ├── memory_utilization.csv
│   │   │   ├── error_rates.csv
│   │   │   └── request_rates.csv
│   │   │
│   │   ├── logs/
│   │   │   ├── application_logs.json
│   │   │   ├── access_logs.json
│   │   │   └── system_logs.json
│   │   │
│   │   └── incidents/
│   │       ├── incident_catalog.json      # Ground truth
│   │       └── incident_timeline.json
│   │
│   └── processed/                   # Cleaned/transformed data
│       └── ...
│
├── src/
│   ├── data_generation/             # Generate synthetic datasets
│   │   ├── generate_metrics.py
│   │   ├── generate_logs.py
│   │   ├── incident_scenarios.py
│   │   └── config.py
│   │
│   ├── agents/                      # Multi-agent system
│   │   ├── __init__.py
│   │   ├── orchestrator.py          # Main coordinator
│   │   ├── anomaly_detector.py      # Anomaly detection agent
│   │   ├── root_cause_analyzer.py   # RCA agent
│   │   ├── reporter.py              # Reporting agent
│   │   └── base_agent.py            # Abstract base class
│   │
│   ├── data_access/                 # Local file readers
│   │   ├── __init__.py
│   │   ├── metrics_reader.py        # Read CSV metrics
│   │   ├── logs_reader.py           # Read JSON logs
│   │   └── incident_reader.py       # Read ground truth
│   │
│   ├── llm/                         # LLM abstraction layer
│   │   ├── __init__.py
│   │   ├── ollama_client.py         # Ollama integration
│   │   ├── openai_client.py         # OpenAI integration (optional)
│   │   └── base_llm.py              # Abstract LLM interface
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── statistical_analysis.py  # Anomaly detection algorithms
│   │   ├── visualization.py         # Plotting functions
│   │   ├── validation.py            # Response validation
│   │   └── prompts.py               # LLM prompt templates
│   │
│   ├── knowledge_base/              # RAG system
│   │   ├── __init__.py
│   │   ├── vector_store.py          # ChromaDB integration
│   │   └── retriever.py             # Query knowledge base
│   │
│   └── config/
│       ├── agent_config.yaml        # Agent settings
│       └── data_config.yaml         # Data paths
│
├── knowledge_base/                  # Troubleshooting knowledge
│   ├── common_issues/
│   │   ├── latency_issues.json
│   │   ├── error_patterns.json
│   │   ├── resource_issues.json
│   │   └── dependency_failures.json
│   │
│   └── embeddings/                  # Vector embeddings (generated)
│       └── chroma_db/
│
├── notebooks/                       # Jupyter notebooks for development
│   ├── 01_data_generation.ipynb
│   ├── 02_exploratory_analysis.ipynb
│   ├── 03_anomaly_detection.ipynb
│   ├── 04_root_cause_analysis.ipynb
│   ├── 05_agent_orchestration.ipynb
│   ├── 06_evaluation.ipynb
│   └── 07_demo.ipynb               # Final demo notebook
│
├── outputs/                         # Generated reports
│   ├── reports/
│   │   └── incident_*.md
│   └── visualizations/
│       └── *.png
│
├── tests/                           # Unit tests
│   ├── __init__.py
│   ├── test_data_generation.py
│   ├── test_anomaly_detector.py
│   ├── test_root_cause_analyzer.py
│   ├── test_orchestrator.py
│   └── test_llm_clients.py
│
├── docs/
│   ├── setup_guide.md               # Installation instructions
│   ├── architecture.md              # System design
│   ├── agent_design.md              # Agent patterns
│   └── evaluation_results.md       # Performance metrics
│
└── scripts/                         # Utility scripts
    ├── install_ollama.sh
    ├── setup_environment.sh
    └── run_evaluation.py
```

### ☁️ AWS Version (Optional - requires credits)

Add these folders when migrating to AWS:
```
├── infrastructure/
│   ├── cloudformation/
│   │   ├── main.yaml
│   │   └── agents.yaml
│   └── terraform/
│       └── main.tf
│
└── lambda_functions/
    ├── anomaly_detection/
    ├── root_cause_analysis/
    └── generate_report/
```

---

## Appendix B: Sample Queries

```python
sample_queries = [
    # Latency issues
    "Why did latency spike this morning?",
    "What caused the p99 response time to increase at 3 AM?",
    "Show me any latency anomalies in the last 24 hours",
    
    # Error patterns
    "Why are we seeing 5xx errors on the payment API?",
    "What's causing the timeout errors in the database service?",
    "Analyze the error pattern from yesterday afternoon",
    
    # Resource issues
    "Why is CPU usage so high on the API servers?",
    "What caused the memory spike last night?",
    "Show me disk usage trends over the past week",
    
    # Dependency issues
    "Is there a problem with our downstream services?",
    "What happened to the authentication service at 2 PM?",
    "Check for any cascading failures this morning",
    
    # General analysis
    "Are there any anomalies in the last 6 hours?",
    "Summarize all incidents from yesterday",
    "What was the most impactful issue last week?"
]
```

---

## Appendix C: Decision Matrix - Which Path Should You Choose?

| Criteria | 🎓 Free Student Path | ☁️ AWS Production Path |
|----------|---------------------|------------------------|
| **Cost** | $0 | $50-70/month (or free with AWS credits) |
| **Setup Time** | 5 minutes | 1-2 hours |
| **Learning Focus** | Multi-agent patterns | AWS cloud services |
| **LLM Provider** | Ollama (local) | Bedrock (Claude) |
| **Data Storage** | Local CSV/JSON | CloudWatch |
| **Scalability** | Limited to laptop | Production-ready |
| **Internet Required** | No (works offline) | Yes |
| **Portfolio Value** | High (shows ML/AI skills) | High (shows cloud skills) |
| **Resume Bullet** | "Multi-agent AI system" | "AWS cloud architecture" |
| **Best For** | Students, learning, prototyping | Production deployment |

### Recommendation

**Start with the free student path** because:
1. ✅ Zero cost - no credit card needed
2. ✅ Faster to get started (no AWS account setup)
3. ✅ Focus on learning multi-agent patterns
4. ✅ Can migrate to AWS later if needed
5. ✅ Works offline (code on the go)
6. ✅ Easier to debug locally
7. ✅ Still looks impressive on resume!

**Migrate to AWS** when:
- You get AWS student credits ($100-300)
- You want production deployment experience
- You need to scale beyond laptop capabilities
- You want to add CloudWatch integration to resume

---

## Appendix D: Resources for Students

### Learning Materials

**Multi-Agent Systems:**
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [CrewAI Documentation](https://docs.crewai.com/)
- [Multi-Agent Coordination Patterns](https://www.anthropic.com/research/agents)

**Anomaly Detection:**
- Statistical Methods: Z-score, IQR, Moving Averages
- Time-Series Analysis: Decomposition, Seasonality
- [scikit-learn Anomaly Detection](https://scikit-learn.org/stable/modules/outlier_detection.html)

**LLM & Prompt Engineering:**
- [Ollama Documentation](https://ollama.com/docs)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)
- [LangChain Tutorials](https://python.langchain.com/docs/tutorials/)

**AWS Free Resources:**
- [AWS Educate](https://aws.amazon.com/education/awseducate/) - Get $100-300 credits
- [AWS Free Tier](https://aws.amazon.com/free/) - 12 months free services
- [AWS Bedrock Documentation](https://docs.aws.amazon.com/bedrock/)

### Similar Projects for Inspiration
- AutoGPT - Multi-agent task automation
- MetaGPT - Software development agents
- AgentGPT - Goal-oriented agents

### Resume Tips
**Good bullet points:**
- "Built multi-agent AI system using LangGraph that reduced troubleshooting time by 60%"
- "Designed and implemented anomaly detection algorithms achieving 85%+ accuracy"
- "Orchestrated 3 specialized agents (detection, analysis, reporting) for automated root-cause analysis"

**Avoid:**
- Overemphasizing tools over accomplishments
- Generic statements without metrics
- Missing the "why" (business value)

---

**Document Version:** 1.0  
**Last Updated:** November 5, 2025  
**Owner:** Pragnya Suresh  
**License:** MIT (feel free to use and modify)

