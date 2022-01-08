# kevin marquart initial lør. 8. jan. 23.22
from flask import Flask
from views import views

app = Flask(__name__)
app.register_blueprint(views, url_prefix="/home")


if __name__ == "__main__":
    app.run(debug=True)
