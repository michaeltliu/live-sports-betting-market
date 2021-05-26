from datetime import datetime
from functools import total_ordering
import heapq

@total_ordering
class Order:
    def __init__(self, product, side, quantity, limit):
        self.time_sent = datetime.now()
        self.time_filled = None
        self.product = product
        self.side = side
        self.quantity = quantity
        self.limit = limit

    def __eq__(self, other):
        return (self.limit, self.time_sent) == (other.limit, other.time_sent)
    
    def __lt__(self, other):
        assert(self.side == other.side)

        if self.side == "buy":
            return (-self.limit, self.time_sent) < (-other.limit, other.time_sent)
        else:
            return (self.limit, self.time_sent) < (other.limit, other.time_sent)

    def __ne__(self, other):
        return (self.limit, self.time_sent) != (other.limit, other.time_sent)

class Orderbook:
    def __init__(self, product):
        self.product = product
        self.buys = []
        self.sells = []

    # Every order will either be passive or aggressive
    # Fill aggressive orders immediately and add passive orders to the orderbook
    def receiveOrder(self, order):
        pass