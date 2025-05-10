from flask import Flask
from models import db
from views import main

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dishes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
app.register_blueprint(main)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)