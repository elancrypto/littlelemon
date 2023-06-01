from django.test import TestCase
from restaurant.models import Menu

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(Title="IceCream", Price=80, Inventory=100)
        expected_result = "IceCream : 80"
        self.assertEqual(str(item), expected_result)
