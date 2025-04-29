import streamlit as st
import pandas as pd
import os
import google.generativeai as genai
from dotenv import load_dotenv
from thefuzz import fuzz

# Load environment variables from .env file
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure Gemini API
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Ask me anything! I'll check my dataset first, then use Gemini 2.0 Flash if needed."}]

# Load dataset
@st.cache_data
def load_dataset():
    try:
        df = pd.read_csv("QA_dataset/general_knowledge_qa.csv")  # Updated path from previous request
        return df
    except FileNotFoundError:
        st.error("Dataset file not found. Please ensure 'QA_dataset/general_knowledge_qa.csv' exists.")
        return pd.DataFrame(columns=["question", "answer"])

# Function to search dataset for an answer using fuzzy matching
def search_dataset(query, df):
    query = query.lower().strip()
    best_match = None
    highest_score = 0
    threshold = 80  # Similarity threshold (0-100)

    for index, row in df.iterrows():
        dataset_question = row["question"].lower().strip()
        # Calculate similarity score using fuzzy matching
        score = fuzz.token_sort_ratio(query, dataset_question)
        if score > highest_score:
            highest_score = score
            best_match = row["answer"]

    # Return the best match if similarity score exceeds threshold
    if highest_score >= threshold:
        return best_match
    return None

# Function to get response from Gemini 2.0 Flash
def get_gemini_response(query):
    try:
        model = genai.GenerativeModel("gemini-2.0-flash")
        response = model.generate_content(query)
        if response.candidates and response.candidates[0].content.parts:
            return response.candidates[0].content.parts[0].text
        return "Sorry, I couldn't generate a response from Gemini."
    except Exception as e:
        return f"Error with Gemini API: {str(e)}"

# Streamlit app setup
st.title("Simple QA chatbot with Gemini 2.0 Flash")
st.caption("Powered by a local dataset and Google's Gemini 2.0 Flash")

# Display chat history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Load dataset
df = load_dataset()

# Chat input
if prompt := st.chat_input("Ask a question:"):
    # Add user message to session state
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # Search dataset for answer using fuzzy matching
    dataset_answer = search_dataset(prompt, df)

    if dataset_answer:
        # Answer found in dataset
        response = dataset_answer
        source = "dataset"
    else:
        # Fallback to Gemini 2.0 Flash
        response = get_gemini_response(prompt)
        source = "Gemini 2.0 Flash"

    # Add assistant response to session state
    st.session_state.messages.append({"role": "assistant", "content": f"{response} (Source: {source})"})
    st.chat_message("assistant").write(f"{response} (Source: {source})")