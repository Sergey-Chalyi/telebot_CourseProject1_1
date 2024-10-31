import os
import random
import pyjokes
import telebot
from telebot import types
from dotenv import load_dotenv

load_dotenv()

bot = telebot.TeleBot(os.getenv("TOKEN"))

@bot.message_handler(commands=['start'])
def start_command(message: types.Message):
    welcome_text = (
        "Hello! Welcome to the entertainment bot. "
        "To see all the features of this bot, enter the /menu command."
    )
    bot.send_message(message.chat.id, welcome_text)

@bot.message_handler(commands=['menu'])
def bot_menu(message: types.Message):
    menu_text = (
        "Here are the available commands:\n"
        "/menu - Show this menu\n"
        "/give_films - Get film recommendations\n"
        "/give_music - Get music recommendations\n"
        "/give_games - Get game recommendations by genre\n"
        "/give_jokes - Get a joke\n"
        "/give_stories - Get an interesting story\n"
        "/play_game - Play 'Rock-Paper-Scissors' game\n"
    )
    bot.send_message(message.chat.id, menu_text)

@bot.message_handler(commands=['give_films'])
def give_films(message: types.Message):
    films = (
        "Here are some recommended films:\n"
        "- Inception\n"
        "- The Shawshank Redemption\n"
        "- The Godfather\n"
        "- Interstellar\n"
        "- Parasite\n"
    )
    bot.send_message(message.chat.id, films)

@bot.message_handler(commands=['give_music'])
def give_music(message: types.Message):
    music = (
        "Here are some recommended songs:\n"
        "- 'Bohemian Rhapsody' by Queen\n"
        "- 'Blinding Lights' by The Weeknd\n"
        "- 'Imagine' by John Lennon\n"
        "- 'Stairway to Heaven' by Led Zeppelin\n"
        "- 'Smells Like Teen Spirit' by Nirvana\n"
    )
    bot.send_message(message.chat.id, music)

@bot.message_handler(commands=['give_games'])
def give_games(message: types.Message):
    games = (
        "Here are some recommended games by genre:\n"
        "Action: 'The Witcher 3: Wild Hunt'\n"
        "Adventure: 'The Legend of Zelda: Breath of the Wild'\n"
        "Strategy: 'Civilization VI'\n"
        "Role-playing: 'Elden Ring'\n"
        "Puzzle: 'Portal 2'\n"
    )
    bot.send_message(message.chat.id, games)

@bot.message_handler(commands=['give_jokes'])
def give_jokes(message: types.Message):
    joke = pyjokes.get_joke(language="en")
    bot.send_message(message.chat.id, joke)

@bot.message_handler(commands=['give_stories'])
def give_stories(message: types.Message):
    stories = [
        "Once upon a time in a small village, there lived a young girl who could talk to animals. One day, she discovered a hidden forest where animals gathered to share their secrets. This magical place changed her life forever.",
        "In a faraway kingdom, a brave knight set off on a quest to find a lost treasure. After many adventures and challenges, he learned that the true treasure was the friends he made along the way.",
        "A curious scientist invented a machine that could see into the future. What he discovered changed his perspective on life and taught him to cherish the present moment.",
        "In a bustling city, a street artist painted murals that brought joy to everyone who saw them. One day, a famous art critic stumbled upon his work, leading to an unexpected turn of events.",
        "A young boy found a mysterious book in his attic. Each page he turned transported him to a different world filled with adventure, magic, and endless possibilities."
    ]

    story = random.choice(stories)  # Randomly select a story from the list
    bot.send_message(message.chat.id, story)

@bot.message_handler(commands=['play_game'])
def play_game(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Rock", "Paper", "Scissors"]
    markup.add(*buttons)
    bot.send_message(message.chat.id, "Let's play Rock-Paper-Scissors! Please choose: Rock, Paper, or Scissors.", reply_markup=markup)

    # Set the user to the next step for guessing
    bot.register_next_step_handler(message, process_user_choice)

def process_user_choice(message: types.Message):
    if message.content_type != 'text':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ["Rock", "Paper", "Scissors"]
        markup.add(*buttons)
        bot.send_message(message.chat.id, "Invalid input! Please enter Rock, Paper, or Scissors as text.")
        bot.register_next_step_handler(message, process_user_choice)
        return

    choices = ["Rock", "Paper", "Scissors"]
    user_choice = message.text.strip()

    if user_choice not in choices:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ["Rock", "Paper", "Scissors"]
        markup.add(*buttons)
        bot.send_message(message.chat.id, "Invalid choice! Please choose Rock, Paper, or Scissors.", reply_markup=markup)
        bot.register_next_step_handler(message, process_user_choice)
        return


    # Generate a random choice for the bot
    bot_choice = random.choice(choices)

    # Determine the winner
    if user_choice == bot_choice:
        result = "It's a tie!"
    elif (user_choice == "Rock" and bot_choice == "Scissors") or \
         (user_choice == "Paper" and bot_choice == "Rock") or \
         (user_choice == "Scissors" and bot_choice == "Paper"):
        result = "You win! 🎉"
    else:
        result = "I win! 😢"

    bot.send_message(message.chat.id, f"You chose: {user_choice}" + "\n" + f"I chose: {bot_choice}" + "\n" + result)

@bot.message_handler(content_types=['text', 'audio', 'voice', 'photo', 'video', 'document', 'location', 'sticker', 'contact'])
def handle_all_messages(message: types.Message):
    bot.send_message(message.chat.id, "Please call a command.\n /menu")


if __name__ == "__main__":
    bot.polling(none_stop=True)
