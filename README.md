# AI-Agents-Newsletter-Crew-2.0

An AI-powered content generation pipeline featuring OpenAI LLMs, Exa API for real-time web search, and a Streamlit-based GUI. Automates the process of researching, writing, and editing newsletters with seamless collaboration between AI agents.

---

## Features
- **Streamlit-Based GUI**: Interactive interface for effortless newsletter generation.
- **Research Agent**: Uses the Exa API to fetch and summarize relevant web content.
- **Writer Agent**: Creates markdown-formatted articles based on research.
- **Editor Agent**: Refines the content for clarity, structure, and professionalism.
- **Sequential Workflow**: Ensures seamless collaboration between agents for high-quality output.
- **Customizable Templates**: Modify the HTML structure and design of newsletters.
- **Output Files**: Saves newsletters as downloadable HTML files.

---

## Technologies Used
- **CrewAI**: Manages AI agents and task execution.
- **DeepSeek-R1-distill-llama-70b**: Uses State of the Art LLM via Groq API
- **LangChain**: Integrates language models for content processing.
- **Streamlit**: Provides a web-based UI for user interaction.
- **Exa API**: Fetches and processes real-time news data.

## Installation
1. **Clone the Repository**  
   ```
   git clone https://github.com/your-username/AI-Agents-Newsletter-Crew-2.0.git
   cd AI-Agents-Newsletter-Crew-2.0
   ```

2. **Create and Activate a Virtual Environment**  
   - On Windows:  
     ```
     python -m venv venv
     venv\Scripts\activate
     ```
   - On macOS/Linux:  
     ```
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install Dependencies**  
   ```
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**  
   - Create a `.env` file in the root directory and add your API keys:
     ```
     EXA_API_KEY=your_exa_api_key
     GOOGLE_API_KEY=your_google_api_key
     ```

## Usage
### 1. Run the Web Application
   ```
   streamlit run app.py
   ```
   - Enter a topic and a personal message in the UI.
   - Click "Generate Newsletter" to start the process.
   - Download the generated newsletter as an HTML file.

### 2. Run from Command Line
   ```
   python main.py
   ```
   - Enter the topic and personal message when prompted.
   - The generated newsletter will be saved as an HTML file.

## Troubleshooting
- **Issue**: Dependencies missing  
  - **Solution**: Run `pip install -r requirements.txt` to install required libraries.
- **Issue**: API key errors  
  - **Solution**: Ensure the `.env` file contains valid API keys.
- **Issue**: Streamlit UI not loading  
  - **Solution**: Verify that `streamlit` is installed and that no other process is using the assigned port.
- **Issue**: Newsletter output is empty  
  - **Solution**: Check if the research agent retrieved valid news articles.
