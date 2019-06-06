# shopSmart.py
# ------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
Here's the intended output of this script, once you fill it in:

Welcome to shop1 fruit shop
Welcome to shop2 fruit shop
For orders:  [('apples', 1.0), ('oranges', 3.0)] best shop is shop1
For orders:  [('apples', 3.0)] best shop is shop2
"""

import shop
def price_compare(shop_1, shop_2):
    if shop_1 <= shop_2:
        return True
    else:
        return False
         


def shopSmart(orderList, fruitShops):



    shop_2 = fruitShops[0]
    for shop_1 in fruitShops:
        if price_compare(shop_1.getPriceOfOrder(orderList),shop_2.getPriceOfOrder(orderList)) is True:
            shop_2 = shop_1
    return shop_2


if __name__ == '__main__':
  "This code runs when you invoke the script from the command line"
  orders = [('apples',1.0), ('oranges',3.0)]
  dir1 = {'apples': 2.0, 'oranges':1.0}
  shop1 =  shop.FruitShop('shop1',dir1)
  dir2 = {'apples': 1.0, 'oranges': 5.0}
  shop2 = shop.FruitShop('shop2',dir2)
  shops = [shop1, shop2]
  print "For orders ", orders, ", the best shop is", shopSmart(orders, shops).getName()
  orders = [('apples',3.0)]
  print "For orders: ", orders, ", the best shop is", shopSmart(orders, shops).getName()
