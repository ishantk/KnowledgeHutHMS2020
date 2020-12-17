"""
    Multi Threading in Python :)
"""

import time
import requests
import json

import threading

""" 
class PrintingTask:

    def print_documents(self):

        for i in range(1, 11):
            print("[JOHN] Printing Document #{}".format(i))
            time.sleep(1)


class FetchNewsTask:

    def fetch_news(self):

        print("[NEWS] Fetching News...")

        api_key = "31c21508fad64116acd229c10ac11e84"
        url = "http://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={}".format(api_key)

        time.sleep(10)

        response = requests.get(url)
        text = response.text

        print(text)
        print(type(text))

        # converted JSON textual content as Python Dictionary
        data = json.loads(text)
        print(data)
        print(type(data))

        print(data['totalResults'])
        print()
        for article in data['articles']:
            print(article['title'])
            print(article['author'])
            print()

"""

class PrintingTask(threading.Thread):

    # Override run from the Parent threading.Thread
    def run(self):

        for i in range(1, 11):
            print("[JOHN] Printing Document #{}".format(i))
            time.sleep(1)


class FetchNewsTask(threading.Thread):

    def run(self):

        print("[NEWS] Fetching News...")

        api_key = "31c21508fad64116acd229c10ac11e84"
        url = "http://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={}".format(api_key)

        time.sleep(10)

        response = requests.get(url)
        text = response.text

        print(text)
        print(type(text))

        # converted JSON textual content as Python Dictionary
        data = json.loads(text)
        print(data)
        print(type(data))

        print(data['totalResults'])
        print()
        for article in data['articles']:
            print(article['title'])
            print(article['author'])
            print()

def main():

    print("Main Started")

    task1 = PrintingTask()
    task2 = FetchNewsTask()

    # task1.print_documents()
    task1.start()
    print()

    # task2.fetch_news()
    task2.start()
    print()

    for i in range(1, 11):
        print("[MAIN] Printing Document #{}".format(i))
        time.sleep(1)

    print("Main Finished")

if __name__ == '__main__':
    main()