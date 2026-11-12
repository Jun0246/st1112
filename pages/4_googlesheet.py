import streamlit as st
import pandas as pd

st.title("구글 시트 연동")

gsid= st.secrets["gsid"]
url = f"https://docs.google.com/spreadsheets/d/{gsid}/export?format=csv&gid=0"

data = pd.read_csv(url)
st.dataframe(data)
# 문항 1,2,3 만들기
question1 = data.iloc[0, 1]
answer1 = st.text_input("")
question2 = data.iloc[1, 1]
question3 = data.iloc[2, 1]

st.write(question1)
st.write(question2)
st.write(question3)