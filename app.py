import streamlit as st
import pickle
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import string

nltk.download('punkt_tab')
nltk.download('stopword
ps = PorterStemmer()
vector = pickle.load(open("vectorizer.pkl","rb"))
model = pickle.load(open("model.pkl","rb"))


def datapreprocesiing(text):
    text = text.lower()  #convert text into lower case
    text = nltk.word_tokenize(text) #text to token
    y=[]
    for i in text:
        if i.isalnum():  #remove special chracteres
            y.append(i)
    text = y[:]
    y.clear()

    for i in text: #to remove punctutaion and stopwords
        if i not in stopwords.words("english") and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))
    return " ".join(y)






st.title("Email/SMS Spam Classifier")

message= st.text_input("Enter your message.")
if st.button("predict"):

    text = datapreprocesiing(message)

        # 2 vectorize the data
    vector_input = vector.transform([text]).toarray()

        # 3 predict


    result = model.predict(vector_input)[0]

    if result == 1:
            st.header("Enter message is spam")
    else:
            st.header("Enter message is not spam")
#4 display


