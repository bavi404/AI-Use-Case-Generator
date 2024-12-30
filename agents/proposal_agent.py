class ProposalAgent:
    def __init__(self, output_dir="outputs"):
        self.output_dir = output_dir

    def generate_proposal(self, ai_use_cases):
        proposal_content = "# AI/ML Use Case Proposal\n\n"
        proposal_content += "### Overview\nThis document highlights potential AI/ML use cases identified through market research.\n\n"

        for case in ai_use_cases:
            proposal_content += f"## {case['use_case']}\n"
            proposal_content += f"**Title**: {case['title']}\n\n"
            proposal_content += f"**Learn More**: [Link]({case['link']})\n\n"
            proposal_content += f"### Relevant Datasets\n"

            for source, links in case['datasets'].items():
                proposal_content += f"- **{source}**: \n"
                if isinstance(links, list):
                    for link in links:
                        proposal_content += f"  - [Dataset]({link})\n"
                else:
                    proposal_content += f"  - [Search Link]({links})\n"
            proposal_content += "\n---\n"

        # Save to file
        with open(f"{self.output_dir}/ai_use_case_proposal.md", "w", encoding="utf-8") as file:
            file.write(proposal_content)

        print(f"\nProposal saved to {self.output_dir}/ai_use_case_proposal.md")
