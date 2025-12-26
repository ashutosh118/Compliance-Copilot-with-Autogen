# 📜 AI Compliance Copilot

An intelligent multi-agent system built with **Microsoft Autogen** that analyzes policy documents for compliance violations and provides expert recommendations.

## 🎯 Overview

The Compliance Copilot leverages a sophisticated multi-agent architecture to perform comprehensive compliance analysis of policy documents. Using specialized AI agents, it identifies potential regulatory violations, assesses risks, and suggests improvements for better compliance with data protection regulations like GDPR.

## 🏗️ Architecture

### Multi-Agent System Design

The application implements **5 specialized agents** using the Autogen framework:

| Agent | Role | Responsibility |
|-------|------|----------------|
| 📖 **ReaderAgent** | Document Analyzer | Extracts and summarizes important clauses, responsibilities, and regulatory statements |
| 🛡️ **ComplianceExpertAgent** | Compliance Specialist | Analyzes extracted clauses for GDPR and data regulation violations |
| ⚠️ **RiskAssessmentAgent** | Risk Evaluator | Assigns severity levels (Low, Medium, High) with detailed rationale |
| ✍️ **EditorAgent** | Legal Content Improver | Suggests improved wording for regulatory compliance |
| 🧑‍💼 **CoordinatorAgent** | Orchestrator | Manages workflow and initiates analysis process |

### Technical Stack

- **Frontend**: Streamlit web interface
- **Multi-Agent Framework**: Microsoft Autogen
- **LLM**: Azure OpenAI GPT-4o
- **Document Processing**: PyPDF2
- **Configuration**: Environment-based settings

## 🚀 Features

### Core Capabilities
- ✅ **PDF Document Upload** - Support for policy document analysis
- 🔍 **Multi-Agent Analysis** - Collaborative AI agent workflow
- 📊 **Risk Assessment** - Severity classification with rationale
- 📝 **Compliance Review** - GDPR and data regulation analysis
- ✏️ **Improvement Suggestions** - Legal content recommendations
- 🎨 **Interactive UI** - User-friendly Streamlit interface

### Autogen Framework Benefits
- **Specialized Expertise**: Each agent focuses on specific analysis domains
- **Collaborative Intelligence**: Agents build upon each other's findings
- **Autonomous Workflow**: Self-managing conversation flow
- **Scalable Architecture**: Easy to add new analysis capabilities
- **Quality Assurance**: Multiple validation layers

## 📁 Project Structure

```
compliance_copilot/
├── app.py                          # Streamlit web interface
├── create_pdf.py                   # Dummy policy generator for testing
├── dummy_policy.pdf                # Sample policy document
├── requirements.txt                # Python dependencies
├── .env                           # Environment configuration
├── agents/
│   └── multi_agent_system.py      # Autogen agent definitions and orchestration
└── utils/
    └── config.py                  # LLM configuration and setup
```

## ⚙️ Setup and Installation

### Prerequisites
- Python 3.8+
- Azure OpenAI API access
- Virtual environment (recommended)

### Installation Steps

1. **Clone and Navigate**
   ```bash
   cd compliance_copilot
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   source .venv/bin/activate  # Linux/Mac
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment**
   
   Update `.env` file with your Azure OpenAI credentials:
   ```env
   OPENAI_API_TYPE=azure
   OPENAI_API_VERSION=2023-03-15-preview
   OPENAI_ENDPOINT=your_azure_endpoint
   OPENAI_API_KEY=your_api_key
   OPENAI_DEPLOYMENT_NAME=your_model_deployment
   ```

5. **Generate Test Document** (Optional)
   ```bash
   python create_pdf.py
   ```

## 🎮 Usage

### Running the Application

1. **Start the Streamlit App**
   ```bash
   streamlit run app.py
   ```

2. **Access the Interface**
   - Open your browser to `http://localhost:8501`
   - Upload a PDF policy document
   - Click "Analyze for Compliance"
   - Review agent-by-agent analysis results

### Analysis Workflow

1. **Document Upload**: Upload PDF policy document
2. **Text Extraction**: Automatic text extraction from PDF
3. **Multi-Agent Analysis**: 
   - Reader Agent extracts key clauses
   - Compliance Expert identifies violations
   - Risk Assessor evaluates severity
   - Editor suggests improvements
   - Coordinator manages the process
4. **Results Display**: Organized output by agent specialty

## 🔧 Configuration

### LLM Settings
The application uses Azure OpenAI with the following configuration:
- **Model**: GPT-4o
- **API Type**: Azure
- **Max Rounds**: 10 agent interactions
- **Human Input**: Disabled for autonomous operation

### Agent Customization
Each agent's behavior can be modified by updating their `system_message` in `agents/multi_agent_system.py`:

```python
reader_agent = AssistantAgent(
    name="ReaderAgent",
    llm_config=llm_config,
    system_message="Your custom prompt here..."
)
```

## 📊 Example Use Cases

### Supported Analysis Types
- **GDPR Compliance**: Data protection regulation adherence
- **Privacy Policy Review**: User rights and data handling practices
- **Risk Assessment**: Security and compliance risk evaluation
- **Legal Content Improvement**: Regulatory-compliant wording suggestions

### Sample Violations Detected
- Indefinite data storage without justification
- Lack of explicit user consent mechanisms
- Insufficient data encryption measures
- Missing user rights information
- Inadequate third-party data sharing policies

## 🛠️ Development

### Adding New Agents
1. Create new `AssistantAgent` in `multi_agent_system.py`
2. Define specialized system message
3. Add to `GroupChat` agent list
4. Update display names in `app.py`

### Extending Analysis Capabilities
- Modify agent prompts for new compliance domains
- Add industry-specific regulations (HIPAA, SOX, etc.)
- Implement custom risk scoring algorithms
- Integrate additional document formats

## 🔍 Technical Details

### Autogen Implementation
```python
# Group chat setup with multiple agents
groupchat = GroupChat(
    agents=[coordinator_agent, reader_agent, compliance_agent, risk_agent, editor_agent],
    messages=[],
    max_round=10
)

# Managed conversation flow
manager = GroupChatManager(
    groupchat=groupchat,
    llm_config=llm_config,
    human_input_mode="NEVER"
)
```

### Conversation Management
The system tracks and organizes agent conversations for structured output presentation, allowing users to see each agent's specific contributions to the analysis.

## 📋 Dependencies

Key packages:
- `autogen==0.9.7` - Multi-agent framework
- `streamlit` - Web interface
- `PyPDF2` - PDF processing
- `python-dotenv` - Environment management
- `azure-openai` - LLM integration

## 🚨 Security Considerations

- Environment variables for sensitive API keys
- No local data storage of uploaded documents
- Secure Azure OpenAI API communication
- No execution of arbitrary code by agents

## 🤝 Contributing

1. Fork the repository
2. Create feature branch
3. Implement changes with tests
4. Submit pull request with detailed description

## 📄 License

This project is part of Accenture's Data & AI initiatives.

## 🆘 Troubleshooting

### Common Issues
- **API Key Errors**: Verify `.env` configuration
- **PDF Processing**: Ensure PDF is text-based (not scanned images)
- **Agent Timeout**: Check Azure OpenAI service availability
- **Missing Dependencies**: Run `pip install -r requirements.txt`

### Support
For technical support or questions about the Compliance Copilot, please contact the Data & AI team.

---

*Built with ❤️ using Microsoft Autogen and Azure OpenAI*

CREDITS: Ashutosh Srivastava