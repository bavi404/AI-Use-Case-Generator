class MarketAnalysisAgent:
    def __init__(self):
        pass
    
    def analyze_trends(self, research_results):
        ai_use_cases = []
        
        for result in research_results:
            title = result.get('title', '')
            link = result.get('link', '')
            
            if "AI" in title or "ML" in title or "automation" in title:
                ai_use_cases.append({
                    "title": title,
                    "link": link,
                    "use_case": self.extract_use_case(title)
                })
        
        return ai_use_cases
    
    def extract_use_case(self, title):
        if "predictive" in title.lower():
            return "Predictive Analytics"
        if "automation" in title.lower():
            return "Process Automation"
        if "recommendation" in title.lower():
            return "Recommendation Systems"
        if "chatbot" in title.lower():
            return "AI-Powered Chatbot"
        
        return "General AI Application"
