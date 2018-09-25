# conjugame_api
Sanic api used to get proper conjugation of verb given context


$ python3.6 -m pip install -r requirements.txt

$ python3.6 main.py

$ curl -d '{"context": ["Eu preciso","a mesa"], "verb": "pôr"}' 'http://0.0.0.0:8000/conjugate'
