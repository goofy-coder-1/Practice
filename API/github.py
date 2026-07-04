import requests

class GitHubClient:
    def __init__(self, username):
        self.username = username
        self.base_url = "https://api.github.com"

    def fetch_profile(self):
        """Fetches the user's profile data."""
        url = f"{self.base_url}/users/{self.username}"
        response = requests.get(url)
        
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return {"error": "User not found."}
        else:
            return {"error": f"Failed with status code {response.status_code}"}

    def display_info(self):
        """Prints a formatted summary of the profile."""
        data = self.fetch_profile()
        
        if "error" in data:
            print(data["error"])
        else:
            print(f"--- GitHub Profile: {data.get('login')} ---")
            print(f"Name: {data.get('name')}")
            print(f"Bio: {data.get('bio')}")
            print(f"Public Repos: {data.get('public_repos')}")
            print(f"Followers: {data.get('followers')}")
            print(f"URL: {data.get('html_url')}")

# Usage
if __name__ == "__main__":
    user = GitHubClient("github") # Example: fetching the official 'github' profile
    user.display_info()