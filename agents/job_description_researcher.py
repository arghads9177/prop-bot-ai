# Implementation of a tool to analyze job description.

from langchain_core.tools import tool
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
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

# Output parser
parser = JsonOutputParser()

@tool
def job_description_researcher_agent(state: AppState) -> AppState:
    """
    Validates and analyzes job description to extract project type, tasks, time specifications, materials/tech stack, and key deliverables.
    """

    job_description = state.get("job_description", "")
    if not job_description.strip():
        return {"job_analysis": None, "steps_completed": state.get("steps_completed", []) + ["Job Description Analysis"], "error": "No job description provided."}
    
    prompt = PromptTemplate.from_template("""
    You are a job description analysis expert. First validate if the input text is a job description. If not, return:
    {{"error": "The provided text is not a valid job description."}}

    If valid, extract the following information:
    - Title of the project (if mentioned or can be inferred)
    - Project type: Is it Software Development, Hardware Supply, Networking, or a combination?
    - Software Type: Is it Web, Mobile, Desktop, or combination of two or more type?(If it is software development)
    - Client name (if available)
    - Tasks:
    - For Software Development or Networking: list of development or configuration tasks
    - For Hardware Supply: list of hardware items to be supplied
    - For each task, provide a title, brief description, and specified time (man-days/weeks/months)
    - Total specified time for the full project (if mentioned)
    - Tech stack or materials used or required
    - For Software Development tech stack should contain only list of programming languages, frameworks, and tools (if specified). Don't specify any other information.
    - Safety/security terms and conditions (if any)
    - Other terms and conditions (if any)
    - Payment terms (if any)
    - Penalty terms (if any)
    - Project Milestones (bulleted or listed format) (if any)
    - Payment Milestones (bulleted or listed format) (if any)
    - Key deliverables (bulleted or listed format)

    Return the result in JSON format like:
    {{
    "title": "...",
    "project_type": "...",
    "software_type": "...",
    "client_name": "...",
    "tasks": [
        {{
        "title": "...",
        "description": "...",
        "specified_time": "..."
        }}
    ],
    "total_specified_time": "...",
    "tech stack/materials": ["...", "..."],
    "safety_terms": "...",
    "other_terms": "...",
    "payment_terms": "...",
    "penalty_terms": "...",
    "project_milestones": ["...", "..."],
    "payment_milestones": ["...", "..."],
    "key_deliverables": ["...", "..."]
    }}

    Job Description:
    {job_description}
    """)
    
    chain: Runnable = prompt | llm
    response = chain.invoke({"job_description": job_description})

    try:
        parsed = parser.parse(response.content)
        if "error" in parsed:
            return {"job_analysis": None, "steps_completed": state.get("steps_completed", []) + ["Job Description Analysis"], "error": parsed["error"]}
        return {"job_analysis": parsed, "steps_completed": state.get("steps_completed", []) + ["Job Description Analysis"]}
    except Exception:
        return {"job_analysis": None, "steps_completed": state.get("steps_completed", []) + ["Job Description Analysis"], "error": "Failed to parse job description."}