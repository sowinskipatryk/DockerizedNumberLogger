import random
import schedule
import time
import os


def random_number(limit=3, count=1):
    for _ in range(count):
        yield random.randint(1, limit)


def job():
    for number in random_number(limit=10):
        res = f"wynik: {number}"
        print(res)
        with open("docs/random_number.txt", 'a') as file:
            file.write(res+'\n')


script_dir = os.path.dirname(os.path.abspath(__file__))
docs_dir = os.path.join(script_dir, 'docs')
if not os.path.exists(docs_dir):
    os.mkdir(docs_dir)

schedule.every(5).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
