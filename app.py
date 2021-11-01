from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)


app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:149811@localhost/Aggregator_news'
app.debug = True
db = SQLAlchemy(app)


class table(db.Model):
    __tablename__ = "News"
    id = db.Column(db.Integer(), primary_key=True)
    news_title = db.Column(db.String(200), nullable=False)
    news_link = db.Column(db.String(300), nullable=False)
    news_time = db.Column(db.String(40), nullable=False)
    news_image_link = db.Column(db.String(200), nullable=False)

    def __init__(self, news_title, news_link, news_time, news_image_link):
        self.news_title = news_title
        self.news_link = news_link
        self.news_time = news_time
        self.news_image_link = news_image_link


@app.route("/News", methods=["POST"])
def test():
    return {
        "test": "test1"
    }