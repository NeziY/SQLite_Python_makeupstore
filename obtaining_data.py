import sqlite3 as lite
import sys



con = None

def obtaining_data_func():
    try:
        con = lite.connect('makeup_store.db') # connection object returned when connecting to the database

        cur = con.cursor() # The cursor is used to traverse the records from the result set.

        # cur.execute('select users.name, diary_logs.date,diary_logs.content,'
                    #'diary_logs.deleted_content from diary_logs join users on diary_logs.user_id = users.id')

        # cur.execute("INSERT INTO diary_logs VALUES (3,1,'2016-04-20','yo yo yo','FALSE')")
        # cur.execute("select customer.first_name, customer.last_name, inventory.p_name,inventory.price"
        #             " from inventory"
        #             " join customer_shoppingcart on inventory.id = customer_shoppingcart.p_id "
        #             "join customer on customer.id = customer_shoppingcart.c_id")

        c_id = input("Enter id\n")
        purchase = input("what product would you like to purchase\n")

        cur.execute("update inventory set quantity = quantity - 1 where id = " + purchase)
        cur.execute("select * from inventory")
        data = cur.fetchall()
        for i in range(data.__len__()):
            print(data[i])



    except:
        print("error")

    finally:
        if con:
            con.close()


obtaining_data_func()
