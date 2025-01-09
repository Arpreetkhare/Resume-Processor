import openai
import pdfplumber
import os
from openai.error import RateLimitError
from dotenv import load_dotenv


load_dotenv()



openai.api_key = os.getenv("OPENAI_API_KEY")



# Function to extract text from PDF using pdfplumber

"""
    pdf_path : pdf from which extracting info.

"""
def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""

        """ 
            test as empty and incremented as data extratcted.
        """
        for page in pdf.pages:
            text += page.extract_text()
    return text

# Function to send resume text to OpenAI for parsing

def parse_resume_with_openai(resume_text):
    messages = [
        {"role": "system", "content": "You are a resume parser. Extract the candidate's first name, email, and mobile number from the given text."},
        {"role": "user", "content": f"Resume: {resume_text}"}
    ]
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=500,
            temperature=0
        )
        print("OpenAI Response:", response)
        content = response['choices'][0]['message']['content']
        print(f' contect : {content}')
        return str(content.strip())
    
    
    except RateLimitError:
        # Handle quota exhaustion
        return {"error": "API quota exceeded. Please try again later."}