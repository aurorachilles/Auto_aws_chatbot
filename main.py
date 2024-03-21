from src.bot.openai_bot import openai_chatbot
from src.aws.create import create_ec2



def main():
    while True:
        print("")
        print("---------------------Welcome to Auto AWS Chatbot---------------------")
        imp = input("What Can I do for you?:")
        chatbot_reply = openai_chatbot(imp)
        if chatbot_reply[0].lower() == 'error':
            print("Error Try Again!")
            continue
        create_ec2(chatbot_reply)

        if input("Do you want to launch another instance? (y/n):").lower() == 'n':
            break
        else:
            continue
    print("---------------------Thank you for using!---------------------")


if __name__ == "__main__":
    main()
