from service import create_bot, start
from train import train_with_csv

# create the bot
bot = create_bot()

# train
# train_with_corpus(bot, 'chatterbot.corpus.english.greetings')
train_with_csv(bot, './data/mental_health_faq.csv')

# start the bot
start(bot)
