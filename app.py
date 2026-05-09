# Import the OpenAI LLM wrapper from LangChain's OpenAI integration
from langchain_openai import OpenAI
# Import ChatPromptTemplate to structure system + user messages															   
from langchain_core.prompts import ChatPromptTemplate
# Import output parser to convert model output into a clean string																  
from langchain_core.output_parsers import StrOutputParser
# Import Streamlit for building the web UI										  
import streamlit as st

# Import dotenv to load environment variables from .env file															
from dotenv import load_dotenv
import os
from dotenv import load_dotenv
# Load environment variables from the .env file into the environment																	
load_dotenv()

##env variables call
# -------------------------------
# Load API keys from environment
# -------------------------------

# Set OpenAI API key from .env file into environment variable															 
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

## Langsmith tracking
# Set LangSmith API key for LangChain tracing/monitoring
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Enable LangChain tracing (V2)							   
os.environ["LANGCHAIN_TRACING_V2"] = "true"
# Set LangChain project name for grouping traces												
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")

##creating chatbot
# -------------------------------
# Create the chatbot prompt
# -------------------------------

# Define a structured prompt with system + user messages														
prompt=ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Answer the question as best as you can. If you don't know the answer, say you don't know.  Keep the answer concise and to the point."),
    ("user", "Question : {question}")
])

#streamlit framework
# -------------------------------
# Streamlit UI
# -------------------------------

# Set the title of the Streamlit web app										
st.title("ChatMate - Your AI Chatbot")
# Create a text input box for the user to type a question														 
user_input = st.text_input("Ask a question:")

#openai llm call
# -------------------------------
# Initialize the OpenAI LLM
# -------------------------------

# Create an OpenAI model instance with parameters
llm = OpenAI(
    model="gpt-3.5-turbo",      # Model name
    temperature=0.7,            # Creativity level
    max_tokens=1500,            # Max output length
    top_p=1.0,                  # Sampling parameter
    frequency_penalty=0.0,      # Penalize repeated phrases
    presence_penalty=0.0        # Encourage new topics
)

# Create an output parser to convert model output into plain text
output_parser=StrOutputParser()

##chain call
# -------------------------------
# Build the LangChain pipeline
# -------------------------------

# Chain = prompt → LLM → output parser
chain=prompt | llm | output_parser

# -------------------------------
# Run the chain when user submits input
# -------------------------------

# If the user typed something, generate and display the answer															  
if user_input:
    st.write("Answer: ", chain.invoke({'question': user_input}))
