Simple QA Chatbot with Gemini 2.0 Flash
Overview
This project is a Streamlit-based chatbot that answers user questions by first searching a local dataset (general_knowledge_qa.csv) using fuzzy string matching. If no relevant answer is found in the dataset, the chatbot falls back to Google's Gemini 2.0 Flash model to generate a response. The app maintains a chat history and displays the source of each answer (dataset or Gemini).
Features

Dataset-Driven Responses: Answers questions using a local CSV dataset with fuzzy matching for approximate question similarity.
Gemini 2.0 Flash Fallback: Queries Gemini 2.0 Flash when the dataset doesn’t have a relevant answer.
Chat History: Persists conversation history during the session using Streamlit’s session state.
User-Friendly Interface: Built with Streamlit for an interactive web-based chat experience.

Prerequisites

Python 3.8 or higher
A Google Gemini API key (obtain from Google AI Studio)
A dataset file named general_knowledge_qa.csv in the QA_dataset folder

Setup Instructions
1. Clone the Repository
If this project is hosted in a repository, clone it to your local machine:
git clone <repository-url>
cd <repository-name>

2. Create a Virtual Environment (Recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies
Install the required Python libraries listed in requirements.txt:
pip install -r requirements.txt

4. Prepare the Dataset

Ensure the QA_dataset folder exists in the project directory.
Place the general_knowledge_qa.csv file inside the QA_dataset folder.
The CSV file should have two columns: question and answer. Example:question,answer
What is the capital of France?,The capital of France is Paris.
How does photosynthesis work?,Photosynthesis is the process by which plants use sunlight to convert carbon dioxide and water into glucose and oxygen.



5. Set Up Environment Variables

Create a .env file in the project directory.
Add your Google Gemini API key:GOOGLE_API_KEY=your_gemini_api_key_here



6. Run the Application
Start the Streamlit app:
streamlit run app.py


Open your browser and go to http://localhost:8501 (or the URL shown in the terminal) to interact with the chatbot.

Usage

Ask a Question: Type your question in the chat input box at the bottom of the page.
View Response: The chatbot will:
First search the dataset for a similar question using fuzzy matching (80% similarity threshold).
If a match is found, it returns the dataset answer.
If no match is found, it queries Gemini 2.0 Flash to generate a response.


Source Attribution: Each response includes the source (dataset or Gemini 2.0 Flash).
Chat History: Previous messages are displayed above the input box.

Example Interaction

User: "What’s the capital of France?"
Chatbot: "The capital of France is Paris. (Source: dataset)"


User: "How tall is the Eiffel Tower?"
Chatbot: "The Eiffel Tower is 324 meters tall. (Source: Gemini 2.0 Flash)" (if not in the dataset)



Project Structure

app.py: Main application script for the Streamlit chatbot.
requirements.txt: List of Python dependencies.
.env: Environment file for storing the Gemini API key (not tracked in version control).
QA_dataset/general_knowledge_qa.csv: Dataset file with question-answer pairs (not included in the repository).

Dependencies
Listed in requirements.txt:

streamlit==1.38.0
pandas==2.2.3
google-generativeai==0.8.2
python-dotenv==1.0.1
thefuzz==0.22.1

Notes

The fuzzy matching threshold (80%) can be adjusted in app.py by modifying the threshold variable in the search_dataset function.
For better fuzzy matching performance, you can optionally install python-Levenshtein:pip install python-Levenshtein


Ensure your Gemini API key is valid and has access to the Gemini 2.0 Flash model.
The dataset must have question and answer columns; otherwise, you’ll need to modify the search_dataset function to match your CSV structure.

Troubleshooting

"Dataset file not found" Error: Ensure QA_dataset/general_knowledge_qa.csv exists in the correct path.
Gemini API Errors: Verify your API key in .env and ensure you have access to Gemini 2.0 Flash.
Module Not Found: Run pip install -r requirements.txt to install all dependencies.

Future Improvements

Use embeddings (e.g., with sentence-transformers) for semantic similarity matching instead of fuzzy string matching.
Stream responses in real-time (e.g., using st.write_stream).
Add support for multiple datasets or dynamic dataset uploads.

License
This project is licensed under the MIT License. See the LICENSE file for details (if applicable).
Author
Created by [Your Name] on April 29, 2025.
# Simple_QA_Chatbot_with_Gemini
