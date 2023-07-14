import streamlit as st
import pickle

tfidf = pickle.load(open("vectorizer.pkl", "rb"))
model = pickle.load(open("model.pkl", "rb"))

st.title("Email Spam Classifier")

input_mail = [st.text_area("Enter the message")]

if st.button("Predict"):
    transformed_sms = tfidf.transform(input_mail)
    result = model.predict(transformed_sms)
    print(result,input_mail[0])

    if result[0] == 1:
        st.header("Not Spam")
    else:
        st.header("Spam")

    am = 'ham' if result == 0 else 'spam'
    
    file = open('logs.txt', 'a')
    line = f"\n{am},{input_mail[0]}"
    file.write(line)
    file.close()

if st.button("🍵"):
    st.subheader("©️Code Slayers")
