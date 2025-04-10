# testing/test_proposal_writer_agent.py

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from agents.proposal_writer_agent import proposal_writer_agent
from agents.state import AppState

# ✅ Cleaned freelancer_info (all string values)
valid_freelancer_info = {
    "name": "Argha Dey Sarkar",
    "email": "email2argha@gmail.com",
    "phone": "+918373074701",
    "website": "https://portfolio.example.com",
    "skills": "Data Science & AI, Data Analysis, Machine Learning, Deep Learning, Generative AI, Full-stack Development",
    "experience": "Over 13+ years of experience as a software developer and data scientist",
    "certifications": "AWS Certified Developer",
    "portfolio": "AI-Powered ATS, ProposalBot, CRM Chatbot, Material Predictor"
}

# ✅ Cleaned company_info (already good)
valid_company_info = {
    'name': 'Softmeets Info Solutions', 
    'industry': 'IT Consulting, Digital Transformation', 
    'location': 'Asansol, Paschim Bardhaman, India', 
    'website': 'https://softmeets.com/', 
    'description': 'Softmeets Info Solutions is a digital transformation company that helps management teams create high levels of economic value by providing innovative solutions tailored to meet critical operational and strategic needs.', 
    'experience': 'Four decades', 
    'services/products': 'Digital transformation, SaaS, Automation, Internet of Things, Artificial intelligence & Analytics technologies', 
    'clients': 'Indian Railways, Indian Army, SAIL, Ministry of Communication, ICMR, West Bengal Housing Board, Chittaranjan Locomotive Works', 
    'business_regions/countries': 'India, Global', 
    'mission': 'To Transform your entire business to innovative digital business process', 
    'vision': 'Embrace cutting-edge automation, advanced analytics, and seamless integrations to optimize operations, improve decision-making, and deliver exceptional customer experiences.', 
    'email': 'INFO@SOFTMEETS.COM', 
    'phone': '+ (91) 9434 811 929, 0341-3500346', 
    'certifications': 'CMMI Level 5, ISO 27001:2013, ISO 20000-1:2018, ISO 9001:2015'
}

# ✅ Convert tasks list of dicts to bullet point string
def format_tasks(tasks):
    return "\n".join([f"- {t['title']}: {t['description']} (Time: {t['specified_time']})" for t in tasks])

# ✅ Convert list fields to comma-separated strings
def list_to_string(lst):
    return ", ".join(lst)

# ✅ Cleaned job_analysis
valid_job_analysis = {
    'title': 'Proposal to Upgrade Traffic Info System to Unified Rail Logistics System',
    'project_type': 'Software Development',
    'software_type': 'Web and Mobile',
    'client_name': 'Bokaro Steel Plant (BSL)',
    'tasks': format_tasks([
        {
            'title': 'Field Study and Analysis',
            'description': 'Conduct comprehensive field study and analyze existing software to design screens, reports, and data flow',
            'specified_time': '6 months (Phase-1)'
        },
        {
            'title': 'Software Development',
            'description': 'Develop a web and mobile app information portal for data entry and access',
            'specified_time': '6 months (Phase-1)'
        },
        {
            'title': 'Deployment and Testing',
            'description': 'Deploy the solution on BSL native cloud and perform performance testing and validation',
            'specified_time': '6 months (Phase-1)'
        },
        {
            'title': 'Onsite and Online Support',
            'description': 'Provide onsite and online support for the commissioned solution',
            'specified_time': '12 months (Phase-2)'
        },
        {
            'title': 'Modifications and Additions',
            'description': 'Implement approved modifications or additions in the solution',
            'specified_time': '12 months (Phase-2)'
        }
    ]),
    'total_specified_time': '18 months',
    'tech_stack': list_to_string(['PostgreSQL', 'APIs', 'Web and Mobile App Development']),
    'safety_terms': 'Strict adherence to BSL safety guidelines. Penalty for violations applies.',
    'payment_terms': 'Payments based on approved deliverables and milestones.',
    'penalty_terms': '₹500/day penalty for delays, increasing to ₹1000/day after 2 weeks.',
    'project_milestones': list_to_string([
        '80% of work within first 6 months',
        'Remaining within next 12 months',
        'Final billing upon approval'
    ]),
    'payment_milestones': list_to_string([
        'Minimum billing threshold: 40 units',
        'Final billing: based on approved quantity'
    ]),
    'key_deliverables': list_to_string([
        'User manual', 'System architecture diagram',
        'Training program for operators'
    ])
}

# ✅ Create state for freelancer or company
freelancer_state = AppState(
    freelancer_info=valid_freelancer_info,
    job_analysis=valid_job_analysis
)

company_state = AppState(
    company_info=valid_company_info,
    job_analysis=valid_job_analysis
)

# 🔁 Choose which one to test
test_state = company_state  # or freelancer_state

# 🧪 Invoke proposal writer agent
updated_state = proposal_writer_agent.invoke({"state": test_state})

# 📤 Print output
print("📄 Generated Proposal:\n")
if updated_state['generated_proposal']:
    print(updated_state["generated_proposal"])
else:
    print("❌ Error:", updated_state["error"])
