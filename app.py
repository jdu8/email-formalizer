import streamlit as st
import openai
import json

with open("key.json") as key_file:
    key = json.load(key_file)

openai.api_key = key["api_key"]

def formalize_email(prompt):
    print(prompt)
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        temperature = 0.2,
        max_tokens = 1000,
        messages = [
            {"role": "user", "content": prompt}
        ]
    )

    return response['choices'][0]['message']['content']

def main():
    st.title("Email Formalizer")

    subject = st.text_input("Enter your Subject:")
    sender = st.text_input("Enter the sender name and greeting")
    content = st.text_area("Enter your email content:", "I wanted to talk about the upcoming meeting. Can we meet tomorrow to discuss the agenda?")
    extra = st.text_area("Enter Additional Context if required:","")

    if st.button("Formalize Email"):
        st.write("Formalized Email:")
        formalized_email = formalize_email(f"Please formalize the following email:\nSubject: {subject}\n{sender},\n{content}\nExtra Context: {extra}")
        st.write(formalized_email)

if __name__ == "__main__":
    main()