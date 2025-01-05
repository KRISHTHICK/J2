
from dotenv import load_dotenv
load_dotenv() ##To load all env variables
#import google.cloud.aiplatform as aiplatform
import streamlit as st
import os
import google.generativeai as genai
#GOOGLE_API_KEY=""
GOOGLE_API_KEY=""

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

##Func to load gemini pro model and get response
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])
def get_gemini_response(question):

    response=chat.send_message(question,stream = True)  
    return response

## initialize our streamlit app

st.set_page_config(page_title="Simple QA Demo") 

st.header("Gemini LLM Application 2025J")

#Initialize  session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history']=[]

input=st.text_input("Input: ",key="input")
submit=st.button("Ask the Question")

if submit and input:
    response=get_gemini_response(input)
    ## Add user query and response to session state chat history
    st.session_state['chat_history'].append(("You",input))
    st.subheader("The response we got is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot",chunk.text))
st.subheader("The Chat History of 2025J is")

for role,text in st.session_state['chat_history']:st.write(f"{role}:{text}")
 
# 
# from dotenv import load_dotenv
# import streamlit as st
# import os
# import google.generativeai as genai

# # Load environment variables
# load_dotenv()

# # Configure Generative AI
# api_key = os.getenv("GOOGLE_API_KEY")
# if not api_key:
#     st.error("API key not found! Make sure your .env file is set up correctly.")
# else:
#     #genai.configure(api_key='GOOGLE_API_KEY')
#     genai.configure(api_key='GOOGLE_API_KEY')
# # Function to load gemini-pro model and get response
# try:
#     model = genai.GenerativeModel("gemini-pro")
#     chat = model.start_chat(history=[])
# except Exception as e:
#     st.error(f"Error initializing the model: {e}")

# def get_gemini_response(question):
#     try:
#         response = chat.send_message(question, stream=True)
#         return response
#     except Exception as e:
#         st.error(f"Error fetching response: {e}")
#         return []

# # Initialize Streamlit app
# st.set_page_config(page_title="Simple QA Demo")
# st.header("Gemini LLM Application 2025J")

# # Initialize session state for chat history if it doesn't exist
# if "chat_history" not in st.session_state:
#     st.session_state["chat_history"] = []

# # User input and button
# input = st.text_input("Input: ", key="input")
# submit = st.button("Ask the Question")

# if submit and input:
#     response = get_gemini_response(input)
#     # Add user query and response to session state chat history
#     st.session_state["chat_history"].append(("You", input))
#     st.subheader("The response we got is:")
#     for chunk in response:
#         st.write(chunk.text)
#         st.session_state["chat_history"].append(("Bot", chunk.text))

# # Display chat history
# st.subheader("The Chat History of 2025J is:")
# for role, text in st.session_state["chat_history"]:
#     st.write(f"{role}: {text}")
