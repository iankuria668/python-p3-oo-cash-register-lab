#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0):
    self.total = 0
    self.discount = discount
    self.items = []
    self.previous_transaction = []

  def add_item(self, title, price, quantity = 1):
    self.total += price * quantity
    for i in range(quantity):
      self.items.append(title)
    return self.total

  def void_last_transaction(self):
    self.total -= self.previous_transaction[-1]
    self.previous_transaction.pop()
    return self.total
  
  def apply_discount(self):
    if self.discount != 0:
      self.total -= self.discount
    else:
      print("There is no discount to apply.")
    return self.total

  def reset_register_totals(self):
    self.total = 0
    self.previous_transaction = []
    return self.total
