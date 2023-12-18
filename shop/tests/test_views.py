from django.test import TestCase, Client

from shop.models import Product, Purchase


class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.product_table = Product.objects.create(name="Стол", price=2000, quantity_on_stock=10)
        self.product_chair = Product.objects.create(name="Стул", price=1000, quantity_on_stock=7)

    def test_webpage_accessibility(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_purchase(self):
        x = self.client.post('/purchase', data={f'quantity {self.product_table.id}': ['1'],
                                    f'quantity {self.product_chair.id}': ['1'],
                                            'person': ['Анна'],
                                            'address': ['улица Дубова']})
        self.assertEqual(x.context["total_cost"], self.product_table.price + self.product_chair.price)
