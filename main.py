#!/usr/bin/env python3

import json as json_lib
import urllib.parse


from sanic import Sanic, request, response
from sanic.exceptions import abort
from sanic.response import json, text
from typing import Dict
from sanic_cors import CORS, cross_origin
from inflect.conjugate import VerbConjugator

app = Sanic()
CORS(app)

@app.route('/conjugate', methods=['POST', 'OPTIONS'])
async def post_endpoint(request: request) -> response:
    try:
        ret = await inflect(json_lib.loads(request.body.decode('utf8')))
    except Exception as e:
        abort(400)
        text(str(e))

    return response.json({"conjugated_verb": ret}, status=200)

async def inflect(body: Dict) -> str:
    if not valid_post_body(body):
        return ValueError("Post called with invalid body")
    before, after = body['context']
    verb = body['verb']
    conjugator = VerbConjugator(beforere, verb, after)
    return conjugator.conjugate_verb()

def valid_post_body(body: Dict) -> bool:
    return 'context' in body and 'verb' in body and len(body["context"]) == 2

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
