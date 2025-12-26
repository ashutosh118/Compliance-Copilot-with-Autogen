import streamlit as st
import PyPDF2
from agents.multi_agent_system import run_analysis  # adjusted to correct module name

st.set_page_config(page_title="AI Compliance Copilot", layout="wide")
st.title("📜 AI Compliance Copilot")

uploaded_file = st.file_uploader("Upload a policy document (PDF)", type=["pdf"])

if uploaded_file:
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text = "\n".join([page.extract_text() or "" for page in pdf_reader.pages])

    st.text_area("Extracted Text", value=text, height=300)

    if st.button("Analyze for Compliance"):
        with st.spinner("Running multi-agent analysis..."):
            agent_conversations = run_analysis(text)

        st.success("✅ Analysis Complete")
        st.markdown("## 🧠 Agent-by-Agent Responses")

        agent_display_names = {
            "ReaderAgent": "📖 Reader Agent",
            "ComplianceExpertAgent": "🛡️ Compliance Expert",
            "RiskAssessmentAgent": "⚠️ Risk Assessor",
            "EditorAgent": "✍️ Legal Editor",
            "CoordinatorAgent": "🧑‍💼 Coordinator"
        }

        for agent, messages in agent_conversations.items():
            with st.container():
                st.markdown(f"### {agent_display_names.get(agent, agent)}")
                for idx, message in enumerate(messages, 1):
                    st.markdown(f"**Response {idx}:**")
                    st.markdown(f"> {message}")
                    st.markdown("---")
