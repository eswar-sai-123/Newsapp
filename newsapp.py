from gnewsclient import gnewsclient
import streamlit as st 

def news(lang,topic,max_number_of_topic,loca):
    client = gnewsclient.NewsClient(
        language=lang,
        topic=topic,
        location=loca,
        max_results=max_number_of_topic

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



language = input("Enter: \n")
topic = input("Enter: \n ")
maximum = int(input("Enter : \n"))
loca  = input("Enter: \n")

print(news(language,topic,maximum,loca))
