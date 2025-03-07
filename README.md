# PropBot AI

🚀 **PropBot AI** – An AI-powered chatbot that helps businesses generate professional proposals with automated cost estimation and document generation.

## 📌 Project Overview
PropBot AI is a Retrieval-Augmented Generation (RAG) chatbot that assists businesses in creating proposals by:
- Extracting relevant information from a document database (FAQs, past proposals, pricing data, etc.) using **LangChain** and **ChromaDB**.
- Automatically calculating cost estimates from structured data (CSV, Excel) using **Pandas**.
- Generating customized proposals in **DOCX/PDF** formats using **python-docx** and **ReportLab**.
- Providing a user-friendly interface using **Streamlit**.

## 🎯 Key Features
✅ **Context-aware conversation memory** using LangChain's memory components.  
✅ **Real-time cost estimation** using structured pricing data.  
✅ **Proposal document generation** in DOCX and PDF formats.  
✅ **Interactive UI** powered by Streamlit for seamless user experience.  
✅ **AI-driven responses** based on stored business knowledge.  

## 🏗️ Project Architecture
```
📂 PropBot-AI/
│-- 📂 knowledge_base/           # Contains FAQs, proposals, pricing data
│   │-- faqs.json                # Frequently Asked Questions
│   │-- pricing_data.csv         # Pricing details in CSV format
│   │-- pricing_data.xlsx        # Pricing details in Excel format
│   │-- 📂 proposals/             # Past business proposals
│-- 📂 src/                      # Source code for PropBot AI
│   │-- app.py                   # Streamlit app for chatbot UI
│   │-- chatbot.py               # Chatbot logic using LangChain
│   │-- data_loader.py           # Loads data into ChromaDB
│   │-- proposal_generator.py    # Generates proposal documents
│-- requirements.txt             # Dependencies for the project
│-- README.md                    # Project documentation
```

## 🔧 Installation & Setup
1. **Clone the Repository**  
   ```bash
   git clone https://github.com/arghads9177/prop-bot-ai.git
   cd prop-bot-ai
   ```

2. **Create a Virtual Environment** (Recommended)  
   ```bash
   conda create -p venv python==3.13
   conda activate venv/
   source env/bin/activate   # On Windows use: env\Scripts\activate
   ```

3. **Install Dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit App**  
   ```bash
   streamlit run src/app.py
   ```

## 🛠️ Technologies Used
- **LangChain** – Context retrieval and AI-powered chatbot
- **ChromaDB** – Vector database for storing and retrieving knowledge
- **OpenAI API** – LLM for generating responses
- **Streamlit** – Web UI for user interaction
- **python-docx & ReportLab** – Document generation (DOCX/PDF)
- **Pandas** – Data processing for pricing calculations

## 📖 Usage Guide
- Enter your business requirements in the chatbot.
- The bot retrieves relevant information from FAQs, past proposals, and pricing data.
- It calculates estimated costs based on structured pricing.
- Generates a customized business proposal in **DOCX/PDF format**.
- Download and share the proposal with clients.

## 🛠 Future Enhancements
- Integration with **GPT-4** for improved proposal writing.
- **Multi-language support** for international clients.
- **User authentication** to save and manage proposals.
- **API support** for integrating PropBot AI with third-party apps.

## 🤝 Contributing
Contributions are welcome! Feel free to fork this repo, create a feature branch, and submit a PR.

## 📜 License
This project is licensed under the **GNU Open License**.

---
Made with ❤️ by [Argha Dey Sarkar](https://github.com/arghads9177/)

