# Implementation of Application State for the Agents

from typing_extensions import Optional, List, Dict, TypedDict

class AppState(TypedDict, total=False):
    # Input values
    freelancer_profile: Optional[str]
    company_profile: Optional[str]
    job_description: Optional[str]

    # Output from Freelancer Profile Checker Agent
    freelancer_info: Optional[Dict[str, str]]

    # Output from Company Profile Checker Agent
    company_info: Optional[Dict[str, str]]

    # Output from Job Description Researcher Agent
    job_analysis: Optional[Dict[str, str]]  # e.g., tasks, materials, time_estimate

    # Output from Proposal Writer Agent
    generated_proposal: Optional[str]

    # Optional: Status logging
    steps_completed: Optional[List[str]]
