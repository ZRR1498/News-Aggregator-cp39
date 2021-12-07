# from flask import Flask, render_template, request, redirect
#
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy import create_engine
# from werkzeug.security import generate_password_hash, check_password_hash
#
# app = Flask(__name__)
#
#
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:149811@localhost/Aggregator_news'
# db = SQLAlchemy(app)
# app.debug = True
#
#
# class table(db.Model):
#     __tablename__ = "users"
#     id = db.Column(db.Integer(), primary_key=True)
#     user_name = db.Column(db.String(20), nullable=False, unique=True)
#     user_surname = db.Column(db.String(20), nullable=False, unique=True)
#     user_nickname = db.Column(db.String(20), nullable=False, unique=True)
#     user_email = db.Column(db.String(30), nullable=False, unique=True)
#     user_password_hash = db.Column(db.String(128), nullable=False)
#
#     def __init__(self, user_name, user_surname, user_nickname, user_email, user_password_hash):
#         self.user_name = user_name
#         self.user_surname = user_surname
#         self.user_nickname = user_nickname
#         self.user_email = user_email
#         self.user_password_hash = generate_password_hash(user_password_hash)
#
#     def set_password(self, secret):
#         self.password = generate_password_hash(secret)
#
#
# @app.route("/")
# def index():
#     return render_template('index.html')
#
# @app.route("/sign_up", methods=["POST", "GET"])
# def sign_up():
#     if request.method == "POST":
#         user_name = request.form["firstName"]
#         user_surname = request.form['lastName']
#         user_nickname = request.form["nickname"]
#         user_email = request.form["email"]
#         user_password = request.form["password"]
#
#         item = table(
#             user_name=user_name,
#             user_surname=user_surname,
#             user_nickname=user_nickname,
#             user_email=user_email,
#             user_password_hash=user_password
#         )
#
#         try:
#             db.session.add(item)
#             db.session.commit()
#             return redirect('/')
#         except:
#             return "Error POST"
#     else:
#         return render_template('sign_up.html')
#
#
# @app.route("/sign_in", methods=["POST", "GET"])
# def sign_in():
#     if request.method == "POST":
#         email = request.form["email"]
#         password = request.form['password']
#
#         engine = create_engine('postgresql://postgres:149811@localhost/Aggregator_news')
#
#         Session = sessionmaker(bind=engine)
#         s = Session()
#
#         query = s.query(table).filter_by(table.user_email == email).one()
#         result = query.first()
#         if result:
#             return redirect('/')
#         else:
#             return 'Wrong email or password!'
#     else:
#         return render_template('sign_in.html')
#
#
# @app.route("/support")
# def support():
#     return render_template('support.html')
#
#
#
# if __name__=="__app__":
#     app.run(debug=True)

# with connection.cursor() as cursor:
#     sql = "COPY news(news, links, times, links_images) FROM 'C:\\PycharmProjects\\Aggregator News\\sw_data.csv' DELIMITER ',' CSV HEADER"
#     cursor.copy_expert(sql, open('sw_data.csv', 'r', encoding='utf-8'))
# threading.Timer(86400, load_news).start()