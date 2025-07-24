import streamlit as st
import snowflake.connector
from snowflake.connector.errors import ProgrammingError

# Snowflake connection parameters - replace with your credentials or use secrets management
SNOWFLAKE_ACCOUNT = "your_account"
SNOWFLAKE_USER = "your_username"
SNOWFLAKE_PASSWORD = "your_password"
SNOWFLAKE_WAREHOUSE = "your_warehouse"
SNOWFLAKE_DATABASE = "your_database"
SNOWFLAKE_SCHEMA = "your_schema"

def run_query(query):
    try:
        ctx = snowflake.connector.connect(
            user=SNOWFLAKE_USER,
            password=SNOWFLAKE_PASSWORD,
            account=SNOWFLAKE_ACCOUNT,
            warehouse=SNOWFLAKE_WAREHOUSE,
            database=SNOWFLAKE_DATABASE,
            schema=SNOWFLAKE_SCHEMA,
        )
        cs = ctx.cursor()
        cs.execute(query)
        results = cs.fetchall()
        columns = [desc[0] for desc in cs.description]
        cs.close()
        ctx.close()
        return columns, results
    except ProgrammingError as e:
        return None, f"Query error: {e}"
    except Exception as e:
        return None, f"Error: {e}"

def main():
    st.title("Snowflake Chatbot")
    st.write("Interact with your Snowflake data using natural language queries or SQL.")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_input = st.text_input("Enter your query or command:")

    if st.button("Send"):
        if user_input:
            st.session_state.chat_history.append({"user": user_input})
            # For simplicity, treat user input as SQL query
            columns, results = run_query(user_input)
            if columns is None:
                st.session_state.chat_history.append({"bot": results})
            else:
                # Format results as a table string
                result_str = ""
                if results:
                    result_str += "| " + " | ".join(columns) + " |\n"
                    result_str += "| " + " | ".join(["---"] * len(columns)) + " |\n"
                    for row in results:
                        result_str += "| " + " | ".join(str(cell) for cell in row) + " |\n"
                else:
                    result_str = "No results found."
                st.session_state.chat_history.append({"bot": result_str})

    for chat in st.session_state.chat_history:
        if "user" in chat:
            st.markdown(f"**You:** {chat['user']}")
        else:
            st.markdown(f"**Bot:**\n{chat['bot']}")

if __name__ == "__main__":
    main()
