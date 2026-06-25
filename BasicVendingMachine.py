class VendingMachine:
    """A vending machine that vends some product for some price. 
    Applying the Adding Funds and Vending methods

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Please add $10 more funds.'
    >>> v.add_funds(7)
    'Current balance: $7'
    >>> v.vend()
    'Please add $3 more funds.'
    >>> v.add_funds(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.add_funds(10)
    'Current balance: $10'
    """
    def __init__(self, product: str, price: int):
        """Set the product and its price attributes."""
        self.product = product
        self.price = price
        self.funds = 0

    def add_funds(self, n: int) -> str:
        """add n to the balance and return a message about the updated balance."""
        self.funds += n
        return f'Current balance: ${self.funds}'

    def vend(self) -> str:
        """Dispense the product if there is sufficient funds and
        return a message. Update balance accordingly."""
        
        # Check if they paid yet
        if self.funds < self.price:
            difference = self.price - self.funds
            return f'Please add ${difference} more funds.'

        # There is enough funds
        change = self.funds - self.price
        self.funds = 0 
        
        # Return Change
        if change > 0:
            return f'Here is your {self.product} and ${change} change.'
        
        return f'Here is your {self.product}.'