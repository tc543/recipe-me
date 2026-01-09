import sqlite3

# add scraper that scrapes cooking websites for recipes (give credit)

# class Db_utils:


def create_tables(connection):

    query = '''
        CREATE TABLE catalog(
            id INTEGER PRIMARY KEY,
            dish TEXT NOT NULL,
            main_ingr TEXT NOT NULL,
            sub_ingr TEXT NOT NULL,
            steps TEXT NOT NULL)
    '''
    cursor = connection.cursor()
    exist = "SELECT name FROM sqlite_master WHERE type = 'table' AND name = 'catalog';"
    table_exist = cursor.execute(exist).fetchall()
    if table_exist == []:
        cursor.execute(query)
        connection.commit()
        print("Tables Created")
    # else:
    #     print("Tables already exists")



#reading file:
# with open('file_name', 'r') as file:
#     sqlite_script = file.read()
#     cursor.executescript(sqlite_script)

connection = sqlite3.connect('menu.db')
cursor = connection.cursor()
print("Connected")

create_tables(connection)


def insert_row(id, dish, main_ingr, sub_ingr, steps) -> None:
    # do you even need self ???
    #also can insert many if easier rather than one by one
    #id or diff primary key???
    #how to link to current existing menu.db
    connection = sqlite3.connect('menu.db')
    cursor = connection.cursor()
    print("Connected")

    try:

        insert = '''
            INSERT INTO catalog
            (id, dish, main_ingr, sub_ingr, steps)
            VALUES
            (?, ?, ?, ?, ?)
        '''

        data_tuple = (id, dish, main_ingr, sub_ingr, steps)
        count = cursor.execute(insert, data_tuple)
        connection.commit()
        print(f"{cursor.rowcount} row(s) inserted")
        cursor.close()

    except sqlite3.Error as error:
        print("error inserting row(s)", error)
    finally:
        if connection:
            connection.close()
            print("Closed")


def find_primary_keys(main_ingredients) -> list[int]:
    #TODO 
    connection = sqlite3.connect('menu.db')
    cursor = connection.cursor()

    query = '''
        SELECT * from catalog WHERE main_ingr = ?
    '''
    # also main_ingr has to include that, so like just at least the main_ingr #
    cursor.execute(query, (main_ingredients,))
    foods = cursor.fetchall()
    cursor.close()
    keys = []
    for food in foods:
        keys.append(food[0])
    print("found:", keys) # EDIT; primary key is given, not something inserted? or basically if row 1 delete, can't have key 2, 3, 4, 5...etc. should have key 1, 2, 3, 4....every row shift above
    print("worked find_primary_keys") 


# def view_data():
#     connection = sqlite3.connect('menu.db')
#     cursor = connection.cursor()

#     query = '''
#         SELECT * from catalog
#     '''
#     cursor.execute(query)
#     foods = cursor.fetchall()
#     cursor.close()
#     for food in foods:
        # print(food[0], food[1], food[2], food[3], food[4])



def delete_row(key):
    connection = sqlite3.connect('menu.db')
    cursor = connection.cursor()


    try:
        query = '''
            DELETE FROM catalog WHERE id = ?
        '''
        data = (key,)
        count = cursor.execute(query, data)
        connection.commit()
        print(f"{cursor.rowcount} row(s) deleted")
        cursor.close()
    
    except sqlite3.Error as error:
        print("error inserting row(s)", error)
    finally:
        if connection:
            connection.close()
            print("Closed")


insert_row(1, "blah1", "blah2", "blah3", "blah4")
insert_row(2, "bah1", "blah2", "ah3", "bah4")
# view_data()
find_primary_keys("blah2")
# where blha2 = list of ingredients
delete_row(1)