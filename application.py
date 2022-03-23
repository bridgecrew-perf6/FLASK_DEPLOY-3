from flask import Flask

application = app = Flask(__name__)

@application.route("/")
def index():
    return "<body bgcolor=blue><p><font color=red:q!>Hello Oleksii Saiun.version3.1</font></p></body>"

if __name__ == "__main__":
    application.debug = True
    application.run()
