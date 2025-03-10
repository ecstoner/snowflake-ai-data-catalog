import os
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

# Load environment variables (OpenAI API Key)
load_dotenv()

# Initialize a model via LangChain
# Alternatives: 
# llm = HuggingFaceLLM(model_name="gpt2")                               -- from langchain.llms import HuggingFaceLLM
# llm = CohereLLM(api_key=os.getenv("COHERE_API_KEY"), model="medium")  -- from langchain.llms import CohereLLM
# llm = AI21LLM(api_key=os.getenv("AI21_API_KEY"), model="j1-large")    -- from langchain.llms import AI21LLM
llm = ChatOpenAI(
    model_name="gpt-4",
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

# Define the prompt template
prompt_template = PromptTemplate(
    input_variables=["table_name", "column_name", "data_type", "sample_data"],
    template=(
        "Provide a concise but detailed description for the column '{column_name}' "
        "in the '{table_name}' table. The data type is {data_type}, and example values include: {sample_data}. "
        "Explain what this column likely represents in a database used for analytical queries."
    )
)

def generate_column_description(table_name, column_name, data_type, sample_data):
    """
    Generates an AI-powered description for a given column based on table context and sample data.

    Args:
    - table_name (str): The name of the table.
    - column_name (str): The name of the column.
    - data_type (str): The column's data type (e.g., STRING, INT).
    - sample_data (list): A small set of example values from the column.

    Returns:
    - str: A human-readable column description.
    """
    # Format the prompt with the given data
    prompt = prompt_template.format(
        table_name=table_name,
        column_name=column_name,
        data_type=data_type,
        sample_data=sample_data
    )

    # Generate the description using OpenAI's GPT-4 model
    response = llm.predict(prompt)
    return response
