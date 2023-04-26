from flask import Flask
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from loguru import logger

import setting

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{setting.DB_USER_NAME}:{setting.DB_PASSWORD}@{setting.DB_HOST}/{setting.DB_NAME}"

logger.add("main.log", format="[{time}] {level}: {message}", level="INFO", backtrace=True, diagnose=True)
logger.configure()

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import User
from models import Time




@app.route('/', methods=("POST", "GET"))
def register():
    logger.info("access to http://127.0.0.1:5000/")
    if request.method == "POST":
        logger.info("POST request")
        try:
            
            t = Time(    
            )

            db.session.add(t)
            db.session.flush()

            u = User(
                first_name=request.form['first_name'],
                last_name=request.form['last_name'],
                surname=request.form['surname'],
                birth_date=request.form['birth_date'],
                place_work=request.form['place_work'],
                time_id=t.id
            )
            db.session.add(u)
            db.session.commit()
            logger.info("adding user data to database")
        except:
            logger.info("error adding data to database")
            db.session.rollback()
            
        logger.info("Redirect page successful Message")
        return render_template('Message.html')
    logger.info("GET request")
    return render_template('Forms.html')


@app.route('/users', methods=["GET"])
def get_users():
    users = []
    try:
        users = User.query.all()
    except:
        logger.info("show error user data to database")
    return render_template('ListUsers.html', list=users)






if __name__ == '__main__':
    app.run()