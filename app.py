import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from io import BytesIO
import markdown2
import weasyprint
import os
from dotenv import load_dotenv
from html2docx import html2docx

# Load environment variables
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

def generate_proposal(proposal_type, about_you, job_requirements):
    """Generates a proposal using OpenAI's GPT-4o model via LangChain."""
    if not about_you.strip():
        return "Please provide details about yourself or your business."
    if not job_requirements.strip():
        return "Please enter the job requirements."
    
    prompt_templates = {
        "Freelancing Proposal": PromptTemplate(
            input_variables=["about_you", "job_requirements"],
            template=(
                "You are an expert freelancing proposal writer. Generate a professional freelancing proposal from the following freelancer details and job requirement in Markdown format. "
                "Freelancer Details: {about_you}\n"
                "Job Requirements: {job_requirements}\n"
                "If freelancer details like background, skills, or experience are missing, return an appropriate message asking for them. "
                "If job requirements are unclear, request clarification. "
                "Otherwise, ensure the output follows this exact format: \n\n"
                "# Freelancing Proposal\n"
                "*Freelancer: {about_you}* | Email: *[Your Email]* | M: *[Your Contact Number]* | Website: *[Portfolio/Website Link]*\n\n"
                "**Proposal for:** {job_requirements}\n"
                "**Prepared By:** {about_you}\n"
                "**Date:** [Proposal Date]\n\n"
                "## 1. Introduction\n"
                "Dear **{job_requirements}**,\n\n"
                "I am excited about the opportunity to collaborate on **[Project Name]**. "
                "With **[X years]** of experience in **[your field, e.g., web development, content writing, digital marketing, etc.]**, "
                "I am confident in my ability to deliver high-quality results that align with your vision.\n\n"
                "## 2. About Me\n"
                "I am a **[your role, e.g., full-stack developer, UX designer, SEO specialist]** with a strong background in **[mention relevant skills/technologies]**.\n"
                "Over the years, I have successfully completed **[X+]** projects for clients across **[countries/industries]**, helping businesses achieve **[mention key results]**.\n\n"
                "### Why Work With Me?\n"
                "- **[Key Strength 1]**  [Brief description]\n"
                "- **[Key Strength 2]**  [Brief description]\n"
                "- **[Key Strength 3]** [Brief description]\n\n"
                "## 3. Understanding Your Needs\n"
                "Based on your project description, I understand that you require:\n"
                "- **[Project Requirement 1]** [How you will fulfill this need]\n"
                "- **[Project Requirement 2]** [How you will fulfill this need]\n"
                "- **[Project Requirement 3]** [How you will fulfill this need]\n\n"
                "## 4. Proposed Approach & Work Plan\n"
                "- **Phase 1:** [Task] - [Expected Outcome] - [Timeframe]\n"
                "- **Phase 2:** [Task] - [Expected Outcome] - [Timeframe]\n"
                "- **Phase 3:** [Task] - [Expected Outcome] - [Timeframe]\n\n"
                "## 5. Deliverables\n"
                "- **[Deliverable 1]** [Brief description]\n"
                "- **[Deliverable 2]** [Brief description]\n"
                "- **[Deliverable 3]** [Brief description]\n\n"
                "## 6. Timeline & Availability\n"
                "I am available to start **immediately / from [start date]**, and I estimate that the project will take **[X weeks/days]** to complete.\n\n"
                "- **Project Kickoff:** [Start Date]\n"
                "- **Milestone 1 Completion:** [Date]\n"
                "- **Final Delivery & Review:** [Date]\n\n"
                "## 7. Pricing & Payment Terms\n"
                "**Total Project Cost:** $[Total Cost]\n\n"
                "**Payment Schedule:**\n"
                "- **[Milestone 1]:** $[Amount]  Due upon [Task Completion]\n"
                "- **[Milestone 2]:** $[Amount] Due upon [Task Completion]\n"
                "- **[Final Payment]:** $[Amount] Due upon project delivery\n\n"
                "## 8. Why Choose Me?\n"
                "- **100% Client Satisfaction** Proven track record with [X]+ 5-star reviews.\n"
                "- **Expert in [Skillset]** Years of experience in [Your Field].\n"
                "- **Results-Driven** Focused on delivering measurable impact.\n"
                "- **Timely Revisions & Support** Ensuring client satisfaction throughout the project.\n\n"
                "## 9. Next Steps\n"
                "If you’re ready to move forward, let’s discuss your project further. I am available for a quick call or chat at your convenience.\n\n"
                "**Schedule a Call:** [Your Scheduling Link]\n"
                "**Email Me:** {about_you}\n"
                "**Call Me:** {about_you}\n\n"
                "Looking forward to working with you and bringing your project to life!\n\n"
                "Best regards,\n"
                "{about_you}\n"
                "[Your Freelance Role, e.g., Web Developer, Copywriter, Graphic Designer]\n"
                "Website:{about_you}\n"
                "Note the following point while generating the proposal:\n"
                "- After 'Prepared By:' add name of the freelancer only. Don't add other details about the freelancer. If name is not present add placeholder [Freelancer Name].\n"
                "- After 'Freelancer Details:' add name of the freelancer only. Don't add other details about the freelancer. If name is not present add placeholder [Freelancer Name]."
                "- After 'Proposal for:' add name of the project only. Don't add other details about the project. If name is not present add placeholder [Project Name]."
                "- After 'Website:' add the link to the freelancer's portfolio or website. Don't add other details about the freelancer. If Website is not present add placeholder [Portfolio/Website Link]."
                "- After 'Email Me:**' add the email of the freelancer. Don't add other details about the freelancer. If email is not present add placeholder [Your Email]."
                "- After 'Call Me:**' add the phone number of the freelancer. Don't add other details about the freelancer. If phone number is not present add placeholder [Your Contact Number]."
                "- After 'Dear **' add name of the client only. Don't add other details about the project. If name is not present add placeholder [Client Name]."
            ),
        ),
        "Business Proposal": PromptTemplate(
            input_variables=["about_you", "job_requirements"],
            template=(
                "You are an expert business proposal writer. Generate a professional business proposal from the following business details and job requirement in Markdown format. "
                "Business Details: {about_you}\n"
                "Job Requirements: {job_requirements}\n"
                "If business details like description, achievements, or experience are missing, return an appropriate message asking for them. "
                "If job requirements are unclear, request clarification. "
                "Otherwise, Ensure the output follows this exact format: \n\n"
                "# Business Proposal\n"
                "**Prepared For:** [Client Name]\n"
                "**Prepared By:** {about_you}\n"
                "**Date:** [Proposal Date]\n\n"
                "## 1. Executive Summary\n"
                "This proposal outlines how {about_you} can provide [specific service or product] to [Client Name]. "
                "Our expertise in [industry/sector] allows us to deliver [key benefits], ensuring efficiency, cost-effectiveness, and high-quality results.\n\n"
                "## 2. About Us\n"
                "### Who We Are\n"
                "{about_you} is a [years of experience]-year-old company specializing in [your services/products]. "
                "We have successfully served [number] clients across [regions/countries] and are committed to delivering excellence.\n\n"
                "### Our Mission & Vision\n"
                "- *Mission:* To provide [primary goal/service] with [unique value proposition].\n"
                "-*Vision:* To become the leading provider of [industry-specific service] globally.\n\n"
                "### Our Competitive Edge\n"
                "- [Key strength 1] - [Brief description]\n"
                "- [Key strength 2] - [Brief description]\n"
                "- [Key strength 3] - [Brief description]\n\n"
                "## 3. Services Offered\n"
                "### [Service 1]\n"
                "- *Description:* [Brief details of the service]\n"
                "- *Benefits:*"
                "   - [Benefit 1]\n"
                "   - [Benefit 2]\n"
                "   - [Benefit 3]\n\n"
                "### [Service 2]\n"
                "- *Description:* [Brief details of the service]\n"
                "- *Benefits:*\n"
                "   - [Benefit 1]\n"
                "   - [Benefit 2]\n"
                "   - [Benefit 3]\n\n"
                "## 4. Proposed Solution\n"
                "- **Step 1:** [Outline the first step of implementation]\n"
                "- **Step 2:** [Outline the second step]\n"
                "- **Step 3:** [Outline the third step]\n\n"
                "## 5. Project Timeline\n"
                "- **Phase 1:** [Task] - [Timeframe] - [Expected Outcome]\n"
                "- **Phase 2:** [Task] - [Timeframe] - [Expected Outcome]\n"
                "- **Phase 3:** [Task] - [Timeframe] - [Expected Outcome]\n\n"
                "## 6. Pricing & Payment Terms\n"
                "**Total Cost:** $[Total Cost]\n"
                "**Payment Schedule:**\n"
                "- **[Milestone 1]:** $[Amount] due on [Date]\n"
                "- **[Milestone 2]:** $[Amount] due on [Date]\n"
                "- **[Final Payment]:** $[Amount] upon completion\n\n"
                "## 7. Why Choose Us?\n"
                "- **Proven Track Record** Over [number] satisfied clients.\n"
                "- **Innovative Solutions** Cutting-edge technology & strategies.\n"
                "- **Industry Expertise** Experienced professionals in [industry].\n"
                "- **Measurable ROI** Guaranteed growth & efficiency.\n\n"
                "## 8. Terms & Conditions\n"
                "- The proposal is valid for [X] days from the date issued.\n"
                "- A formal contract must be signed before commencement.\n"
                "- Payment terms as agreed must be followed.\n"
                "- Intellectual property rights & confidentiality clauses apply.\n\n"
                "## 9. Next Steps\n"
                "**Schedule a Meeting:** [Your Scheduling Link]\n"
                "**Email Us:** [Your Email Address]\n"
                "**Call Us:** [Your Phone Number]\n\n"
                "Sincerely,\n"
                "{about_you}\n"
                "Note the following point while generating the proposal:\n"
                "- After 'Prepared By:' add name of the company.\n"
                "- After 'Sincerely,' add name of the company only in the next line. Don't add other details about the company."
            ),
        ),
    }

    llm = ChatOpenAI(model_name="gpt-4o")
    prompt = prompt_templates[proposal_type]
    chain = prompt | llm
    response = chain.invoke({"about_you": about_you, "job_requirements": job_requirements})
    return response.content.strip()

# Convert Markdown to DOCX
def get_docx(proposal):
    """Converts Markdown to DOCX using html2docx"""
    docx_stream = BytesIO()

    # Convert Markdown to HTML first
    html_content = markdown2.markdown(proposal)

    # Convert HTML to DOCX
    docx_bytes = html2docx(html_content, "Proposal")

    # Write to BytesIO
    docx_stream.write(docx_bytes.getvalue())
    docx_stream.seek(0)

    return docx_stream

# Convert Markdown to PDF Using WeasyPrint
def get_pdf(proposal):
    html_content = markdown2.markdown(proposal)
    pdf_stream = BytesIO()
    
    # Convert HTML to PDF
    pdf = weasyprint.HTML(string=html_content).write_pdf()
    pdf_stream.write(pdf)
    pdf_stream.seek(0)

    return pdf_stream

# Streamlit UI
def main():
    st.set_page_config(page_title="PropBot AI - Proposal Generator", layout="centered")
    proposal_type = st.sidebar.radio("Select Proposal Type:", ["Freelancing Proposal", "Business Proposal"], index=0)
    st.title("🚀 PropBot AI - Proposal Generator")
    st.subheader(proposal_type)
    
    about_you = st.text_area("About You:" if proposal_type == "Freelancing Proposal" else "About Your Business:", "", help="Describe your background, skills, and experience" if proposal_type == "Freelancing Proposal" else "Describe your business, achievements, and experience")
    job_requirements = st.text_area("Job Requirements:", "", help="Paste the job requirements you’re applying for")
    
    if "proposal" not in st.session_state:
        st.session_state.proposal = ""
    
    if st.button("Generate Proposal"):
        if "proposal" not in st.session_state:
            st.session_state.proposal = ""
        with st.spinner("Generating proposal..."):
            st.session_state.proposal = generate_proposal(proposal_type, about_you, job_requirements)
    
    if st.session_state.proposal:
        st.write(markdown2.markdown(st.session_state.proposal), unsafe_allow_html=True)
    
        col1, col2 = st.columns(2)
        with col1:
            st.download_button("Download as DOCX", get_docx(st.session_state.proposal), "proposal.docx", "application/vnd.openxmlformats-officedocument.wordprocessingml.document")
        with col2:
            st.download_button("Download as PDF", get_pdf(st.session_state.proposal), "proposal.pdf", "application/pdf")

if __name__ == "__main__":
    main()