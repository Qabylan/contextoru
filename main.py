from time import sleep
from selenium import webdriver

visited_urls = []

driver = webdriver.Chrome()
urls = ['http://lib.ru/']

while urls:
    url = urls.pop(0)
    visited_urls.append(url)
    driver.get(url)
    print(url)
    sleep(3)
    if '.txt' in url:
        pre = driver.find_element('xpath', '//pre')
        with open('texts.txt', 'a', encoding='utf-8') as f:
            f.write(pre.text)
            print(pre.text)
    else:
        elements = driver.find_elements('xpath', '//a')
        for element in elements:
            href = element.get_attribute('href')
            if href is None:
                continue
            if '#' in href or 'http://lib.ru/' not in href:
                continue
            if 'http' not in href and url[-1] == '/':
                href = url+href
            if 'http' not in href and url[-1] != '/':
                href = 'http://lib.ru/' + href
            if href in visited_urls:
                continue
            urls.append(href)
            urls = list(set(urls))