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
    Argha Dey Sarkar With over 13+ years of experience as a software developer and a Master of Computer Applications (MCA), I bring a unique blend of expertise in software development and data science. My professional journey spans across Web & Mobile App development, REST API design, project analysis, and database architecture. Currently, I also consult for two clients on a regular basis, helping them build and optimize their web and mobile applications.

In addition to software development, I have ventured into data science and artificial intelligence, developing cutting-edge AI products and consulting businesses to harness the power of data and automation. I specialize in exploratory data analysis, predictive modeling, and deploying AI applications, including generative AI solutions powered by Transformers and Large Language Models (LLMs).

What I Offer

1. Data Science Expertise: Exploratory data analysis, visualization, and actionable insights using Python and its powerful libraries.
2. Machine Learning & Deep Learning: Expertise in applying ML algorithms, ANN, CNN, and NLP techniques to solve complex problems.
3. Generative AI & LLMs: Experience in developing next-gen applications using cutting-edge technologies like Transformers and LLMs.
4. Custom AI Solutions: Tailored AI-driven applications and AI Agents to improve business efficiency and innovation.
5. Software Development & Consultancy: End-to-end development for web and mobile applications, REST APIs, and scalable database designs.

Key Skills:

1. Data Science & AI
a. Data Analysis & Visualization: Python (Pandas, Matplotlib, Seaborn, Plotly)
b. Machine Learning: Scikit-learn, TensorFlow, PyTorch, XGBoost
c. Deep Learning: ANN, CNN, and NLP models
d. Generative AI: Transformers, Large Language Models (e.g., GPT, BERT), LangChain, RAG
e. Agentic AI: Phidata/Agno, LangFlow, LangGraph
f. Vector databases: ChromaDB, Pinecone, AstraDB
g. Tools & Platforms: Jupyter Notebooks, Google Colab, Kaggle Notebooks, Docker


2. Software Development
a. Full-stack Web & Mobile App Development
b. REST API Design and Integration
c. Scalable Database Design and Management (MySQL, PostgreSQL, MongoDB)
d. Agile Project Analysis & Delivery

Why Choose Me?

1. Versatile Expertise: Proficient in both software development and advanced AI/ML technologies.
2. Problem Solver: Known for delivering innovative solutions tailored to client needs.
3. Professional Reliability: Over a decade of experience consulting and developing industry-grade applications.
4. Cutting-Edge Innovator: Actively gaining expertise in generative AI and agentic AI to stay ahead in the AI revolution.

Projects:
1. AI-Powered ATS Resume Optimizer for Job Matching
2. PropBot AI: AI-Powered Proposal Generation Tool
3. AI-Powered Customer Support Bot for Aastha Co-operative Society
4. Material Name & Quantity Prediction for Construction Work Scheduling
5.Web app and mobile app of Co-Operative Bank Management
6. eCollect: Web & Mobile Collection Management System
7. Rolling Block Planning And Monitoring System for Indian Railways

Contact Me:
email2argha@gmail.com or +918373074701
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