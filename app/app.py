from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the DevSecOps Pipeline!"

@app.route('/vuln')
def vuln():
    return "<input type='text' name='username'>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
