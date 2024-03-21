def openai_chatbot(s) -> Exception or list[str]:
    import openai
    import os
    from src.bot.conf.data import message
    from dotenv import load_dotenv
    import src.bot.conf.func

    load_dotenv()
    openai_key = os.getenv("OPEN_AI_KEY")
    myclient = openai.OpenAI(api_key=openai_key)
    message.append(src.bot.conf.func.add_user_message(s))
    # print(message)
    try:
        response = myclient.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=message,
            temperature=0.1,
        )
        reply = response.choices[0].message.content.split(" ")
        # print(reply)
        return reply
    except Exception as e:
        print("Error Occured! Check your token")
        return e
