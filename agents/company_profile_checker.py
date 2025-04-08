# agents/company_profile_checker.py

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.tools import tool
from langchain_groq import ChatGroq
from langchain_core.runnables import Runnable
from dotenv import load_dotenv
import os


from agents.state import AppState

# Load environment variables
load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

@tool
def company_profile_checker_agent(state: AppState) -> AppState:
    """
    Validates a company profile and extracts key details like name, industry, location, website, and description.
    """
    profile = state.get("company_profile", "")
    if not profile or len(profile.strip()) < 20:
        return AppState(company_profile=profile, result="❌ Company profile information is too short or empty.")

    prompt = PromptTemplate.from_template("""
    You are a company profile validator and extractor. 

    Given the following text, determine if it's a valid company profile. If valid, extract:
    - name
    - industry
    - location
    - website (if any)
    - description

    Respond ONLY in the following JSON format:
    {{
      "name": "...",
      "industry": "...",
      "location": "...",
      "website": "...",
      "description": "...",
      "experience": "...",
      "services/products": "...",
      "clients": "...",
      "business regions/countries": "...",
      "mission": "...",
      "vision": "...",
      "email": "...",
      "phone": "...",
      "certifications": "...",
    }}

    If the input is not a company profile or lacks enough information, reply with:
    "❌ Not a valid company profile or insufficient information."

    Text:
    {company_profile}
    """)

    # Load the model from Groq (use Llama-3.3 model)
    llm = ChatGroq(model_name="llama-3.3-70b-versatile")

    # Output parser
    parser = JsonOutputParser()


    chain: Runnable = prompt | llm

    response = chain.invoke({"company_profile": profile})

    # return AppState(company_profile=profile, result=response.content.strip())

    try:
        parsed = parser.parse(response.content)
        if "error" in parsed:
            return {"company_profile": None, "steps_completed": state.get("steps_completed", []) + ["Company Profile Checker"], "error": parsed["error"]}
        return {"company_profile": parsed, "steps_completed": state.get("steps_completed", []) + ["Company Profile Checker"]}
    except Exception:
        return {"company_profile": None, "steps_completed": state.get("steps_completed", []) + ["Company Profile Checker"], "error": "Failed to parse company profile."}
