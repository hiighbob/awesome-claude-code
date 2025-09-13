import anthropic
from github import Github

def ask_claude(api_key, prompt):
    client = anthropic.Anthropic(api_key=api_key)
    response = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=256,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.content if hasattr(response, "content") else str(response)

def github_info(token, repo_name):
    g = Github(token)
    repo = g.get_repo(repo_name)
    return {
        "name": repo.full_name,
        "description": repo.description,
        "stars": repo.stargazers_count,
        "issues": repo.open_issues_count,
        "topics": repo.get_topics(),
    }