
import os
GROQ_API_KEY = '' # @param {type:"string"}
HUGGING_FACE_TOKEN = '<HUGGING_FACE_TOKEN>' # @param {type:"string"}
# GROQ_API_KEY 
print(GROQ_API_KEY)
# Get your API Key from https://console.groq.com/keys
os.environ['GROQ_API_KEY'] = GROQ_API_KEY
print(os.environ['GROQ_API_KEY'])
os.environ['GRAPHRAG_API_KEY'] = 'DUMMY_KEY'
# If gated LLM
os.environ['HUGGING_FACE_TOKEN'] = HUGGING_FACE_TOKEN

if len(os.getenv("GROQ_API_KEY"))<25:
    assert False, "is required. Sign up and Get your API Key from https://console.groq.com/keys"
# print(os.getenv('REDDIT_NAME'))
