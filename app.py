import requests

def fetch_github_user(username):
    response = requests.get(f"https://api.github.com/users/{username}")
    if response.status_code == 200:
        user_data = response.json()
        print(f"User: {user_data['login']}, ID: {user_data['id']}")
    else:
        print("Failed to fetch user")

if __name__ == "__main__":
    fetch_github_user("octocat")