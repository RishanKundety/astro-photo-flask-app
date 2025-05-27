from flask import Flask, render_template
import random

app = Flask(__name__)

# List of valid cat image URLs (should be direct image links)
images = [
    "https://photos.app.goo.gl/EFj341GqiU39JPvz6"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
