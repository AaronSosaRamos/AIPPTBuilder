from langchain_core.output_parsers import JsonOutputParser
from app.api.features.schemas.schemas import PPTFileSchema
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import GoogleGenerativeAI
from app.api.logger import setup_logger

import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

logger = setup_logger(__name__)

parser = JsonOutputParser(pydantic_object=PPTFileSchema)

model = GoogleGenerativeAI(model="gemini-1.5-pro")

def read_text_file(file_path):
    # Get the directory containing the script file
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Combine the script directory with the relative file path
    absolute_file_path = os.path.join(script_dir, file_path)
    
    with open(absolute_file_path, 'r') as file:
        return file.read()

prompt = PromptTemplate(
  template=read_text_file('prompts/generate-ppt-prompt.txt'),
  input_variables=[
    "topic",
    "objective",
    "target_audience",
    "n_slides",
    "slide_breakdown",
    "lang",
    "summary"
  ],
  partial_variables={"format_instructions": parser.get_format_instructions()}
)

def compile_chain():
    logger.info("Compiling chain...")
    chain = prompt | model | parser
    logger.info("Chain is compiled successfully")
    return chain