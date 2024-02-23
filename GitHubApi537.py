import requests
import json

def get_user_repositories(user_id):
    url = f"https://api.github.com/users/{user_id}/repos"
    response = requests.get(url)
    if response.status_code == 200:
        repos = json.loads(response.text)
        return [repo['name'] for repo in repos]
    else:
        print(f"Failed to fetch repositories for user {user_id}")
        return []

def get_commit_count(user_id, repo):
    url = f"https://api.github.com/repos/{user_id}/{repo}/commits"
    response = requests.get(url)
    if response.status_code == 200:
        commits = json.loads(response.text)
        return len(commits)
    else:
        print(f"Failed to fetch commits for repository {repo}")
        return 0

def get_repo_commits(user_id):
    repositories = get_user_repositories(user_id)
    result = []
    for repo in repositories:
        commit_count = get_commit_count(user_id, repo)
        result.append((repo, commit_count))
    return result

# Unit tests
def test_get_user_repositories():
    assert get_user_repositories("richkempinski") == ["hellogitworld"]

def test_get_commit_count():
    assert get_commit_count("richkempinski", "hellogitworld") > 0

def test_get_repo_commits():
    assert get_repo_commits("richkempinski") == [("hellogitworld", 30)]  # Update commit count accordingly

if __name__ == "__main__":
    user_id = input("Enter GitHub user ID: ")
    repo_commits = get_repo_commits(user_id)
    for repo, commit_count in repo_commits:
        print(f"Repo: {repo} Number of commits: {commit_count}")
