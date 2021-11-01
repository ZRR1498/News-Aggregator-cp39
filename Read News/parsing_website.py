import feedparser
import csv


News_feed = feedparser.parse("https://meduza.io/rss2/all")

arr_data = []
arr_headers = ["News", "Links", "Times", "Links images"]

def parsing_link():
    for entry in News_feed.entries:
        title = entry.title.replace(u'\xa0', ' ')
        link = entry.link
        time = entry.published
        image = entry.links[1]["href"]
        arr_data.append([title, link, time, image])

    with open("sw_data.csv", "w", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(arr_headers)
        for row in arr_data:
            writer.writerow(row)