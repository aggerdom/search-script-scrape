import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime
from collections import namedtuple


def get_total_datasets(url='http://catalog.data.gov/dataset'):
    """
    Number of datasets currently listed on data.gov
    Notes:
        This does not crawl based on links, but uses the "<N> datasets found" result from the landing page
        of catalog.data.gov/dataset
    """
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    for tag in soup.find_all(name='div', attrs={'class': 'new-results'}):
        # strip commas to make pulling the number out easier
        tag_contents = tag.text.replace(',', '')
        # use a regex to find a solid block of one or more digits in succession
        possible_number = re.search(r'(?P<nsets>\b\d+\b) datasets found',
                                    tag_contents)
        if possible_number:
            total_datasets = possible_number.groups('nsets')[0]
            return int(total_datasets)
        else:
            raise UserWarning("It was originally assumed that div selected"
                              "to find this information was uniquely identified"
                              "(PLEASE CONSIDER CHECKING THIS ASSUMPTION!)")

def get_total_datasets_through_api(url='http://catalog.data.gov/dataset'):
    """
    Number of datasets currently listed on data.gov
    Notes:
        This does not crawl based on links, but uses the "<N> datasets found" result from the landing page
        of catalog.data.gov/dataset
    """
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    for tag in soup.find_all(name='div', attrs={'class': 'new-results'}):
        # strip commas to make pulling the number out easier
        tag_contents = tag.text.replace(',', '')
        # use a regex to find a solid block of one or more digits in succession
        possible_number = re.search(r'(?P<nsets>\b\d+\b) datasets found',
                                    tag_contents)
        if possible_number:
            total_datasets = possible_number.groups('nsets')[0]
            return int(total_datasets)
        else:
            raise UserWarning("It was originally assumed that div selected"
                              "to find this information was uniquely identified"
                              "(PLEASE CONSIDER CHECKING THIS ASSUMPTION!)")


if __name__ == '__main__':
    print("'{}', '{} datasets'".format(datetime.utcnow().ctime(),
                                       get_total_datasets()))
