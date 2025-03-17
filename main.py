import telebot
from llama_cpp import Llama

# Замените на ваш токен
TOKEN = ' TOKEN '

# Инициализация бота
bot = telebot.TeleBot(TOKEN)

# Загрузка модели
model_path = "/content/drive/MyDrive/DeepSeek-V2-Lite-Chat.Q2_K.gguf"
llm = Llama(model_path=model_path)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот с моделью DeepSeek. Задайте мне вопрос.")

# Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    user_input = message.text
    # Генерация ответа с использованием модели
    response = llm(user_input, max_tokens=100)
    bot.reply_to(message, response['choices'][0]['text'])

# Запуск бота
bot.polling()

