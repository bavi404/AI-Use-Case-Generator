import os
from serpapi import GoogleSearch

class ResearchAgent:
    def __init__(self):
        self.api_key = os.getenv("SERPAPI_API_KEY")

    def search_company(self, company_name):
        params = {
            "engine": "google",
            "q": f"{company_name} AI and ML applications",
            "api_key": self.api_key,
            "hl": "en"
        }
        search = GoogleSearch(params)
        result = search.get_dict()
        return result.get("organic_results", [])

    def search_industry(self, industry_name):
        params = {
            "engine": "google",
            "q": f"AI and ML trends in {industry_name} industry",
            "api_key": self.api_key,
            "hl": "en"
        }
        search = GoogleSearch(params)
        result = search.get_dict()
        return result.get("organic_results", [])
