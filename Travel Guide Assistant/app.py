from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv
import os 

load_dotenv()
gemini_api_key = os.getenv('GEMINI_API_KEY')
groq_api_key = os.getenv('GROQ_API_KEY')

system_msg = SystemMessage("You are a travel guide who gives brief recommendations for tourist destinations.")
human_msg = HumanMessage("Suggest top 3 places to visit in Japan.")

messages = [system_msg, human_msg]

model1 = init_chat_model(
    "google_genai:gemini-2.5-flash",
    api_key=gemini_api_key
)

model2 = init_chat_model(
    "groq:llama-3.3-70b-versatile",
    api_key=groq_api_key
)

response1 = model1.invoke(messages)
print("Response from Gemini:\n", response1.content)

response2 = model2.invoke(messages)
print("\nResponse from Groq:\n", response2.content)