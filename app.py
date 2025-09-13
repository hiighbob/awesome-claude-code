import streamlit as st
import anthropic
from github import Github
from utils import ask_claude, github_info

st.set_page_config(page_title="Claude AI + GitHub Webapp", layout="wide")

st.title("Claude AI + GitHub Explorer (Mobile-ready)")

with st.sidebar:
    st.header("Settings")
    claude_api_key = st.text_input("Claude API Key", type="password")
    github_token = st.text_input("GitHub Token", type="password")
    repo_name = st.text_input("GitHub Repo (owner/repo)", value="hiighbob/awesome-claude-code")

tab1, tab2 = st.tabs(["Ask Claude", "Browse GitHub"])

with tab1:
    st.subheader("Chat with Claude")
    user_query = st.text_area("Your question to Claude:", "")
    if st.button("Ask Claude"):
        if claude_api_key and user_query:
            response = ask_claude(claude_api_key, user_query)
            st.success(response)
        else:
            st.error("Provide an API key and question.")

with tab2:
    st.subheader("GitHub Repo Explorer")
    if github_token and repo_name:
        repo_data = github_info(github_token, repo_name)
        st.json(repo_data)
    else:
        st.info("Enter your GitHub token and repo in settings.")

st.markdown("""
<style>
body { font-size: 18px; }
@media (max-width: 600px) { .stTextInput, .stTextArea { font-size: 20px; } }
</style>
""", unsafe_allow_html=True)