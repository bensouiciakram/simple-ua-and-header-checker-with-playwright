from playwright.sync_api import sync_playwright 
from playwright.sync_api._generated import Response
from pprint import pprint 
import logging 

# global vars & initialisations : 
browsers = [
    'chromium',
    'firefox',
    'webkit'
]
logging.basicConfig(
    level=logging.DEBUG,
)

# helper functions : 
def choose_browser_type() -> int :
    for index,browser_type in enumerate(browsers):
        print(f'{browser_type} : {index}')
    return int(input('Choose you browser id : '))

def information_formatter(response:Response):
    logging.info(f'the user agent is : {response.request.headers["user-agent"]}\n')
    logging.info('the request headers is : \n')
    pprint(response.request.headers)
    print()
    logging.info('the response headers is :\n')
    pprint(response.headers)

# main funtionality : 
if __name__ == '__main__':
    with sync_playwright() as p :
        #browser = p.chromium.launch(channel='chrome',headless=False)
        exec(f'browser = p.{browsers[choose_browser_type()]}.launch(headless=False)')
        context = browser.new_context()
        page = context.new_page() 
        url = input('Enter the intended url : ')
        response = page.goto(url)
        information_formatter(response)
        breakpoint()