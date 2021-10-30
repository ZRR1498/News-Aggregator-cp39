import os
import requests
import csv
import shutil


if os.path.exists("C:\\PycharmProjects\\Aggregator News\\Read News\\Dir_news"):  # Directory check
    shutil.rmtree("C:\\PycharmProjects\\Aggregator News\\Read News\\Dir_news")
os.mkdir("C:\\PycharmProjects\\Aggregator News\\Read News\\Dir_news")

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
}

arr_news = []

def download_data():
    with open("sw_data.csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        header_table = next(reader, None)
        for row in reader:
            arr_news.append(row)

        for elem in enumerate(arr_news):
            url_new = elem[1][1]
            url_images = elem[1][3]
            i = elem[0] + 1

            r_html = requests.get(url=url_new, headers=headers)
            r_img = requests.get(url=url_images, headers=headers)

            dir_take_news = f"C:\\PycharmProjects\\Aggregator News\\Read News\\Dir_news\\News_{i}"
            file_html = f"C:\\PycharmProjects\\Aggregator News\\Read News\\Dir_news\\News_{i}\\News_{i}.html"
            image = f"C:\\PycharmProjects\\Aggregator News\\Read News\\Dir_news\\News_{i}\\Image_{i}.png"

            os.mkdir(dir_take_news)

            with open(file_html, "w", encoding="utf-8") as file:
                file.write(r_html.text)

            with open(image, "wb") as file:
                file.write(r_img.content)