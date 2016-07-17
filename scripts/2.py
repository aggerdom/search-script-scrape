# coding: utf-8
import requests
from bs4 import BeautifulSoup
from datetime import datetime as dt

def get_most_recent_dataset(url='http://catalog.data.gov/dataset?q=&sort=metadata_created+desc'):
    """
    Params:
        url (str): The dataset.gov portal with a query to sort by date, descending
    Returns:
        dataset_name (str): The name of the most recent dataset from data.gov
    """
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    tag = soup.find_all('h3', attrs={'class': "dataset-heading"}, limit=1)[0]
    # Select and return the text from the link inside dataset-heading
    dataset_name = tag.findAll('a')[0].text
    return dataset_name

if __name__ == '__main__':
    get_most_recent_dataset()
    print("'{}', '{}'".format(dt.utcnow().ctime(),
                              get_most_recent_dataset()))
