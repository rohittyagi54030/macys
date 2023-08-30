import os

os.system("pip3 install -r requirements.txt")
from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import random
from urllib.parse import urlparse
from pyvirtualdisplay import Display
import time
import requests

options = webdriver.ChromeOptions()

uas = []
import csv

with open("./UserAgentMobile.csv", "r") as csvfile:
    reader_variable = csv.reader(csvfile, delimiter=",")
    for row in reader_variable:
        uas.append(row)
ua = random.choice(uas)
print(ua)
options.add_argument(f"user-agent={ua[0]}")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-blink-features=AutomationControlled')
autocontrol = 'no'
if autocontrol == 'yes':
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--window-size=1420,1080")
    display = Display(visible=0, size=(1420, 1080))
    display.start()

sleep_time = 50
count = 1000

run = 0
bounce = 35
c_bounce = 0

cities = ['california', 'georgia', 'illinois', 'massachusetts', 'new jersey', 'new york', 'ohio', 'pennsylvania',
          'texas', 'washington', 'wisconsin', 'missouri']

final_urls = [
    {'id': 1, 'url': 'https://superadme.com/tracker/click.php?key=mlkcs0uxhszz9cmtadhm', 'page_view': 1}
]

while True:
    if run >= count:
        break
    try:
        num = random.randint(0, 1000000)
        padded_num = str(num).rjust(6, '0')
        seleniumwire_options = {
            'proxy': {
                'http': f'http://639467+US+639467-{padded_num}:73e4e129e@us-1m.geosurf.io:8000',
                'https': f'https://639467+US+639467-{padded_num}:73e4e129e@us-1m.geosurf.io:8000',
                'verify_ssl': True,
            },
        }
        # proxy_dict = {
        #     'http': f'http://639467+US+639467-{padded_num}:73e4e129e@us-1m.geosurf.io:8000',
        #     'https': f'http://639467+US+639467-{padded_num}:73e4e129e@us-1m.geosurf.io:8000'
        # }
        # s = requests.Session()
        # s.proxies = proxy_dict
        # ip_details = s.get('https://geo.geosurf.io/').json()
        # if ip_details['city'].lower() not in cities:
        if True:
            final_url = random.choice(final_urls)
            try:
                driver = webdriver.Chrome(ChromeDriverManager().install(), options=options,
                                          seleniumwire_options=seleniumwire_options)
                action = webdriver.ActionChains(driver)
                driver.implicitly_wait(30)

                driver.get(final_url['url'])
                time.sleep(10)

                driver.execute_script(f"window.scrollTo(0, {random.randint(100, 1000)})")
                time.sleep(2)
                driver.execute_script(f"window.scrollTo({random.randint(100, 1000)}, 0)")
                time.sleep(5)
                driver.execute_script(f"window.scrollTo(0, {random.randint(100, 1000)})")

                print(f"Sleeping for {random.randint(60, 70)} seconds")

                current_url = urlparse(driver.current_url)

                c_weightage = int((bounce * run) / 100)
                if c_bounce < c_weightage:
                    c_bounce += 1
                    print("Bounce")
                else:
                    print(True)
                    i = 0
                    while i < final_url["page_view"]:
                        print(i)
                        try:
                            links = []
                            for link in driver.find_elements(By.TAG_NAME, "a"):
                                link_url = urlparse(link.get_attribute("href"))
                                if link_url.netloc == current_url.netloc and link_url.path != current_url.path:
                                    links.append(link)
                            link = random.choice(links)
                            action.move_to_element(link)
                            action.perform()
                            link.click()
                            driver.execute_script(f"window.scrollTo(0, {random.randint(100, 1000)})")
                            time.sleep(2)
                            driver.execute_script(f"window.scrollTo({random.randint(100, 1000)}, 0)")
                            time.sleep(5)
                            driver.execute_script(f"window.scrollTo(0, {random.randint(100, 1000)})")

                            print(f"Sleeping for {random.randint(40, 50)} seconds")
                            time.sleep(sleep_time)
                            i += 1
                        except:
                            i += 1
                            pass
                print("Closing Browser")
                run += 1
                driver.quit()
            except Exception as e:
                print(e)
                try:
                    driver.quit()
                except:
                    pass
    except Exception as e:
        print(e)
