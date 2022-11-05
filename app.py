from cProfile import run
from operator import mod
import replicate
from flask import Flask, request
import json

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return "got an api okay"
    if request.method == 'POST':
        # print("i got something")
        # request_data = request.data
        # request_data = json.loads(request_data.decode('utf-8'))
        # prompt = request_data['prompt']
        # model = replicate.models.get("stability-ai/stable-diffusion")
        # output_url = model.predict(prompt=prompt)[0]
        # return {"generated": output_url}
        return "post api detected"


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5000, debug=True)
    app.run()
