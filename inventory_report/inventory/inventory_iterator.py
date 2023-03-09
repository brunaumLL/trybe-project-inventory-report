from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, data):
        self.data = data
        self.current_product = 0

    def __next__(self):
        product = self.data[self.current_product]

        if not product:
            raise StopIteration()

        self.current_product += 1
        return product
