from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

from utils import csv_to_train_data


def train_with_corpus(bot, corpus_path):
    """
    Trains the bot with YAML or JSON data
    """
    print(f'Starting training with: {corpus_path}')
    corpus_trainer = ChatterBotCorpusTrainer(bot)
    corpus_trainer.train(corpus_path)
    print(f'Finished training with: {corpus_path}')


def train_with_csv(bot, csv_path, bot_col=1, user_col=0):
    """
    Trains the bot with CSV data
    """
    print(f'Starting training with: {csv_path}')
    conversation = csv_to_train_data(csv_path, bot_col, user_col)
    trainer = ListTrainer(bot)
    i = 0
    while i < len(conversation):
        trainer.train([conversation[i], conversation[i + 1]])
        i += 2
    print(f'Finished training with: {csv_path}')
