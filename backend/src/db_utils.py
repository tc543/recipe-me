import sqlite3

# add scraper that scrapes cooking websites for recipes (give credit)

# class Db_utils:
def insert_row(id, dish, main_ingr, sub_ingr, steps) -> None:
    # do you even need self ???
    #also can insert many if easier rather than one by one
    try:

        connection = sqlite3.connect('menu.db')
        cursor = connection.cursor()
        print("Connected")
        insert = '''
            INSERT INTO catalog
            (id, dish, main_ingr, sub_ingr, steps)
            VALUES
            (?, ?, ?, ?)
        '''

        data_tuple = (id, dish, main_ingr, sub_ingr, steps)
        count = cursor.execute(insert, data_tuple)
        connection.commit()
        print(f"{cursor.rowcount} row(s) inserted")
        cursor.close()

    except sqlite3.Error as error:
        print("error inserting row(s)")
    finally:
        if connection:
            connection.close()
            print("Closed")


    # def find_primary_keys(self) -> list[int]:
    #     #TODO 
    #     print("worked find_primary_keys") 
    #     #blah

    # def delete_row(self):
    #     print("worked delete_row")


insert_row(1, "pasta", "tomato", "cheese", 3)