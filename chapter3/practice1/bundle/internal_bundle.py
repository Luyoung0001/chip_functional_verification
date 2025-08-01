from toffee import Bundle, Signals

class InternalBundle(Bundle):
    full, empty, resetn = Signals(3)
