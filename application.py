from flask import Flask

application = app = Flask(__name__)

@application.route("/")
def index():
    return "<p><font color=black>Hello Oleksii Saiun.version3</font></p>"

if __name__ == "__main__":
    application.debug = True
    application.run()