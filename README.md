# conjugame_api
Sanic api used to get proper conjugation of verb given context

## Setup
$ python3.6 -m pip install -r requirements.txt


## Local Dev
$ python3.6 main.py

$ curl -d '{"context": ["Eu preciso","a mesa"], "verb": "pôr"}' 'http://0.0.0.0:8000/conjugate'

$ docker run -d -p 8000:80 --name webserver conjugame


## Deployment
$ sudo docker build -t conjugame .

$ docker run -d -p 8000:80 --name webserver conjugame
