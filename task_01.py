#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Mini-DB """


def sum_orders(customers, orders):
    """
    Calculate total orders per customer.
    Args:
        customers (dict): A dictionary of customers keyed by customer_id
        orders (dict): A dictionary of orders keyed by order id
    Returns:
        dict: A dictionary with the total or orders per customer.
    """

    join = {}

    for ckey, cust in customers.iteritems():
        hits = 0
        totals = 0
        for order in orders.values():
            if ckey in (order['customer_id'],):
                hits += 1
                totals += order['total']
                join[ckey] = {'name': cust['name'],
                              'email': cust['email'],
                              'orders': hits,
                              'total': totals}
    return join
