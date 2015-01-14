from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
  return 'Hello World!'

@app.route('/bye')
def goodbye():
  return '<H1>Bye World!<H1>'

@app.route('/tree')
def tree():
  return 'oak'

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
