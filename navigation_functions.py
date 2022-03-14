# imports

from selenium import webdriver
from time import sleep as s
from product_database import shirts_list
from product_database import henley_list
from product_database import shorts_list
from product_database import polos_list
from product_database import tshirts_list
from product_database import pants_list

# global variables

driver = webdriver.Firefox(
    executable_path='D:/User/Documents/Iago/Rhudá Ltda/Algoritmos/'
                    'verificar estoque/geckodriver.exe'
    )

# open browser and url
def open_site(search_text, counter, database, url):
    # opening the browser and accessing the site
    driver.get(url)
    print('Open Website')
    s(3)
    search_product(search_text, counter, database)

# search the product in the search bar
def search_product(search_text, counter, database):
    if database == 'shirts':
        # searching the product inside shirts
        search_bar = driver.find_element_by_xpath(
            "//*[@id='main-content']/app-catalog/ion-header/ion-toolbar/div/ion-buttons[2]/ion-searchbar/div/input"
        )
        search_bar.clear()
        search_bar.send_keys(search_text)
        print('\n')
        print(f'Searching for {shirts_list[counter]}...')
        print('\n')
        s(1)
    elif database == 'pants':
        # searching the product inside pants
        search_bar = driver.find_element_by_xpath(
            "//*[@id='main-content']/app-catalog/ion-header/ion-toolbar/div/ion-buttons[2]/ion-searchbar/div/input"
        )
        search_bar.clear()
        search_bar.send_keys(search_text)
        print('\n')
        print(f'Searching for {pants_list[counter]}')
        print('\n')
        s(1)
    elif database == 'shorts':
        # searching the product inside shorts
        search_bar = driver.find_element_by_xpath(
            "//*[@id='main-content']/app-catalog/ion-header/ion-toolbar/div/ion-buttons[2]/ion-searchbar/div/input"
        )
        search_bar.clear()
        search_bar.send_keys(search_text)
        print('\n')
        print(f'Searching for {shorts_list[counter]}')
        print('\n')
        s(1)
    elif database == 'polos':
        # searching the product inside polos
        search_bar = driver.find_element_by_xpath(
            "//*[@id='main-content']/app-catalog/ion-header/ion-toolbar/div/ion-buttons[2]/ion-searchbar/div/input"
        )
        search_bar.clear()
        search_bar.send_keys(search_text)
        print('\n')
        print(f'Searching for {polos_list[counter]}')
        print('\n')
        s(1)
    elif database == 't-shirts':
        # searching the product inside t-shirts
        search_bar = driver.find_element_by_xpath(
            "//*[@id='main-content']/app-catalog/ion-header/ion-toolbar/div/ion-buttons[2]/ion-searchbar/div/input"
        )
        search_bar.clear()
        search_bar.send_keys(search_text)
        print('\n')
        print(f'Searching for {tshirts_list[counter]}')
        print('\n')
        s(1)
    elif database == 'henley':
        # Pesquisando o Produto dentro de calças
        search_bar = driver.find_element_by_xpath(
            "//*[@id='main-content']/app-catalog/ion-header/ion-toolbar/div/ion-buttons[2]/ion-searchbar/div/input"
        )
        search_bar.clear()
        search_bar.send_keys(search_text)
        print('\n')
        print(f'Searching for {henley_list[counter]}')
        print('\n')
        s(1)

# select the searched product
def click_product():
    click_product = driver.find_element_by_xpath(
        "/html/body/app-root/ion-app/ion-router-outlet/app-store/ion-router-outlet/app-catalog/ion-content/app-content-wrapper/div/div/div/app-catalog-products/div/div/div/div[1]/img"
    )
    click_product.click()
    s(1)