# Streamlit Chat Application with SQL Database

## Overview

This Streamlit application is designed to facilitate chat interactions with a SQL database using a Large Language Model (LLM). The application allows users to interact with the database through a chat interface powered by Streamlit. It utilizes Python 3.10.12 for its backend functionality.

## Features

- Chat interface powered by Streamlit
- Integration with a SQL database
- Utilizes a Large Language Model for natural language processing
- Python 3.10.12 backend

## Requirements

- Python 3.10.12
- Streamlit
- SQL database (e.g., MySQL, SQLite, PostgreSQL)

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/your-repo.git
   cd your-repo
   ```

2. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Create a `.streamlit` folder in the root directory if it does not exist.

4. Create a `secrets.toml` file inside the `.streamlit` folder.

5. Add the following keys and their corresponding values to the `secrets.toml` file:

   ```toml
   db_user = ""
   db_password = ""
   db_host = ""
   db_name = ""
   semicolons_gateway_api_key = ""
   semicolons_gateway_base_url = ""          
   openai_api_key = ""
   ```

   Make sure to replace the empty strings with your actual credentials and API keys.

## Configuration

1. Ensure that you have a SQL database set up and accessible from your environment.
2. Update the database connection details in the configuration file (`config.py` or similar).

## Usage

1. Navigate to the project directory.
2. Run the Streamlit application:

   ```
   streamlit run app.py
   ```

3. Access the application through your web browser at the specified URL.

## Usage Tips

- Ensure that your SQL database is properly configured and accessible from the application.
- Interact with the chat interface using natural language queries and commands.
- Monitor the application logs for any errors or issues encountered during runtime.


## Acknowledgments

- Thanks to the Streamlit team for providing a powerful tool for building interactive web applications with Python.
- Special thanks to the Python community for their continuous support and contributions.