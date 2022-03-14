# imports

from database_handling import delete_database
from stock_validation_functions import validate_shirt
from stock_validation_functions import validate_tshirt
from stock_validation_functions import validate_short
from stock_validation_functions import validate_polo
from stock_validation_functions import validate_pants
from stock_validation_functions import validate_henley
from navigation_functions import driver


#  main function

def inventory_analysis(
            database_shirt, database_pants, database_tshirt,
            database_henley, database_short, database_polo, url
        ):
    try:
        #stopwatch_started = ptns()
        print('Deleting Database ...')
        delete_database(
            database_shirt, database_pants, database_tshirt,
            database_henley, database_short, database_polo
        )
        print('Database Deleted ...')
        validate_shirt(
            database_shirt, database_pants, database_tshirt,
            database_henley, database_short, database_polo, url
        )
        validate_tshirt(
            database_shirt, database_pants, database_tshirt,
            database_henley, database_short, database_polo, url
        )
        validate_short(
            database_shirt, database_pants, database_tshirt,
            database_henley, database_short, database_polo, url
        )
        validate_polo(
            database_shirt, database_pants, database_tshirt,
            database_henley, database_short, database_polo, url
        )
        validate_henley(
            database_shirt, database_pants, database_tshirt,
            database_henley, database_short, database_polo, url
        )
        validate_pants(
            database_shirt, database_pants, database_tshirt,
            database_henley, database_short, database_polo, url
        )
        driver.close()
    except:
        driver.close()
        print('\033[0;31mBoot Error\033[m')