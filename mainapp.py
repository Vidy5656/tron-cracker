import telebot

# Create bot instance with token
bot = telebot.TeleBot("6286224911:AAFkwjC8VmNk0or1JktqeyDDsdC1E4GFwis")

# Define markup for main menu
markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
markup.row("Charge Account", "Create Account", "View Account")

# Define markup for account types
account_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
account_markup.row("VMess", "VLESS", "Trojan")

# Define markup for vmess types
vmess_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
vmess_markup.row("Vmess-xtls", "Vmess-grcp", "Vmess-tcp")

# Define start command handler
@bot.message_handler(commands=['start'])
def start_command_handler(message):
    bot.send_message(message.chat.id, "Welcome to the all-purpose robot for selling VPN account on V2. Please use the option below to use the features, with this robot you will not need everything.", reply_markup=markup)

# Define create account handler
@bot.message_handler(func=lambda message: message.text == "Create Account")
def create_account_handler(message):
    bot.send_message(message.chat.id, "Please select an account type:", reply_markup=account_markup)

#Define create vmess handler
@bot.message_handler(func=lambda message:message.text == "VMess")
def create_vmess_handler(message):
    bot.send_message(message.chat.id, "please choice your vmess types", reply_markup=vmess_markup)
    
@bot.message_handler()    
def keyboard(message):
    if message.text == "Vmess-xtls":
        bot.send_message(message.chat.id, "trojan://Bfl4wDI1wu@earthquke.lightspeed.best:2087?security=tls&type=tcp#Trojan.XTLS")  
    elif message.text == "Vmess-grcp":  
        bot.send_message(message.chat.id, "vless://18637290-5dca-4479-e232-cb37592cfd5d@188.121.120.35:2083?mode=gun&security=none&encryption=none&type=grpc&serviceName=#EarthQuake.vless.grcp")
# Start polling for new messages
bot.infinity_polling()

