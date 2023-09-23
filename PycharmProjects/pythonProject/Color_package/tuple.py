# from collections import namedtuple
#
#
# class Point:
#
#     def __init__(self, x, y):
#         self.x = x
#
#
# Point = namedtuple("Point", ['x', 'y'])
#
# p1 = Point(x=1, y=2)
# p2 = Point(x=1, y=2)
#
# print(p1 == p2)


from translate import Translator

text = "We are the world. We are the children."
# msg = "Take kindly the council of the years."

translator = Translator(to_lang='ig')
translation = translator.translate(text)
# translation1 = translator.translate(msg)

print(translation)