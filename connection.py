import psycopg2
from config import DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME

try:
    connection = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    connection.autocommit = True
    print("Connection with DB is successfully")

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )
        print(f"Server version: {cursor.fetchone()}")

        # create table
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """CREATE TABLE news(
    #             id serial PRIMARY KEY,
    #             title varchar(200) NOT NULL,
    #             links varchar(300) NOT NULL,
    #             time varchar(40) NOT NULL,
    #             links_images varchar(200) NOT NULL);"""
    #     )
    #     print("TABLE news created")

        # insert data into table
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """INSERT INTO news (title, links, time, links_images) VALUES
    #         ('lklk', 'klk', 'lklk', 'klk');"""
    #     )

        # select data from table
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """SELECT title FROM news WHERE links = 'klk';"""
    #     )
    #     print(cursor.fetchone())

        # drop table
#     with connection.cursor() as cursor:
#         cursor.execute(
#             """DROP TABLE news;"""
#         )
#         print("[INFO]: Table was dropped")
#
# except Exception as _ex:
#      print("Error connection")

finally:
    if connection:
        connection.close()
        print('Connection closed')
