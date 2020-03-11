from flask import Flask

app = Flask(__name__)

@app.route("/")
def hell0_world():
  return "HelloWorld"

if __name__ == '__main__':
    app.run()
