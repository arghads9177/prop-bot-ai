# Implementation of a tool to check freelancer profiles.

from langchain_core.tools import tool
from langchain_core.runnables import Runnable
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
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

# Prompt Template for Profile Extraction
prompt = PromptTemplate.from_template("""
You are an expert assistant helping extract freelancer information for a proposal generator system.

Given the freelancer profile text below, extract the following details in JSON format. 
If the information is insufficient or not related to a freelancer profile, reply with:
{{"error": "Invalid or insufficient freelancer information provided."}}

Required JSON structure:
{{
  "name": "<Full Name>",
  "email": "<Email>",
  "phone": "<Phone Number>",
  "website": "<Website>",
  "skills": ["<Skill1>", "<Skill2>", ...],
  "experience": "<Experience Summary>",
  "certifications": ["<Cert1>", "<Cert2>", ...],
  "portfolio": ["<Project1>", "<Project2>", ...]
}}

Freelancer Profile:
```{profile}```
""")

# Define the agent logic
@tool
def freelancer_profile_checker_agent(state: AppState) -> AppState:
    """
    Validates and extracts relevant freelancer information from the input string.
    Returns a structured dictionary if valid, or an error message if not.
    """
    print("📥 Received state in freelancer_profile_checker:")
    print(state)
    profile = state.get("freelancer_profile", "")
    if not profile.strip():
        return {"freelancer_info": None, "steps_completed": state.get("steps_completed", []) + ["Freelancer Profile Checker"], "error": "No freelancer profile provided."}

    # formatted_prompt = prompt.format(profile=profile)
    chain = prompt | llm
    # Run the chain
    response = chain.invoke({"profile": profile})
    # response = llm.invoke(formatted_prompt)

    try:
        parsed = parser.parse(response.content)
        if "error" in parsed:
            return {"freelancer_info": None, "steps_completed": state.get("steps_completed", []) + ["Freelancer Profile Checker"], "error": parsed["error"]}
        return {"freelancer_info": parsed, "steps_completed": state.get("steps_completed", []) + ["Freelancer Profile Checker"]}
    except Exception:
        return {"freelancer_info": None, "steps_completed": state.get("steps_completed", []) + ["Freelancer Profile Checker"], "error": "Failed to parse freelancer info."}
