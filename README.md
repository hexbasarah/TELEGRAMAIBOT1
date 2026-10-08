# 🤖 Telegram AI Bot

An AI-powered Telegram bot built with **Python** that can answer questions, explain programming concepts, and interact with users directly through Telegram.

The bot uses the **Google Gemini API** to generate intelligent responses and **pyTelegramBotAPI (TeleBot)** to communicate with Telegram users.

## ✨ Features

* 💬 Answers users' questions using AI
* 🤖 Powered by Google Gemini
* 🐍 Built with Python
* 📚 Can explain programming concepts
* ⚡ Responds directly inside Telegram
* 🔄 Handles multiple user messages
* 🔐 Uses environment variables for API keys
* 🛠️ Simple structure that can be extended with more features

## 🛠️ Technologies Used

* **Python 3**
* **Google Gemini API**
* **pyTelegramBotAPI (TeleBot)**
* **python-dotenv**
* **Telegram Bot API**

## 📂 Project Structure

```text
telegrambot/
│
├── bot.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

> Your filenames may be different. If your main Python file has another name, replace `bot.py` with your actual filename.

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Hexbasarah/telegrambot.git
```

Move into the project folder:

```bash
cd telegrambot
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install the required packages

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt` file yet, you can install the main packages with:

```bash
pip install pyTelegramBotAPI google-generativeai python-dotenv
```

## 🔑 Setting Up API Keys

You need two API keys:

1. **Telegram Bot Token**
2. **Google Gemini API Key**

### Telegram Bot Token

Create your Telegram bot using **BotFather** on Telegram and copy the bot token provided to you.

### Gemini API Key

Create an API key from Google AI Studio.

Create a `.env` file in your project folder:

```env
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
GEMINI_API_KEY=your_gemini_api_key
```

⚠️ **Never upload your `.env` file or API keys to GitHub.**

Add this to your `.gitignore`:

```text
.env
venv/
__pycache__/
```

## ▶️ Running the Bot

After setting up your API keys, run:

```bash
python bot.py
```

If everything is configured correctly, your bot should start running and waiting for messages.

Open Telegram, find your bot, and send a message.

## 💬 Example

**User:**

```text
What is Python?
```

**Bot:**

```text
Python is a high-level programming language
used for web development, automation, data analysis,
artificial intelligence, and many other applications.
```

The bot can also be used to ask programming-related questions such as:

```text
Explain Python functions.
```

```text
What is a variable in Python?
```

```text
How does a for loop work?
```

## 🎯 Purpose of the Project

I created this project to improve my skills in:

* Python programming
* APIs and API integration
* Telegram bot development
* Artificial intelligence
* Prompt-based AI applications
* Debugging and problem solving
* Building practical Python projects

## 🔮 Future Improvements

Some features I plan to add include:

* 🧠 Conversation memory
* 🎙️ Voice message support
* 📄 File and document analysis
* 🖼️ Image understanding
* 👤 User authentication
* 📊 Usage tracking
* 🌐 Web search capabilities
* ⚙️ More advanced AI tools

## 🧑‍💻 Author

**Peter Sarah Wuwuda**

Chemical Engineering Student | Python Developer | AI Enthusiast

📍 Nigeria

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

---

### 📌 Disclaimer

This project is created for educational and portfolio purposes. API usage may be subject to the terms, limits, and pricing of the services used.
