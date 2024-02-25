
import os, streamlit as st
import openai

# Uncomment to specify your OpenAI API key here (local testing only, not in production!), or add corresponding environment variable (recommended)
# os.environ['OPENAI_API_KEY']= ""

from sqlalchemy import create_engine, text
from llama_index import SQLDatabase
import tiktoken
from llama_index.callbacks import CallbackManager, TokenCountingHandler
from llama_index import ServiceContext, LLMPredictor, OpenAIEmbedding, PromptHelper
from llama_index.llms import OpenAI
from llama_index import ServiceContext
from llama_index.indices.struct_store.sql_query import NLSQLTableQueryEngine


db_user = st.secrets["db_user"]
db_password = st.secrets["db_password"]
db_host = st.secrets["db_host"]
db_name = st.secrets["db_name"]

connection_string = f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}"


# Define a simple Streamlit app
st.markdown("""
    <style>
        .reportview-container {
            margin-top: -2em;
        }
        #MainMenu {visibility: hidden;}
        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        #stDecoration {display:none;}
    </style>
""", unsafe_allow_html=True)

st.title("Ask Finance AI")
query = st.text_input("What would you like to ask? ", "")

# If the 'Submit' button is clicked
if st.button("Submit"):
    if not query.strip():
        st.error(f"Please provide the search query.")
    else:
        try:
            # This example uses text-davinci-003 by default; feel free to change if desired
            engine = create_engine(connection_string)

            # sql_database = SQLDatabase(engine, include_tables=tables,sample_rows_in_table_info=5)
            sql_database = SQLDatabase(engine, sample_rows_in_table_info=2)

            token_counter = TokenCountingHandler(
                tokenizer=tiktoken.encoding_for_model("gpt-3.5-turbo").encode
            )

            callback_manager = CallbackManager([token_counter])

            model = "gpt-35-turbo-16k"

            openai.api_key = st.secrets["openai_api_key"]
            llm = OpenAI(temperature=0.1, model="gpt-3.5-turbo")

            # llm = OpenAI(
            #     model=model,
            #     api_key=gateway_api_key,
            #     api_base=gateway_base_url, # api_base represents the endpoint the Llama-Index object will make a call to when invoked
            #     temperature=0.1
            # )
            
            service_context = ServiceContext.from_defaults(
                llm=llm,callback_manager=callback_manager
            )


            query_engine = NLSQLTableQueryEngine(
                sql_database=sql_database,
                service_context=service_context
            )
        
            response = query_engine.query(query)
            st.success(response)
            print(response)
        except Exception as e:
            st.error(f"An error occurred: {e}")