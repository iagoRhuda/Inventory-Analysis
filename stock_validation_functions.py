# imports

from product_database import shirts_list
from product_database import henley_list
from product_database import shorts_list
from product_database import polos_list
from product_database import tshirts_list
from product_database import pants_list
from navigation_functions import open_site
from navigation_functions import click_product
from database_handling import create_table_parts_up
from database_handling import create_table_bottom_parts
from database_handling import no_stock_parts_up
from database_handling import no_stock_bottom_parts
from time import sleep as s
from navigation_functions import driver

# check the size slots (only shirts) in the url and creating the table (database)
def validate_shirt(
        database_shirt, database_pants, database_tshirt,
        database_henley, database_short, database_polo, url
):

    database = 'shirts'
    quantity_items = len(shirts_list)
    counter = 0

    while counter < len(shirts_list):

        print('\033[0;shirts\033[m')
        search_text = shirts_list[counter]

        # opening the browser, accessing the site and searching for the product
        open_site(search_text, counter, database, url)

        try:
            # entering the product
            click_product()
            # checking the first stock slot
            slot1 = validate_stock(
                "current xpath of the slot"
            )
            # checking the first stock slot
            slot2 = validate_stock(
                "current xpath of the slot"
            )
            # checking the second stock slot
            slot3 = validate_stock(
                "current xpath of the slot"
            )
            # checking the third stock slot
            slot4 = validate_stock(
                "current xpath of the slot"
            )
            # checking the fourth stock slot
            slot5 = validate_stock(
                "current xpath of the slot"
            )

            # saving on database
            create_table_parts_up(
                search_text, slot1, slot2, slot3, slot4, slot5, database, database_shirt, database_pants, database_tshirt,
                database_henley, database_short, database_polo,
                quantity_items
            )

            s(1)

            counter = counter + 1
            print('\n')
            print('\033[0;34mVALIDATED\033[m')
            print('\n')

        except:
            print('\n')
            print('\033[0;33mNOT VALIDATED\033[m')
            print('\n')

            # making the table out of stock
            no_stock_parts_up(
                search_text, database_shirt, database_pants,
                database_tshirt, database_henley, database_short,
                database_polo, database
            )

            counter = counter + 1

    # go_back = driver.find_element_by_xpath("xpath")
    # go_back.click()

# check the size slots (t-shirts only) in the url and creating the table (database)
def validate_tshirt(
        database_shirt, database_pants, database_tshirt,
        database_henley, database_short, database_polo, url
):

    database = 'tshirts'
    quantity_items = len(tshirts_list)
    counter = 0

    print('\033[0;34mT-shirts\033[m')

    while counter < len(tshirts_list):

        search_text = tshirts_list[counter]

        # opening the browser, accessing the site and searching for the product
        open_site(search_text, counter, database, url)

        try:
            # Entering on product
            click_product()
            # checking the first stock slot
            slot1 = validate_stock(
                "current xpath of the slot"            
            )
            # checking the second stock slot
            slot2 = validate_stock(
                "current xpath of the slot"            
            )
            # checking the third stock slot
            slot3 = validate_stock(
                "current xpath of the slot"            
            )
            # checking the fourth stock slot
            slot4 = validate_stock(
                "current xpath of the slot"            
            )
            # checking the fifth stock slot
            slot5 = validate_stock(
                "current xpath of the slot"            
            )

            # saving on database
            create_table_parts_up(
                search_text, slot1, slot2, slot3, slot4, slot5,
                database, database_shirt, database_pants, database_tshirt,
                database_henley, database_short, database_polo, quantity_items
            )

            s(1)

            counter = counter + 1
            print('\n')
            print('\033[0;34mVALIDATED\033[m')
            print('\n')

        except:
            print('\n')
            print('\033[0;33mNOT VALIDATED\033[m')
            print('\n')

            # making the table out of stock
            no_stock_parts_up(
                search_text, database_shirt, database_pants, database_tshirt,
                database_henley, database_short, database_polo, database
            )

            counter = counter + 1

    # go_back = driver.find_element_by_xpath("xpath")
    # go_back.click()


# check the size slots (pants only) in the url and creating the table (database)
def validate_pants(
        database_shirt, database_pants, database_tshirt,
        database_henley, database_short, database_polo, url
):

    database = 'pants'
    quantity_items = len(pants_list)
    counter = 0

    print('\033[0;34mPants\033[m')

    while counter < len(pants_list):

        search_text = pants_list[counter]

        # opening the browser, accessing the site and searching for the product
        open_site(search_text, counter, database, url)

        try:
            # entering the product
            click_product()
            # checking the first stock slot
            slot1 = validate_stock(
                "current xpath of the slot"            
            )
            # checking the second stock slot
            slot2 = validate_stock(
                "current xpath of the slot"            
            )
            # checking the third stock slot
            slot3 = validate_stock(
                "current xpath of the slot"            
            )
            # checking the fourth stock slot
            slot4 = validate_stock(
                "current xpath of the slot"            
            )
            # checking the fifth stock slot
            slot5 = validate_stock(
                "current xpath of the slot"            
            )
            # checking the sixth stock slot
            slot6 = validate_stock(
                "current xpath of the slot"            
            )
            # checking the seventh stock slot
            slot7 = validate_stock(
                "current xpath of the slot"            
            )

            # saving on database
            create_table_bottom_parts(
                search_text, slot1, slot2, slot3, slot4, slot5, slot6, slot7,
                database, database_shirt, database_pants, database_tshirt,
                database_henley, database_short, database_polo, quantity_items
            )

            s(1)

            counter = counter + 1
            print('\n')
            print('\033[0;34mVALIDATED\033[m')
            print('\n')

        except:
            print('\n')
            print('\033[0;33mNOT VALIDATED\033[m')
            print('\n')

            # making the table out of stock
            no_stock_bottom_parts(
                search_text, database_shirt, database_pants, database_tshirt,
                database_henley, database_short, database_polo, database
            )
            counter = counter + 1
    # go_back = driver.find_element_by_xpath("xpath")
    # go_back.click()

# check the size slots (shorts only) in the url and creating the table (database)
def validate_short(
        database_shirt, database_pants, database_tshirt,
        database_henley, database_short, database_polo, url
):

    database = 'shorts'
    quantity_items = len(shorts_list)
    counter = 0

    print('\033[0;34mShorts\033[m')

    while counter < len(shorts_list):

        search_text = shorts_list[counter]

        # opening the browser, accessing the site and searching for the product
        open_site(search_text, counter, database, url)

        try:
            # entering the product
            click_product()

            # checking the first stock slot
            slot1 = validate_stock(
                "current xpath of the slot"            
            )
            # checking the second stock slot
            slot2 = validate_stock(
                "current xpath of the slot"            
            )
            # checking the third stock slot
            slot3 = validate_stock(
                "current xpath of the slot"            
            )
            # checking the fourth stock slot
            slot4 = validate_stock(
                "current xpath of the slot"            
            )
            # checking the fifth stock slot
            slot5 = validate_stock(
                "current xpath of the slot"            
            )
            # checking the sixth stock slot
            slot6 = validate_stock(
                "current xpath of the slot"            
            )
            # checking the seventh stock slot
            slot7 = validate_stock(
                "current xpath of the slot"            

            # saving on database
            create_table_bottom_parts(
                search_text, slot1, slot2, slot3, slot4, slot5, slot6, slot7,
                database, database_shirt, database_pants, database_tshirt,
                database_henley, database_short, database_polo, quantity_items
            )

            s(1)

            counter = counter + 1
            print('\n')
            print('\033[0;34mVALIDATED\033[m')
            print('\n')

        except:
            print('\n')
            print('\033[0;33mNOT VALIDATED\033[m')
            print('\n')

            # making the table out of stock
            no_stock_bottom_parts(
                search_text, database_shirt, database_pants, database_tshirt,
                database_henley, database_short, database_polo, database
            )

            counter = counter + 1

    # go_back = driver.find_element_by_xpath("xpath")
    # go_back.click()

# check the size slots (polos only) in the url and creating the table (database)
def validate_polo(
        database_shirt, database_pants, database_tshirt,
        database_henley, database_short, database_polo, url
):

    database = 'polos'
    quantity_items = len(polos_list)
    counter = 0

    print('\033[0;34mPolos\033[m')

    while counter < len(polos_list):

        search_text = polos_list[counter]

        # opening the browser, accessing the site and searching for the product
        open_site(search_text, counter, database, url)

        try:
            # entering the product
            click_product()

            # checking the first stock slot
            slot1 = validate_stock(
                "current xpath of the slot"            
            )
            # checking the second stock slot
            slot2 = validate_stock(
                "current xpath of the slot"            
            )
            # checking the thirth stock slot
            slot3 = validate_stock(
                "current xpath of the slot"            
            )
            # checking the fourth stock slot
            slot4 = validate_stock(
                "current xpath of the slot"            
            )
            # checking the fifth stock slot
            slot5 = validate_stock(
                "current xpath of the slot"            
            )

            # saving on database
            create_table_parts_up(
                search_text, slot1, slot2, slot3, slot4, slot5, database,
                database_shirt, database_pants, database_tshirt,
                database_henley, database_short, database_polo,
                quantity_items
            )

            s(1)

            counter = counter + 1
            print('\n')
            print('\033[0;34mVALIDTED\033[m')
            print('\n')

        except:
            print('\n')
            print('\033[0;33mNOT VALIDATED\033[m')
            print('\n')

            # making the table out of stock
            no_stock_parts_up(
                search_text, database_shirt, database_pants, database_tshirt,
                database_henley, database_short, database_polo, database
            )

            counter = counter + 1

    # go_back = driver.find_element_by_xpath("xpath")
    # go_back.click()

# check the size slots (henley only) in the url and creating the table (database)
def validate_henley(
        database_shirt, database_pants, database_tshirt,
        database_henley, database_short, database_polo, url
):

    database = 'henley'
    quntity_items = len(henley_list)
    counter = 0

    print('\033[0;34mHenley\033[m')

    while counter < len(henley_list):


        search_text = henley_list[counter]

        # opening the browser, accessing the site and searching for the product
        open_site(search_text, counter, database, url)

        try:
            # entering on the product
            click_product()

            # checking the first stock slot
            slot1 = validate_stock(
                "current xpath of the slot"            
            )
            # checking the second stock slot
            slot2 = validate_stock(
                "current xpath of the slot"            
            )
            # checking the third stock slot
            slot3 = validate_stock(
                "current xpath of the slot"            
            )
            # checking the fourth stock slot
            slot4 = validate_stock(
                "current xpath of the slot"            
            )
            # checking the fifth stock slot
            slot5 = validate_stock(
                "current xpath of the slot"            
            )

            # saving on database
            create_table_parts_up(
                search_text, slot1, slot2, slot3, slot4, slot5, database,
                database_shirt, database_pants, database_tshirt, database_henley,
                database_short, database_polo, quntity_items
            )

            s(1)

            counter = counter + 1
            print('\n')
            print('\033[0;34mVALIDATED\033[m')
            print('\n')

        except:
            print('\n')
            print('\033[0;33mNOT VALIDATED\033[m')
            print('\n')

            # making the table out of stock
            no_stock_parts_up(
                search_text, database_shirt, database_pants, database_tshirt,
                database_henley, database_short, database_polo, database
            )

            counter = counter + 1

    # go_back = driver.find_element_by_xpath("xpath")
    # go_back.click()

# individually scan size slots by xpath
def validate_stock(xpath):
    try:
        check_stock = driver.find_element_by_xpath(xpath)
        stock = True
    except:
        stock = False

    if stock == True:
        print("\033[0;32mHave Stock\033[m")
        return "Have Stock"
    else:
        print("\033[0;31mOut of Stock\033[m")
        return "Out of Stock"

def validate_files(
        database, file_camisas, file_calcas, file_camisetas,
        file_henley, file_bermudas, file_polos
):
    if database == 'shirts':
        file = file_camisas
    elif database == 'pants':
        file = file_calcas
    elif database == 'tshirts':
        file = file_camisetas
    elif database == 'henley':
        file = file_henley
    elif database == 'shorts':
        file = file_bermudas
    elif database == 'polos':
        file = file_polos
    return file
