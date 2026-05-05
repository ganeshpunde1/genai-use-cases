# !pip install huggingface_hub
from langchain_huggingface import HuggingFaceEndpoint


llm = HuggingFaceEndpoint(repo_id="google/flan-t5-large", temperature=0.7, max_new_tokens=64)
# name = llm.predict("I want to open a restaurant for Chinese food. Suggest a fency name for this.")
name = llm.invoke("I want to open a restaurant for Indian food. Suggest a fancy name for this.")

print(name)