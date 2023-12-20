import streamlit as st
import random
import time

st.title("Text2query chat")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Text question"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        if prompt == 'Show name, country, age for all singers ordered by age from the oldest to the youngest.':
            assistant_response = 'SELECT name, country, age FROM singer ORDER BY age DESC;'
        elif prompt == 'What is the average, minimum, and maximum age of all singers from France?':
            assistant_response = "SELECT avg(age) ,  min(age) ,  max(age) FROM singer WHERE country  =  'France';"
        elif prompt == 'Show the stadium name and the number of concerts in each stadium.':
            assistant_response = 'SELECT T2.name ,  count(*) FROM concert AS T1 JOIN stadium AS T2 ON T1.stadium_id  =  T2.stadium_id GROUP BY T1.stadium_id;'
        # Simulate stream of response with milliseconds delay
        for chunk in assistant_response.split():
            full_response += chunk + " "
            time.sleep(0.05)
            # Add a blinking cursor to simulate typing
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})
