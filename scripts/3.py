# coding: utf-8
import requests
from bs4 import BeautifulSoup
from datetime import datetime as dt

"""
Notes as I'm going about this.

Challenge Description:
    Retrieve the number of people who visited a U.S. government website using Internet Explorer 6.0
    in the last 90 days.

Supplied Link:
    https://analytics.usa.gov/data/live/ie.json

- Looks like a good point to start using api's when possible

Attempt to Reconstruct Finding Link:
    - "Google: Visit statistics for all u.s. gov websites."
    - Analytics.usa.gov
    - https://analytics.usa.gov/#explanation (About the data)
    - quote::
        Not every government website is represented in this data.
    - Odd thoughts:
        - https://analytics.usa.gov/data/live/browsers.json (Browser breakdown)
             Who the hell is visiting this on a ps3?
             ``"Nintendo Browser": 46683``
             ``"Playstation 3": 29793``
             ``"Dolfin": 1601,`` (surprisingly low)
        - https://analytics.usa.gov/data/live/ie.json (Versions of internet explorer)

If I were to use this data, it would probably be either a good idea to dump the json to a database,
or to find where I can make a GET request. In any case, it would be good to figure out when the data updates
in order to set up a time for this to run and log the data.
"""


def main(url="https://analytics.usa.gov/data/live/ie.json"):
    """
    Challenge Description:
        Retrieve the number of people who visited a U.S. government website using Internet Explorer 6.0
        in the last 90 days.

    Args:
        url (str): analytics.gov live data url for visits from different i.e. version

    Returns:
        (int) Number of views within last 90 days.
    """
    r = requests.get(url)
    data = r.json()
    return data['totals']['ie_version']['6.0']


if __name__ == '__main__':
    print('========== Challenge 3 ============')
    print('TIME REQUESTED (UTC): ', dt.utcnow().ctime())
    print('NUMBER OF REQUESTS IN LAST 90 DAYS: ', main())