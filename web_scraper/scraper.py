import requests
import pprint
from bs4 import BeautifulSoup
def get_citations_needed_count():

    url = 'https://en.wikipedia.org/wiki/History_of_Mexico'
    response = requests.get(url)
    soup = BeautifulSoup(response.content , 'html.parser')
    results = soup.find(id="mw-content-text")
    citations_needed = results.find_all('a', title='Wikipedia:Citation needed')
    # print(citations_needed)
    # print(len(citations_needed))
    # print(type(dir(citations_needed)))
    return citations_needed
    return len(citations_needed)
    
  
get_citations_needed_count()    


def get_citations_needed_report():
    citations_needed = get_citations_needed_count()
    for x in citations_needed:
        find_parent = x.find_parents('p')
        for b in find_parent:
            text = b.text   
        print( f'Citation needed for {text}')
   
    


get_citations_needed_report()    








