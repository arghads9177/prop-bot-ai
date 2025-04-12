# workflow/graph.py

from langgraph.graph import StateGraph, END
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from agents.state import AppState
from agents.freelancer_profile_checker import freelancer_profile_checker_agent
from agents.company_profile_checker import company_profile_checker_agent
from agents.job_description_researcher import job_description_researcher_agent
from agents.proposal_writer_agent import proposal_writer_agent


# 🧠 Create LangGraph with Shared State
def create_proposal_workflow():
    workflow = StateGraph(AppState)

    # 🔹 Add agent nodes
    workflow.add_node("FreelancerProfileChecker", freelancer_profile_checker_agent)
    workflow.add_node("CompanyProfileChecker", company_profile_checker_agent)
    workflow.add_node("JobDescriptionResearcher", job_description_researcher_agent)
    workflow.add_node("ProposalWriter", proposal_writer_agent)

    # 🔄 Define edges (data flow)
    # Assume user selects freelancer or company dynamically in your Streamlit UI
    workflow.set_entry_point("FreelancerProfileChecker")
    workflow.add_edge("FreelancerProfileChecker", "JobDescriptionResearcher")
    workflow.add_edge("JobDescriptionResearcher", "ProposalWriter")
    workflow.add_edge("ProposalWriter", END)

    # Optional: alternate entry flow for company users
    workflow.add_edge("CompanyProfileChecker", "JobDescriptionResearcher")

    return workflow.compile()

