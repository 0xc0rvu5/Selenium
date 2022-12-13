from selenium import webdriver
from selenium.webdriver.common.by import By


#initialize global variables
PATH = '~/.local/bin/chromedriver'
DRIVER = webdriver.Chrome(PATH)


def find_events():
    '''Launch Selenium browser using chromedriver, find event times and titles, add to events dictionary and print out dictionary content.'''
    DRIVER.get('https://www.python.org/')
    events = {}
    times = DRIVER.find_elements(By.CSS_SELECTOR, '.event-widget time')
    names = DRIVER.find_elements(By.CSS_SELECTOR, '.event-widget .menu a')

    #place each date and title key,value pair into additional dicitonaries starting from 0
    for n in range(len(times)):
        events[n] = {
            'time': f'2022-{times[n].text}',
            'name': names[n].text,
        }

    DRIVER.close()


find_events()


#example output
events = {0: {'time': '2022-12-17', 'name': 'Python Pizza Holguín'}, 1: {'time': '2022-12-21', 'name': 'An Introduction to Model Drift - PyLadies Amsterdam'}, 2: {'time': '2022-12-27', 'name': 'XtremePython 2022'}, 3: {'time': '2022-01-18', 'name': 'Python Meeting Düsseldorf'}, 4: {'time': '2022-02-16', 'name': 'PyConFr 2023'}}

#print out on newlines for readability
for key, value in events.items():
        print(key, value)