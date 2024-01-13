from flask import Flask, render_template, request
from Pintrest import Pintrest
from base64 import b64decode

app = Flask(__name__)

@app.route("/api/download")
def downloadVideo():
    url = request.args.get('url')
    p = Pintrest(url)
    return p.get_media_Link()   


if __name__ == "__main__":
    app.run(debug=True)