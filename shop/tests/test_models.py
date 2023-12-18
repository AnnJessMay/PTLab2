from django.test import TestCase
from shop.models import Product, Purchase
from datetime import datetime


class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name="Стол", price=2000, quantity_on_stock=10)

    def test_correctness_types(self):
        self.assertIsInstance(Product.objects.get(name="Стол").name, str)
        self.assertIsInstance(Product.objects.get(name="Стол").price, int)
        self.assertIsInstance(Product.objects.get(name="Стол").quantity_on_stock, int)

    def test_correctness_data(self):
        self.assertTrue(Product.objects.get(name="Стол").price == 2000)
        self.assertTrue(Product.objects.get(name="Стол").quantity_on_stock == 10)


class PurchaseTestCase(TestCase):
    def setUp(self):
        self.product_table = Product.objects.create(name="Стол", price=2000, quantity_on_stock=10)
        Purchase.objects.create(product=self.product_table, person="Анна",
                                address="улица Дубова", price=2000,
                                quantity_purchased=1)

    def test_correctness_types(self):
        self.assertIsInstance(Purchase.objects.get(product=self.product_table).person, str)
        self.assertIsInstance(Purchase.objects.get(product=self.product_table).address, str)
        self.assertIsInstance(Purchase.objects.get(product=self.product_table).date, datetime)
        self.assertIsInstance(Purchase.objects.get(product=self.product_table).price, int)
        self.assertIsInstance(Purchase.objects.get(product=self.product_table).quantity_purchased, int)

    def test_correctness_data(self):
        self.assertTrue(Purchase.objects.get(product=self.product_table).person == "Анна")
        self.assertTrue(Purchase.objects.get(product=self.product_table).address == "улица Дубова")
        self.assertTrue(Purchase.objects.get(product=self.product_table).price == 2000)
        self.assertTrue(Purchase.objects.get(product=self.product_table).quantity_purchased == 1)
        