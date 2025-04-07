# test_freelancer_profile_checker.py
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from agents.freelancer_profile_checker import freelancer_profile_checker_agent
from agents.state import AppState

# ✅ Example 1: Valid Freelancer Profile
# Sample input
valid_input = {
    "freelancer_profile": """
    John Doe is a seasoned developer with over 5 years of experience in full-stack development and AI tools.
    His skills include React, Node.js, and LangChain.
    He has built a chatbot for CRM and an e-commerce app.
    He is AWS Certified Developer.
    """
}

# Convert to State
valid_state = AppState(**valid_input)

# ❌ Example 2: Invalid Input (not a freelancer profile)
invalid_input = {
    "freelancer_profile": "Looking for someone to build a mobile app using Flutter and Firebase."
}

# Convert to State
invalid_state = AppState(**invalid_input)


# ❌ Example 3: Empty Input
empty_input = {
    "freelancer_profile": ""
}

# Convert to State
empty_state = AppState(**empty_input)

print("✅ Valid Input Test:")
print(freelancer_profile_checker_agent.invoke({"state": valid_state}))

print("\n❌ Invalid Input Test:")
print(freelancer_profile_checker_agent.invoke({"state": invalid_state}))

print("\n❌ Empty Input Test:")
print(freelancer_profile_checker_agent.invoke({"state": empty_state}))