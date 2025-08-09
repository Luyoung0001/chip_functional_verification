from toffee import Bundle, Signals

class InternalBundle(Bundle):
    full, empty = Signals(2)
