from flask import Flask
from config import Config
from controllers.home_controller import home

app = Flask(__name__)
app.config.from_object(Config)

# Enregistrer les blueprints
app.register_blueprint(home)

if __name__ == "__main__":
    app.run(debug=True)
