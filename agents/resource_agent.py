import requests

class ResourceAgent:
    def __init__(self):
        self.kaggle_url = "https://www.kaggle.com/search?q="
        self.huggingface_url = "https://huggingface.co/models?search="
        self.github_url = "https://api.github.com/search/repositories"

    def search_resources(self, use_case):
        datasets = {}

        # Kaggle Search
        kaggle_search = self.kaggle_url + use_case.replace(" ", "+")
        datasets['Kaggle'] = kaggle_search

        # HuggingFace Search
        huggingface_search = self.huggingface_url + use_case.replace(" ", "+")
        datasets['HuggingFace'] = huggingface_search

        # GitHub Search
        github_search = self.search_github(use_case)
        datasets['GitHub'] = github_search

        return datasets

    def search_github(self, query):
        params = {
            'q': f"{query} AI dataset",
            'sort': 'stars',
            'order': 'desc'
        }
        response = requests.get(self.github_url, params=params)
        if response.status_code == 200:
            results = response.json().get('items', [])
            return [repo['html_url'] for repo in results[:5]]
        return ["No GitHub results found"]
