# imports

from os import remove as r
from stock_validation_functions import validate_files


# delete database
def delete_database(
        database_shirt, database_pants, database_tshirt,
        database_henley, database_short, database_polo,
):
    try:
        r(database_shirt)
    except:
        pass
    try:
        r(database_pants)
    except:
        pass
    try:
        r(database_tshirt)
    except:
        pass
    try:
        r(database_henley)
    except:
        pass
    try:
        r(database_short)
    except:
        pass
    try:
        r(database_polo)
    except:
        pass

# Create the size and stock table in the parts up database
def create_table_parts_up(
        product, slot1, slot2, slot3, slot4, slot5, database,
        file_shirts, file_pants, file_tshirts, file_henley,
        file_shorts, file_polos
):

    files = validate_files(
        database, file_shirts, file_pants, file_tshirts, file_henley,
        file_shorts, file_polos
    )
    # opening the database file
    file = open(files, 'a')
    # model for print
    model = (
        f'-------------------\n'
        f'SKU: {product}\n'
        f'P: {slot1};\n'
        f'M: {slot2};\n'
        f'G: {slot3};\n'
        f'GG: {slot4};\n'
        f'3G: {slot5};\n'
        f'-------------------\n'
    )
    file.write(model)
    file.close()

# Create the size and stock table in the bottom parts database
def create_table_bottom_parts(
        product, slot1, slot2, slot3, slot4, slot5, slot6, slot7,
        database, file_shirts, file_pants, file_tshirts, file_henley,
        file_shorts, file_polos
):

    files = validate_files(
        database, file_shirts, file_pants, file_tshirts, file_henley,
        file_shorts, file_polos
    )
    # opening the database file
    file = open(files, 'a')
    # model for print
    model = (
        f'-------------------\n'
        f'SKU: {product}\n'
        f'38: {slot1};\n'
        f'40: {slot2};\n'
        f'42: {slot3};\n'
        f'44: {slot4};\n'
        f'46: {slot5};\n'
        f'48: {slot6};\n'
        f'50: {slot7};\n'
        f'-------------------\n'
    )
    file.write(model)
    file.close()

# create table when there is no stock for parts up
def no_stock_parts_up(
        product, file_shirts, file_pants, file_tshirts, file_henley,
        file_shorts, file_polos, database
):

    files = validate_files(
        database, file_shirts, file_pants, file_tshirts, file_henley,
        file_shorts, file_polos
    )
    # opening the database file
    file = open(files, 'a')
    # model for print
    model = (
        f'-------------------\n'
        f'SKU: {product}\n'
        f'P: ----------;\n'
        f'M: ----------;\n'
        f'G: ----------;\n'
        f'GG: ---------;\n'
        f'3G: ---------;\n'
        f'-------------------\n'
    )
    file.write(model)
    file.close()

# create table when there is no stock for bottom parts
def no_stock_bottom_parts(
        product, file_shirts, file_pants, file_tshirts, file_henley,
        file_shorts, file_polos, database
):

    files = validate_files(
        database, file_shirts, file_pants, file_tshirts, file_henley,
        file_shorts, file_polos
    )
    # opening the database file
    file = open(files, 'a')
    # model for print
    model = (
        f'-------------------\n'
        f'SKU: {product}\n'
        f'38: ----------;\n'
        f'40: ----------;\n'
        f'42: ----------;\n'
        f'44: ----------;\n'
        f'46: ----------;\n'
        f'48: ----------;\n'
        f'50: ----------;\n'
        f'-------------------\n'
    )
    file.write(model)
    file.close()