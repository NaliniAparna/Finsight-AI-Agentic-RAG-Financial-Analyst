
import streamlit as st
from langgraph_backend import financial_graph_v4

st.set_page_config(
    page_title="Financial Intelligence AI",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Financial Intelligence AI")
st.caption(
    "Infosys FY 2024–25 Annual Report | "
    "RAG + Gemini + LangGraph"
)

st.info(
    "Answers are grounded in the Infosys annual "
    "report. Check PDF page citations before "
    "using financial figures."
)

with st.sidebar:
    st.header("About this application")
    st.write(
        "An AI-powered financial research assistant "
        "using ChromaDB, sentence-transformers, "
        "Google Gemini and LangGraph."
    )
    st.write("Document: Infosys Annual Report FY 2024–25")

    if st.button("Clear chat history"):
        st.session_state.messages = []
        st.rerun()

if "messages" not in st.session_state:
    st.session_state.messages = []

suggested_questions = [
    "What was Infosys consolidated revenue in FY 2024-25?",
    "What was the percentage increase in Infosys "
    "consolidated operating cash flow in FY 2024-25?",
    "What business risks did Infosys report?"
]

st.subheader("Suggested questions")

selected_question = st.selectbox(
    "Choose a question",
    ["Select a question"] + suggested_questions
)

ask_suggestion = st.button("Ask selected question")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

typed_question = st.chat_input(
    "Ask a question about Infosys financial reports..."
)

question = typed_question

if ask_suggestion and selected_question != "Select a question":
    question = selected_question

if question:
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("Analyzing annual report..."):
            try:
                result = financial_graph_v4.invoke({
                    "question": question,
                    "evidence": [],
                    "evidence_valid": False,
                    "validation_message": "",
                    "answer": ""
                })

                answer = result.get(
                    "answer",
                    "No answer was generated."
                )

                st.markdown(answer)

            except Exception as error:
                answer = (
                    "Unable to complete the request. "
                    "Please try again or check the "
                    "application logs."
                )
                st.error(answer)
                st.exception(error)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })
