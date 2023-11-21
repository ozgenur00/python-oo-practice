"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=0):
        """Make a new generator, starting at start"""
        self.start = self.current = start

    def __repr__(self):
        """Show representation"""
        return f"SerialGenerator(start={self.start} next={self.current})"
        
    def generate(self):
        """Return the next serial number"""
        self.current += 1
        return self.current - 1
    
    def reset(self):
        """Reset the serial number to the start"""
        self.current = self.start
