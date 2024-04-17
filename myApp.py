from flask import Flask

app = Flask(__name__)
app.secret_key = "SUPER_SECRET_KEY"


@app.route('/')
@app.route('/home')
def home():
    return 'this is my home page'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
