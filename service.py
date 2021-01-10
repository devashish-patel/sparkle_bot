from chatterbot import ChatBot

BOT_NAME = 'Sparkle'
BYE_LIST = [
    'bye',
    'exit',
    'e',
]


def create_bot():
    """
    Creates the chat bot
    """
    bot = ChatBot(BOT_NAME,
                  storage_adapter='chatterbot.storage.SQLStorageAdapter',
                  logic_adapters=[{
                      'import_path': 'chatterbot.logic.BestMatch',
                      'default_response':'I am sorry, but I do not understand. '
                      'Please visit https://gratitude07.wixsite.com/website',
                      'maximum_similarity_threshold': 0.90
                  }])
    return bot


def start(bot):
    """
    Starts and take responses from the chat bot
    """
    print(f'Hello, I am {BOT_NAME}. Ask me about mental health.')

    while True:
        user_input = input("me: ")
        if user_input.lower() in BYE_LIST:
            print(f'{BOT_NAME}: Good bye and have a blessed day!')
            break

        response = bot.get_response(user_input)
        print(f'{BOT_NAME}:', response)
