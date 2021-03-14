from auth import app, db
from flask import Flask
from flask_mail import Mail
from flask_gravatar import Gravatar
from flask_sqlalchemy import SQLAlchemy

#app = Flask(__name__)
#app.config.from_object('auth.config')

#mail = Mail(app)
#gravatar = Gravatar(app, use_ssl=True)
#db = SQLAlchemy(app)

from auth import hooks
from auth import models
from auth import views 




if __name__ == '__main__':
    db.create_all()
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)
    #app.run(debug=True)

