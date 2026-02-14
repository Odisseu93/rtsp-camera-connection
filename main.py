import vlc
import time
from dotenv import load_dotenv
import os

load_dotenv()

# --- COLE AQUI O ENDEREÇO RTSP DA SUA CÂMERA ---
rtsp_url = os.getenv("RTSP_URL")

# ------------------------------------------------
instance = vlc.Instance("--network-caching=300")
player = instance.media_player_new()
media = instance.media_new(rtsp_url)
player.set_media(media)
player.play()

print("Assistindo... Pressione Ctrl+C para parar.")
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    player.stop()