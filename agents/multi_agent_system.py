from autogen import AssistantAgent, UserProxyAgent, GroupChat, GroupChatManager
from utils.config import get_llm_config

llm_config = get_llm_config()

reader_agent = AssistantAgent(
    name="ReaderAgent",
    llm_config=llm_config,
    system_message="You are an expert at reading policy documents. Extract and summarize important clauses, responsibilities, and regulatory statements."
)

compliance_agent = AssistantAgent(
    name="ComplianceExpertAgent",
    llm_config=llm_config,
    system_message="You are a compliance expert. Analyze the extracted clauses for compliance with GDPR and other data regulations. Identify potential violations or risks."
)

risk_agent = AssistantAgent(
    name="RiskAssessmentAgent",
    llm_config=llm_config,
    system_message="You are a risk assessor. For each compliance issue found, assign a severity level (Low, Medium, High) and explain the rationale."
)

editor_agent = AssistantAgent(
    name="EditorAgent",
    llm_config=llm_config,
    system_message="You are a legal editor. Suggest improved wording or additions to make the clauses compliant with regulations."
)

coordinator_agent = UserProxyAgent(
    name="CoordinatorAgent",
    llm_config=llm_config,
    code_execution_config=False
)
def run_analysis(document_text):
    groupchat = GroupChat(
        agents=[
            coordinator_agent,
            reader_agent,
            compliance_agent,
            risk_agent,
            editor_agent
        ],
        messages=[],
        max_round=10
    )

    manager = GroupChatManager(
        groupchat=groupchat,
        llm_config=llm_config,
        human_input_mode="NEVER"
    )

    # After initiation
    coordinator_agent.initiate_chat(
        manager,
        message=f"Please analyze this document:\n\n{document_text}"
    )

    # Get the messages from the group chat
    messages = manager.groupchat.messages

    conversation_by_agent = {}

    for msg in messages:
        print(type(msg), msg)  # Debug print to verify message type & structure

        sender = getattr(msg, "name", None) or msg.get("name", None)
        content = getattr(msg, "content", None) or msg.get("content", None)
        if content:
            content = content.strip()
            if sender not in conversation_by_agent:
                conversation_by_agent[sender] = []
            conversation_by_agent[sender].append(content)

    return conversation_by_agent