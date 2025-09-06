import telegram
from telegram import bot
import requests
import time
import imghdr



BOT_TOKEN = "8431098641:AAFHkabBirjMG6MINm9xz5M5WxLuETrb3iM"
CHAT_ID = "-4984490758"
SERVER_URL = "https://teste.com"

bot = telegram.Bot(token=BOT_TOKEN)

def check_server_status():
    #Verifica o status do servidor
    try:
        response = requests.get(SERVER_URL, timeout=5)
        # 200 = online
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        print(f"Erro ao tentar conectar: {e}")
        return False

"""
def check_server_status():
    #Simula o status do servidor, alternando entre online e offline.
    global is_online_simulated # Declara a variável global
    
    # Se a variável ainda não existe, crie-a com o valor True
    if 'is_online_simulated' not in globals():
        is_online_simulated = True
        
    # Inverte o valor do status a cada chamada
    is_online_simulated = not is_online_simulated
    
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Status simulado: {'Online' if is_online_simulated else 'Offline'}")

    return is_online_simulated
"""
# O bot só alerta a troca de status.
def main():
    """Loop principal para monitorar o servidor."""
    is_online = check_server_status()
    print(f"Status inicial do servidor: {'Online' if is_online else 'Offline'}")

    while True:
        time.sleep(60)
        current_status = check_server_status()

        if not current_status and is_online:
            # O servidor estava online e agora está offline.
            message = f"🚨 ALERTA: O servidor em {SERVER_URL} parece estar OFFLINE!"
            bot.send_message(chat_id=CHAT_ID, text=message)
            print(message)
            is_online = False
        elif current_status and not is_online:
            # O servidor estava offline e agora voltou.
            message = f"✅ O servidor em {SERVER_URL} voltou a ficar ONLINE!"
            bot.send_message(chat_id=CHAT_ID, text=message)
            print(message)
            is_online = True

if __name__ == "__main__":
    main()