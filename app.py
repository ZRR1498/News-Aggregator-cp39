from flask import Flask, render_template, request, redirect
from config import DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME
import psycopg2
import threading
import csv
from parsing_website import parsing_link

app = Flask(__name__)


connection = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
)
connection.autocommit = True

with connection.cursor() as cursor:
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS news(
            id serial PRIMARY KEY,
            news varchar,
            links varchar,
            times varchar,
            links_images varchar);""")

with connection.cursor() as cursor:
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS users(
            id serial PRIMARY KEY,
            user_name varchar,
            user_lastname varchar,
            user_email varchar,
            user_password varchar);"""
        )

    #Copy csv in to table pg
def load_news_to_db():
    parsing_link()
    with open("sw_data.csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        header_table = next(reader, None)
        for row in reader:
            news_row = row[0]
            with connection.cursor() as cursor:
                cursor.execute("""SELECT 1 FROM news WHERE news = %s;""", (news_row,))
                if cursor.fetchone() is None:
                    cursor.execute("""INSERT INTO news(news, links, times, links_images) VALUES (%s, %s, %s, %s);""",
                                   (row[0], row[1], row[2], row[3]))
    threading.Timer(60, load_news_to_db).start()


load_news_to_db()


# @app.route("/")
# def index():
#     return render_template('index.html')
#

if __name__ == "__main__":
    app.run(debug=True)