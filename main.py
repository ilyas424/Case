from flask import Flask
from flask import render_template
from flask import request
from flask import redirect 
from flask import url_for
from flask import flash
from flask_login import LoginManager
from flask_login import login_user
from flask_login import login_required
from flask_login import logout_user
from flask_login import current_user
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from loguru import logger
import datetime  
from datetime import datetime

import setting


app = Flask(__name__)
app.secret_key = 'some secret salt'
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{setting.DB_USER_NAME}:{setting.DB_PASSWORD}@{setting.DB_HOST}/{setting.DB_NAME}"

logger.add("main.log", format="[{time}] {level}: {message}", level="INFO", backtrace=True, diagnose=True)
logger.configure()

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login_manager = LoginManager(app)

import models
import setting
import schemas



@login_manager.user_loader
def load_user(user_id):
    return models.Admin.query.filter_by(id=user_id).first()


@app.route('/', methods=("POST", "GET"))
def register():
    logger.info("access to http://127.0.0.1:5000/")
    if request.method == "POST":
        logger.info("POST request")
        try:
            
            t = models.Time(    
            )

            db.session.add(t)
            db.session.flush()

            u = models.User(
                first_name=request.form['first_name'],
                last_name=request.form['last_name'],
                surname=request.form['surname'],
                birth_date=request.form['birth_date'],
                place_work=request.form['place_work'],
                time_id=t.id
            )
            db.session.add(u)
            db.session.flush()


            d = models.Statistic(
                name=request.form['first_name'],
                status='user',
                action='append',
            )

            db.session.add(d)
            db.session.commit()

            logger.info("adding user data to database")
            logger.info("Redirect page successful Message")

            return render_template('Message.html')
        except:
            logger.info("error adding data to database")
            db.session.rollback()
            
    logger.info("GET request url '/'")
    return render_template('Forms.html')


@app.route('/users', methods=["GET"])
@login_required
def get_users():
    logger.info("access to http://127.0.0.1:5000/users")
    users = []
    try:
        logger.info("Select data to database")
        users = models.User.query.all()
    except:
        logger.info("show error user data to database")
    return render_template('ListUsers.html', list=users)


@app.route('/delete/<id>', methods=["GET","POST"])
@login_required
def delete_user_by_id(id):
    logger.info("access to http://127.0.0.1:5000/delete")
    try:
        ("Select data to database")
        user = models.User.query.filter_by(id=id).first()
        db.session.delete(user)

        u = models.Statistic(
                name=str(current_user.login),
                status='admin',
                action='delete'
            )
        db.session.add(u)
        db.session.commit()

        logger.info("adding action data to database")
    except:
        logger.info("show error user data to database")
        db.session.rollback()
    return redirect(url_for('get_users'))


@app.route('/auth', methods=["GET", "POST"])
def auth():
    logger.info("access to http://127.0.0.1:5000/auth")
    if request.method == 'POST':
        admin = models.Admin.query.filter_by(login=request.form['login'], password=request.form['password']).first()
        if admin:
            login_user(admin)
            logger.info("successful authorization")
            return redirect(url_for('get_users'))
        else:
            logger.info('valid data')
            flash("Неверный пароль и/или логин", "error")
    return render_template('Auth.html')


@app.route('/statistics', methods=["GET"])
@login_required
def get_statistics():
    logger.info("access to http://127.0.0.1:5000/statistics")
    statics = []
    try:
        ("Select statistics to database")
        statics = models.Statistic.query.all()
        statics_req = []
        for i in statics:
            statics_req.append(schemas.ResponseModel(
                id=i.id, 
                name=i.name, 
                status=i.status, 
                action=i.action,
                date=i.date.strftime('%Y-%b-%d')
            ))
            logger.info("show statistic page")
    except:
        logger.info("show error user data to database")
    return render_template('Statics.html', list=statics_req)





@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('register'))




if __name__ == '__main__':
    app.run(debug=True)