# FURIA CHATBOT

Chatbot para os fãs de Counter-Strike da FURIA, oferecendo informações sobre o time.

## 📋 Visão Geral

O FURIA Chatbot é um bot para Telegram desenvolvido em Python que fornece informações sobre a equipe brasileira de Counter-Strike FURIA. O bot responde a comandos específicos, permitindo aos fãs consultar informações sobre o elenco atual, ranking mundial, títulos conquistados, história da equipe e mais.

## 🚀 Funcionalidades

O bot responde aos seguintes comandos:

- /start - Mensagem de boas-vindas e lista de comandos disponíveis
- /elenco - Mostra o elenco atual da FURIA CS
- /agenda - Exibe o próximo jogo da equipe
- /ranking - Mostra a posição atual da FURIA no ranking mundial (HLTV)
- /titulos - Lista os principais títulos conquistados pela equipe
- /recordes - Exibe os recordes da FURIA
- /historia - Conta a história da FURIA
- /redes - Fornece informações das redes sociais
- /comandos - Lista todos os comandos disponíveis


## 📦 Requisitos

O projeto utiliza as seguintes dependências:

- python-telegram-bot (v22.0): Framework para criar bots do Telegram
- python-dotenv (v1.1.0): Para gerenciar variáveis de ambiente
- httpx (v0.28.1): Cliente HTTP para Python
- Outros pacotes auxiliares

## ⚙️ Configuração e Instalação

1. *Clone o repositório:*

   
   git clone https://github.com/PedroVella/furia_chatbot.git
   cd furia_chatbot
   

2. *Instale as dependências:*

   
   pip install -r requirements.txt
   

3. *Configure as variáveis de ambiente:*

   Crie um arquivo .env na raiz do projeto com a seguinte variável:

   
   TELEGRAM_TOKEN=digite aqui seu token do telegram
   

   Para obter um token, converse com o [@BotFather](https://t.me/BotFather) no Telegram.

4. *Execute o bot:*
   
   python -m bot.main
   

## 👨‍💻 Como Contribuir

1. Faça um fork do projeto
2. Crie uma branch para sua feature (git checkout -b feature/nova-funcionalidade)
3. Commit suas mudanças (git commit -m 'Adiciona nova funcionalidade')
4. Push para a branch (git push origin feature/nova-funcionalidade)
5. Abra um Pull Request


## 📞 Contato

opedro.vella@gmail.com
