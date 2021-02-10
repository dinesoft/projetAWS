
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def dashboard(name):
    return 'welcome %s' % name


@app.route('/index', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['name']
        print(user)
        return render_template('index.html')
    else:
        user = request.args.get('name')
        return render_template('index.html')


if __name__ == "__main__":
    app.run(host='localhost', port=3000)
