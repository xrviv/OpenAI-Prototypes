import requests
import json

def get_contributors(repo):
    contributors = []
    url = f"https://api.github.com/repos/{repo}/contributors"
    while url:
        response = requests.get(url)
        data = json.loads(response.text)
        contributors.extend(data)
        if "next" in response.links:
            url = response.links["next"]["url"]
        else:
            url = None
    return sorted(contributors, key=lambda x: x["contributions"], reverse=True)

repo = "bitcoin/bitcoin"
contributors = get_contributors(repo)

with open("bitcoin-contributors.md", "w") as file:
    for contributor in contributors:
        file.write(f"{contributor['login']} - {contributor['contributions']} contributions\n")
