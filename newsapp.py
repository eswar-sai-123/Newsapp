import streamlit as st 
import smtplib
from email.mime.text import MIMEText
from gnewsclient import gnewsclient
from email.mime.multipart import MIMEMultipart


st.title(""" Top News directly to your Email""")
language = st.selectbox('Select language:', ['telugu','english', 'hindi', 'french'])
topic = st.selectbox('Select topic:', ['top news', 'world', 'nation', 'business', 'technology', 'entertainment', 'sports', 'science'])
num_of_news = st.number_input("Enter Number of news")
location = st.selectbox("Enter the location",["India", "USA","Russia"])
email_to = st.text_input("Enter email")

def news(lang,topic,max_number_of_topic,loca):
    client = gnewsclient.NewsClient(
        language=lang,
        topic=topic,
        location=loca,
        max_results=int(max_number_of_topic)

    )
    li_st = []
    cl_news = client.get_news()
    for i in cl_news:
        news_item = ""
        for x,y in i.items():
            if x == "media":
                continue
            else:
                news_item += f"{x}: {y}\n"
        li_st.append(news_item)
    return "\n".join(li_st) 

def send_email(lis,email_to):
    from_email = "20je0672@ap.iitism.ac.in"
    from_password = "123456789"

    messsage = MIMEMultipart()
    messsage["From"] = from_email 
    messsage["To"]   = email_to
    messsage["Subject"] = "Top Stories"

    body = "\n".join(lis)
    messsage.attach(MIMEText(body, 'plain'))
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, from_password)
    server.sendmail(from_email, email_to, messsage.as_string())
    server.quit() 


if st.button('Send News'):
    if email_to:
        news_list = news(language, topic, num_of_news, location).split('\n')
        send_email(news_list, email_to)
        st.success('Email sent successfully!')
    else:
        st.error('Please enter a valid email address.')
