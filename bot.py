#######################################################################
########################### MADE BY MARCO #############################
#######################################################################

import requests, time
import telegram, telepot

### Parte do Telegram Package
token = 'SEU_TOKEN'
bot = telegram.Bot(token)
chat_id = 'SEU_CHAT'

telebot = telepot.Bot('SEU_TOKEN')
telechat = ('SEU_CHAT')

boasvindas = ("Olá, estou Online novamente! \n" + "Lembrando a todos que: Por mais que eu seja bom no que faço, meu sistema não é 100% preciso. Portanto, NÃO NOS RESPONSABILIZAMOS por qualquer dano." + "\n \n" + "Developed by Fuzzy ;)")

telebot.sendMessage(telechat, boasvindas)


### Começa o ciclo de anuncio
while True:

    url = 'https://blaze.com/api/roulette_games/recent'

    response = requests.get(url)

    retorno = response.json()

    ray = []

    for x in range(len(retorno)):
        val = retorno[x]['color']
        if val == 1:
            val = 'Vermelho'

        if val == 2:
            val = 'Preto'

        if val == 0:
            val = 'Branco'

        ray.append(val)

    print(ray)

    def resultado(num):

        timer = 30

        if num[0:4] == ['Preto', 'Vermelho', 'Vermelho', 'Vermelho']:

            msg = '''✅ GREEN no ⚫'''
            mensagem = bot.send_message(chat_id=chat_id, text=msg)
            time.sleep(timer)
            

        elif num[0:4] == ['Vermelho', 'Vermelho', 'Vermelho', 'Vermelho']:

            text = '''✅ LOSS'''
            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(timer)

        elif num[0:3] == ['Vermelho', 'Vermelho', 'Vermelho']:

            text = '''✅ Entrada confirmada, entrar no ⚫
                      Cuidado com o ⚪'''
            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(timer)

        elif num[0:2] == ['Vermelho', 'Vermelho']:

            text = '''✅ Possivel entrada no ⚫
                Cuidado com o ⚪'''
            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(timer)

        elif num[0:4] == ['Vermelho', 'Preto', 'Preto', 'Preto']:

            text = '''✅ GREEN no 🔴'''
            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(timer)

        elif num[0:4] == ['Preto', 'Preto', 'Preto', 'Preto']:

            text = '''✅ LOSS'''
            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(timer)

        elif num[0:3] == ['Preto', 'Preto', 'Preto']:

            text = '''✅ Entrada confirmada, entrar no 🔴
                   Cuidado com o ⚪'''
            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(timer)

        elif num[0:2] == ['Preto', 'Preto']:

            text = '''✅ Possivel entrada no 🔴
                 Cuidado com o ⚪ '''
            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(timer)

        elif num[0:2] == ['Branco', 'Vermelho', 'Branco']:

            text = '''✅ Possivel Triple ⚪
                    Cuidado com o ⚫ '''
            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(timer)

    resultado(ray)

    time.sleep(5)
