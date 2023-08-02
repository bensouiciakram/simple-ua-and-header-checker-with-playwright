from playwright.sync_api import sync_playwright 
from playwright.sync_api._generated import Response
from pprint import pprint 
import logging 
from pathlib import Path 
import sys 

# helper functions for initialisations : 
def create_logger(logging_level:int) -> logging.RootLogger:
    Path(__file__).parent.joinpath('logs').mkdir(exist_ok=True)
    logger = logging.getLogger(__name__)
    logger.setLevel(logging_level)
    stream_handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(levelname)s:%(message)s')
    file_handler = logging.FileHandler('logs/logs.log')
    file_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)
    return logger 

# global vars & initialisations : 
browsers = [
    'chromium',
    'firefox',
    'webkit'
]

logger = create_logger(logging.DEBUG)

# helper functions : 
def choose_browser_type() -> int :
    for index,browser_type in enumerate(browsers):
        print(f'{browser_type} : {index}')
    return int(input('Choose you browser id : '))


def information_formatter(response:Response):
    logger.info(f'\nthe user agent is : {response.request.headers["user-agent"]}\n')
    logger.info(f'the request headers is : \n{str(response.request.headers)}' + '\n')
    logger.info(f'the response headers is :\n{str(response.headers)}')

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