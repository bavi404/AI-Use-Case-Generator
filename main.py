from agents.research_agent import ResearchAgent
from agents.market_analysis_agent import MarketAnalysisAgent
from agents.resource_agent import ResourceAgent
from agents.proposal_agent import ProposalAgent
from dotenv import load_dotenv

load_dotenv()

def main():
    research_agent = ResearchAgent()
    market_analysis_agent = MarketAnalysisAgent()
    resource_agent = ResourceAgent()
    proposal_agent = ProposalAgent()
    
    # Research Phase
    company_results = research_agent.search_company("Tesla")
    industry_results = research_agent.search_industry("Automotive")

    # Market Analysis Phase
    ai_use_cases = market_analysis_agent.analyze_trends(company_results + industry_results)

    # Resource Collection Phase
    for case in ai_use_cases:
        datasets = resource_agent.search_resources(case['use_case'])
        case['datasets'] = datasets  # Add datasets to each use case

    # Proposal Generation Phase
    proposal_agent.generate_proposal(ai_use_cases)

if __name__ == "__main__":
    main()
