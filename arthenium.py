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
# def grading(data, grades=('A', 'B', 'C', 'D', 'F')):
#   inc = int(len(data) / len(grades))
#   return {grade: data[i*inc:(i+1)*inc] for i, grade in enumerate(grades)}
#

# def grading(data):
#     grades = ['A', 'B', 'C', 'D', 'F']
#     range_length = int(len(data) / len(grades))
#     print(range_length)
#     grade_ranges = {}
#     for i, grade in enumerate(data):
#         print(i, grade)
#         start_index = i * range_length
#         stop_index = (i+1) * range_length
#         grade_ranges[grade] = data[start_index:stop_index]
#     return grades

#
# def grading(grades):
#     size = len(grades)
#     lenx = (size * .20)
#     finallist = []
#     for f in range(size):
#             # divide length of numbers by 20% since grades a-f
#             if 0 <= f <= lenx:
#                 letter_grade = 'A'
#             elif (lenx * 1) <= f <= (lenx * 2):
#                 if grades[f] == (grades[f - 1]):
#
#                     letter_grade = dict(finallist).get(f)
#                 else:
#                     letter_grade = 'B'
#
#             elif (lenx * 2) <= f <= (lenx * 3):
#                 if grades[f] == (grades[f - 1:]):
#                     letter_grade =dict(finallist).get(f)
#                 else:
#                     letter_grade = 'C'
#
#             elif (lenx * 3) <= f <= (lenx * 4):
#                 if grades[f] == (grades[f - 1]):
#                     letter_grade =dict(finallist).get(f)
#                 else:
#                     letter_grade = 'D'
#             else:
#                 if grades[f] == (grades[f - 1]):
#                     letter_grade =dict(finallist).get(f)
#                 else:
#                     letter_grade = 'F'
#
#             print("appending ", grades[f], " as ", letter_grade)
#             finallist.append([str(grades[f]), str(letter_grade)])
#     for x in finallist:
#         print(x[0],x[1])


# randomlist = [99, 92, 91, 91, 89, 89,89,89, 89,89,89, 89,89, 89,85, 83, 82, 80, 79, 78, 78, 77, 21, 100, 45, 67, 49, 89, 87, 54, 34]
# (grading(sorted(randomlist, reverse=True)))
#
from collections import OrderedDict


def be_fair(grades_dict):
    """
    Accepts an ordered dict of grades, and ensures that
    the same grade never gets a different score.
    """
    prev_grade = None
    prev_scores = [None]
    for grade, scores in grades_dict.items():
        while prev_scores[-1] == scores[0]:
            grades_dict[prev_grade].append(scores[0])
            scores = scores[1:]
            grades_dict[grade] = scores
        prev_grade = grade
        prev_scores = scores
    return grades_dict


def grading(data, grades=('A', 'B', 'C', 'D', 'F')):
    """
    Retuns an ordered dict of grades using a curve.
    """
    data = sorted(data, reverse=True)
    inc = int(len(data) / len(grades))
    grades_result = OrderedDict((grade, data[i * inc:(i + 1) * inc]) for i, grade in enumerate(grades))
    return be_fair(grades_result)


randomlist = [99, 92, 91, 91, 89,89,89,89, 85, 83, 82, 80, 79, 78, 78, 77, 21, 100, 45, 67, 49, 89, 87, 54, 34]
(grading(randomlist))
d = (grading(randomlist))
for k, v in d.items():
    print (k, v)