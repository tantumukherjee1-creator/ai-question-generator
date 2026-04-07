from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Import routes
from routes import main
app.register_blueprint(main)

if __name__ == '__main__':
    app.run(debug=True)