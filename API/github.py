import requests

class GitHubUser:
    def __init__(self, username):
        self.username = username
        self.__base_url = "https://api.github.com/users/"

    def fetch_data(self):
        """Fetches the raw JSON data for the specific user."""
        try:
            response = requests.get(f"{self.__base_url}{self.username}")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError:
            return None

    def display_profile(self):
        """Processes and prints the user data."""
        data = self.fetch_data()
        
        if not data:
            print(f"Error: Could not find user '{self.username}'.")
            return

        print(f"\n--- Profile for: {data.get('login')} ---")
        print(f"Name: {data.get('name') or 'N/A'}")
        print(f"Bio: {data.get('bio') or 'No bio provided'}")
        print(f"Location: {data.get('location') or 'N/A'}")
        print(f"Followers: {data.get('followers')}")
        print(f"Public Repos: {data.get('public_repos')}")
        print(f"Link: {data.get('html_url')}")

# User Input
if __name__ == "__main__":
    target_user = input("Enter a GitHub username to search: ")
    profile = GitHubUser(target_user)
    profile.display_profile()