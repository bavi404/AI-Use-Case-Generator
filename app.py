import streamlit as st
from agents.research_agent import ResearchAgent
from agents.market_analysis_agent import MarketAnalysisAgent
from agents.resource_agent import ResourceAgent
from agents.proposal_agent import ProposalAgent
from dotenv import load_dotenv

load_dotenv()

# Title
st.title("AI/ML Use Case Generator")

# User Input
company_name = st.text_input("Enter Company Name (e.g., Tesla):")
industry_name = st.text_input("Enter Industry (e.g., Automotive):")

if st.button("Generate Use Cases"):
    st.write("**Running Agents...**")

    research_agent = ResearchAgent()
    market_analysis_agent = MarketAnalysisAgent()
    resource_agent = ResourceAgent()
    proposal_agent = ProposalAgent()

    # Research Phase
    company_results = research_agent.search_company(company_name)
    industry_results = research_agent.search_industry(industry_name)

    # Market Analysis Phase
    ai_use_cases = market_analysis_agent.analyze_trends(company_results + industry_results)

    # Resource Collection Phase
    for case in ai_use_cases:
        datasets = resource_agent.search_resources(case['use_case'])
        case['datasets'] = datasets  # Attach datasets to each use case

    # Proposal Generation Phase
    proposal_agent.generate_proposal(ai_use_cases)
    
    # Display Results
    st.success("Proposal Generated Successfully! 📄")
    st.download_button("Download Proposal", data=open("outputs/ai_use_case_proposal.md").read(), file_name="ai_use_case_proposal.md")
    
    st.write("### AI/ML Use Cases Identified:")
    for case in ai_use_cases:
        st.write(f"**{case['use_case']}** - {case['title']}")
        st.markdown(f"[Learn more]({case['link']})")
