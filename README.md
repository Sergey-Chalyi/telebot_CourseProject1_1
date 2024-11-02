# Entertainment Bot

This is a Telegram bot designed to provide various entertainment features such as film, music, and game recommendations, jokes, and an interactive Rock-Paper-Scissors game. Built with Python and the `pyTelegramBotAPI` library, this bot offers an engaging experience for users looking for fun and recommendations.

## Features

- **Welcome Message:** Users are greeted with a welcome message upon starting the bot.
- **Menu Command:** A comprehensive menu displaying available commands.
- **Film Recommendations:** Users can receive random film suggestions.
- **Music Recommendations:** A selection of popular songs is provided.
- **Game Recommendations:** Recommendations for games based on genres.
- **Jokes:** Users can receive a random joke from the `pyjokes` library.
- **Stories:** A collection of interesting short stories is available.
- **Rock-Paper-Scissors Game:** An interactive game where users can play against the bot.

## Requirements

- Python 3.6 or higher

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/entertainment-bot.git
   cd entertainment-bot
   ```

2. Install the required packages using the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory and add your Telegram bot token:

   ```
   TOKEN=your_telegram_bot_token_here
   ```

4. Run the bot:

   ```bash
   python bot.py
   ```

## Usage

- Start the bot by sending the `/start` command.
- Explore the features using the `/menu` command.
- Enjoy recommendations, jokes, and games!

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to create an issue or submit a pull request.