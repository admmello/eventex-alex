# Eventex

Sistema de eventos encomendado pela Morena


[![Build Status](https://travis-ci.org/admmello/eventex-alex.svg?branch=master)](https://travis-ci.org/admmello/eventex-alex)


## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.5
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env
6. Execute os testes.

```console
git clone https://github.com/admmello/eventex-alex.git
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer deploy?

1. Crie uma instancia no heroku.
2. Envie as configurações para o heroku.
3. Define um SECRET_KEY segura para instancia.
4. Defina DEBUG=False
5. Configure o serviço de email.
6. Envie o código para o heroku.

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
# configura o e-mail
git push heroku master --force 
```