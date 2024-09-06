class AddressNotFoundException(Exception):
    def __init__(self, message="Address not found"):
        self.message = message
        super().__init__(self.message)
