from src.bot.openai_bot import openai_chatbot
import src.bot

def main():
    imp = input("What should i do for you?:")

    lis = openai_chatbot(imp)
    print(lis)

if __name__ == "__main__":
    main()
