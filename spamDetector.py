import streamlit as st
import pickle
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from win32com.client import Dispatch
import pandas as pd


def speak(text):
	speak=Dispatch(("SAPI.SpVoice"))
	speak.Speak(text)


model = pickle.load(open('spam.pkl','rb'))
cv=pickle.load(open('vectorizer.pkl','rb'))

def main():
	st.title(":green[Email/SMS Spam Detection]")
	st.subheader("Built with Streamlit & Python using :blue[Naive Bayes Classifier]")
	activites=["Classification","About"]
	choices=st.sidebar.selectbox("Select Activities",activites)
	
	if choices=="Classification":
		st.subheader(":violet[Classification]")
		msg=st.text_input("Enter a text")
		if st.button("Process"):
			print(msg)
			print(type(msg))
			data=[msg]
			print(data)
			vec=cv.transform(data).toarray()
			result=model.predict(vec)
			if result[0]==0:
				st.success("This is Not A Spam Email/SMS",icon="✅")
				speak("This is Not A Spam Email/SMS")
				st.metric(label="HAM", value="95% SAFE", delta="GOOD")
				st.snow()
			else:
				st.error("This is A Spam Email/SMS",icon="🚨")
				speak("This is A Spam Email/SMS")
				st.metric(label="SPAM", value="-25% SAFE", delta="-BAD")
	if choices=="About":
		st.text("_________________________")
		st.write(":dark[_Developed by_]")
		st.subheader(":red[YASHWANTH] & TEAM :sunglasses:")
		st.markdown('Under the guidance of **:blue[Gouthamm Sir]**.')
		st.snow()

		
		

main()



