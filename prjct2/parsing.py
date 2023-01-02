
import requests
from bs4 import BeautifulSoup


def main_parsing():

    anecdotes = []
    link = "https://www.anekdot.ru/"
    response = requests.post(link).content
    soup = BeautifulSoup(response, 'lxml').find('div', class_="wrapper desktop")
    texts = soup.find('div', class_="fill textblock columns").find('div', class_="texts")
    text = texts.findAll('div', class_="text")[5:]
    for i in text:
        if i.text.find("читать дальше") == -1:
            anecdotes.append(i.text)

    return anecdotes