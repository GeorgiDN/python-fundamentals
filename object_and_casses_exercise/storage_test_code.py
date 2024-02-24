class Storage:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []

    def add_product(self, product: str):
        if len(self.storage) < self.capacity:
            self.storage.append(product)

    def get_products(self):
        return self.storage


# TEST CODE
from unittest import TestCase, main


class StorageTest(TestCase):
    def test_01_init(self):
        storage1 = Storage(2)
        self.assertEqual(storage1.capacity, 2)
        self.assertEqual(storage1.storage, [])

    def test_2_add_product(self):
        storage1 = Storage(2)
        storage1.add_product("apple")
        self.assertEqual(storage1.storage, ["apple"])

    def test_3_add_product_with_not_enough_capacity(self):
        storage1 = Storage(1)
        storage1.add_product("apple")
        storage1.add_product("banana")
        storage1.add_product("orange")
        self.assertEqual(storage1.storage, ["apple"])

    def test_4_get_product(self):
        storage1 = Storage(2)
        storage1.add_product("apple")
        storage1.add_product("banana")
        result = storage1.get_products()
        self.assertEqual(result, ["apple", "banana"])


if __name__ == "__main__":
    main()
  
