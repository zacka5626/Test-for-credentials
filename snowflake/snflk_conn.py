import snowflake.connector

# Snowflake connection parameters
conn = snowflake.connector.connect(
    user='Dev_infra',
    #password='eyJraWQiOiI5MjAzNDkyMTU5NTA4NjM4IiwiYWxnIjoiRVMyNTYifQ.eyJwIjoiMTQwNDM0MTQ3ODYxOjE0MDQzNDE0NTY2OSIsImlzcyI6IlNGOjEwNDMiLCJleHAiOjE3NTE0NTU2MjR9.BDtPnrEbgUKGZezHZ4rvJi0BsROaWyLlmKInIszO385eEPsBCXKWP9KT7P-wkB_04HjuffIMgrGcZsYuxMGLfQ',
    private_key_file='C:\\Users\\amit.mathur\\Dev_infra_Private_key.p8',
    private_key_file_pwd='Dev_infra$*^#1267',
    account='rpb68119.us-east-1'  # e.g., abcd-xy12345.east-us-2.azure
    #warehouse='YOUR_WAREHOUSE',
    #database='YOUR_DATABASE',
    #schema='YOUR_SCHEMA'
)

try:
    # Create a cursor object
    cursor = conn.cursor()

    # Execute a simple query
    #cursor.execute("SELECT * FROM TALKPUSH.DBO.TBLTALKPUSHCANDIDATEINFO  LIMIT 10")
    cursor.execute("SELECT current_date")

    # Fetch and print the results
    for row in cursor.fetchall():
        print(row)

finally:
    # Close the cursor and connection
    cursor.close()
    conn.close()
