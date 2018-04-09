# Part 1
"""
Assume you have the following tables:
Item
+-------------+--------------+------+-----+----------------+
| Field
| Type
| Null | Key | Extra
+-------------+--------------+------+-----+----------------+
| itemID
| int(11)
|
| PRI | auto_increment |
| name
| varchar(64) |
| description | varchar(128) | YES |
| categoryID | int(11)
| YES |
+-------------+--------------+------+-----+----------------+
Category
+-------------+--------------+------+-----+----------------+
| Field
| Type
| Null | Key | Extra
+-------------+--------------+------+-----+----------------+
| categoryID | int(11)
|
| PRI | auto_increment |
| name
| varchar(64) |

+-------------+--------------+------+-----+----------------+
ItemOrderMembership
+-------------+--------------+------+-----+----------------+
| Field
| Type
| Null | Key | Extra
|
+-------------+--------------+------+-----+----------------+
| orderID
| int(11)

| itemID
| int(11)

+-------------+--------------+------+-----+----------------+
Write a query that will get me the item name and item category name for
all items in orderID 12345. Please note that Item.categoryID may be NULL,
and that the query should return item names even for those records where
this is the case.

Answer:

SELECT Item.name, Category.name
FROM Item LEFT JOIN Category ON
     Item.categoryid=Category.id LEFT JOIN
     Itemordermembership ON Item.id=Itemordermembership.itemid
where Itemordermembership.orderid = 12345

"""


def grading(data):
    size = len(data)
    lenx = int(round((size * .20)))
    print(lenx)
    for f in range(size):
            # divide length of numbers by 20% since grades a-f
            y = (f,)
            if 0 <= y[0] <= lenx:
                print("A:", data[f])
                print()
            elif (lenx) <= y[0] <= (lenx * 2):
                print("B:", data[f])
                print()
            elif (lenx) <= y[0] <= (lenx * 3):
                print("c:", data[f])
                print()
            elif (lenx) <= y[0] <= (lenx * 4):
                print("d:", data[f])
                print()
            else:
                print("f:", data[f])
                print()
randomlist = [99, 92, 91, 91, 89, 85, 83, 82, 80, 79, 78, 78, 77, 76, 75, 74, 62, 55, 43, 20]
grading(randomlist)

