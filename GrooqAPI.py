
# from groq import Groq
# Free alternatives you can use instead:

# Google Gemini API - has a free tier

# Get key at https://aistudio.google.com/apikey
# pip install google-generativeai

# from google import genai

# client = genai.Client(api_key="AIzaSyBB1FMxeiujceCwc2Swt7AekO9BAljBS8c")
# response = client.models.generate_content(
#     model="gemini-2.0-flash",
#     contents="write a haiku about ai"
# )
# print(response.text)

# Groq's free tier doesn't expire based on time. Instead it has rate limits:
# Requests per minute (RPM): 30
# Requests per day (RPD): 14,400
# Tokens per minute (TPM): 6,000
# So as long as you stay within these limits, your free API key will keep working indefinitely. The limits reset every minute/day automatically.
# Check current limits at https://console.groq.com/docs/rate-limits
# Groq - free tier with fast inference
# Get key at https://console.groq.com
from groq import Groq
import configparser

def get_property(key):
    config = configparser.ConfigParser()
    config.read("config.properties")
    return config["DEFAULT"][key]

# usage
# print(get_property("GROQ_API_KEY"))

client = Groq(api_key=get_property("GROQ_API_KEY")) # Groq API key, get it at https://groq.com/
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role": "user", "content": "How to learn AI?"}]
)
print(response.choices[0].message.content)




# pip install google-generativeai
# python '.\Google Gemini API.py'
