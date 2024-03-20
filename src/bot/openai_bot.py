import openai
import os
from conf.data import message
from dotenv import load_dotenv
import conf.func

load_dotenv()


def openai_chatbot(s) -> Exception or list[str]:
    openai_key = os.getenv("OPEN_AI_KEY")
    myclient = openai.OpenAI(api_key=openai_key)
    message.append(conf.func.add_user_message(s))

    try:
        response = myclient.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=message,
            temperature=0.1,
        )
        reply = response.choices[0].message.content.split(" ")
        return reply
    except Exception as e:
        print("Error Occured! Check your token")
        return e
