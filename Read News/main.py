import download_pages_images
import parsing_website


def main():
    print("Parsing_website...")
    parsing_website.parsing_link()
    print("Download pages and images...")
    download_pages_images.download_data()
    print("Done!")

if __name__ == "__main__":
    main()