#first output
print("""**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************""")
#second
print("""

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears
""")
#third
print("""
***********************************
** What would you like to order? **
***********************************
""")
#menu lists

Appetizers = ["Appetizers" , "Wings" , "Cookies" , "Spring Rolls"]
Entrees = [ "Salmon" ,"Steak" ,"Meat Tornado", "A Literal Garden"]
Desserts = ["Ice Cream" , "Cake" ,"Pie"]
Drinks = ["Coffee" ,"Tea" ,"Unicorn Tears"]
Menu = Appetizers + Entrees + Desserts + Drinks
#input from user
the_order=[]
while(True):
    order=input(">")
    if order == 'quit':
        break
  
    elif  order in Menu:
     the_order.append(order)
     counter=the_order.count(order)
    #append use to add element to the list
    #count to get num of element


    if counter == 1:
            print( f"** 1 order of {order} has been added to your meal **")

    else:
            print(f"** {counter} orders of {order} have been added to your meal **")

            print('\n', "all thing that you order is:", '\n')
            print(the_order)
    