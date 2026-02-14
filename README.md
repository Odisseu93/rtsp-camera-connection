# Conectar câmera via RTSP

Script em Python para conectar câmeras via [RTSP](https://developer.mozilla.org/en-US/docs/Glossary/RTSP) utilizando o módulo [python-vlc](https://python-vlc.readthedocs.io).

## Pré-requisitos

- Python 3.8 ou superior
- [VLC media player](https://www.videolan.org/vlc/) instalado no sistema (necessário para o `python-vlc`)
- pip atualizado

> ⚠️ **Observação:** O VLC deve estar instalado e acessível pelo PATH do sistema. Caso esteja no Windows, verifique se o caminho do VLC (`C:\Program Files\VideoLAN\VLC`) está incluído nas variáveis de ambiente.

## Instalação

1. Crie o seu ambiente virtual:

```bash
python -m venv .venv
```

2. Ative o ambiente virtual:

```bash
# Windows
.\.venv\Scripts\Activate

# macOS/Linux
source .venv/bin/activate
```

3. Atualize o pip para a versão mais recente:

```bash
pip install --upgrade pip
```

4. Instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

## Configuração da câmera

1. Crie um arquivo `.env` na raiz do projeto com a URL da sua câmera:

```env
RTSP_URL="rtsp://admin:admin@192.168.1.1:554/onvif1"
```

> Substitua `admin:admin` pelo usuário e senha corretos da sua câmera e `192.168.1.1:554/onvif1` pelo endereço RTSP correspondente.

## Execução

No ambiente virtual ativo, execute o script principal:

```bash
python main.py
```

Se tudo estiver correto, o script irá conectar e exibir o stream da sua câmera.

## Licença

[MIT](LICENSE)
