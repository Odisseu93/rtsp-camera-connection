# Conectar câmera via RTSP

Script em Python para conectar câmeras via [RTSP](https://developer.mozilla.org/en-US/docs/Glossary/RTSP) utilizando o módulo [python-vlc](https://python-vlc.readthedocs.io)

## Instalação e exucução

crie o seu ambiente virtual

```bash
python -m venv .venv
```

ative o ambiente:

```bash
# Windows
.\.venv\Scripts\Activate

# macOS/Linux
source .venv/bin/activate
```

configure a URL da sua câmera no arquivo de variáveis de ambiente [.env](.env)

```bash
RTSP_URL="rtsp://admin:admin@192.168.1.1:554/onvif1"
```

na pasta raiz do projeto execute o comando:

```bash
pip install -r requirements.txt
```

execute o script no arquivo `main.py`

```bash
python main.py
```

## Licença

[MIT](LICENSE)
