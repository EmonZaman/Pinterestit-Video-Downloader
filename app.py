from flask import Flask, request
from Pintrest import Pinterest

app = Flask(__name__)

@app.route("/api/download")
def download_video():
    url = request.args.get('url')
    p = Pinterest(url)
    return p.get_media_link()  # Adjusted method name to match the class

if __name__ == "__main__":
    app.run(debug=True)
