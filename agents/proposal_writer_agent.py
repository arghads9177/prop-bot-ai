# Implemenration of the proposal writer agent

from langchain_core.tools import tool
from langchain.prompts import PromptTemplate
from langchain_core.runnables import Runnable
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os


from agents.state import AppState

# Load environment variables
load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

# Load the model from Groq (use Llama-3.3 model)
llm = ChatGroq(model_name="llama-3.3-70b-versatile")


# Prompt templates
freelancer_template = PromptTemplate(
    input_variables=["freelancer", "job_details"],
    template=(
        "You are an expert freelancing proposal writer. Generate a professional proposal using the following freelancer and job details:\n\n"
        "Freelancer Info: {freelancer}\n"
        "Job Info: {job_details}\n"
        "Follow this exact Markdown format:\n\n"
        "# Freelancing Proposal\n"
        "*Freelancer: [Freelancer Name]* | Email: *[Email]* | M: *[Phone]* | Website: *[Website]*\n\n"
        "**Proposal for:** [Project Name]\n"
        "**Prepared By:** [Freelancer Name]\n"
        "**Date:** [Proposal Date]\n\n"
        "## 1. Introduction\n"
        "## 2. About Me\n"
        "## 3. Understanding Your Needs\n"
        "## 4. Proposed Approach & Work Plan\n"
        "## 5. Deliverables\n"
        "## 6. Timeline & Availability\n"
        "## 7. Pricing & Payment Terms\n"
        "## 8. Why Choose Me?\n"
        "## 9. Next Steps\n\n"
        "Best regards,\n"
            "[Freelancer Name]\n"
            "[Your Freelance Role, e.g., Web Developer, Copywriter, Graphic Designer]\n"
            "Website:[Portfolio/Website Link]\n"
        "Note: Replace placeholders intelligently based on input."
    ),
)

business_template = PromptTemplate(
    input_variables=["company", "job_details"],
    template=(
        "You are an expert business proposal writer. Generate a professional proposal using the following company and job details:\n\n"
        "Company Info: {company}\n"
        "Job Info: {job_details}\n"
        "Follow this exact Markdown format:\n\n"
        "# Business Proposal\n"
        "**Prepared For:** [Client Name]\n"
        "**Prepared By:** [Company Name]\n"
        "**Date:** [Proposal Date]\n\n"
        "## 1. Executive Summary\n"
        "## 2. About Us\n"
        "## 3. Services Offered\n"
        "## 4. Proposed Solution\n"
        "## 5. Project Timeline\n"
        "## 6. Pricing & Payment Terms\n"
        "## 7. Why Choose Us?\n"
        "## 8. Terms & Conditions\n"
        "## 9. Next Steps\n\n"
        "Sincerely,\n[Company Name]"
        "Note: Replace placeholders intelligently based on input."
    ),
)

@tool
def proposal_writer_agent(state: AppState) -> AppState:
    """Generate a proposal in Markdown format using freelancer or company profile and job details."""

    print("Proposal Writer Agent Invoked")
    try:
        if not state["job_analysis"]:
            # state.error = "No job description provided."
            return {"generated_proposal": None, "steps_completed": state.get("steps_completed", []) + ["Proposal Generation"], "error": "No job description provided."}
        print("Job analysis found.")
        if state.get("freelancer_info", ""):
            print("Freelancer profile found.")
            prompt = freelancer_template.format(
                freelancer=state["freelancer_info"],
                job_details=state["job_analysis"]
            )
        elif state["company_info"]:
            print("Company profile found.")
            prompt = business_template.format(
                company=state["company_info"],
                job_details=state["job_analysis"]
            )
        else:
            print("Neither freelancer nor company profile found.")
            # state.error = "Neither freelancer nor company profile available."
            return {"generated_proposal": None, "steps_completed": state.get("steps_completed", []) + ["Proposal Generation"], "error": "Neither freelancer nor company profile available.."}
        chain: Runnable = llm
        response = chain.invoke(prompt)
        print(response)
        # state.generated_proposal = response.content
        # return state
        return {"generated_proposal": response.content, "steps_completed": state.get("steps_completed", []) + ["Proposal Generation"]}
    except Exception as e:
        print(f"Error generating proposal: {e}")
        return {"generated_proposal": None, "steps_completed": state.get("steps_completed", []) + ["Proposal Generation"], "error": "Failed to generate proposal."}
