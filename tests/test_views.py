from django.test import TestCase

from reservation.models import Menu


class MenuViewTest(TestCase):
	def setUp(self):
		Menu.objects.create(title="Title1", price=1, inventory=1)
		Menu.objects.create(title="Title2", price=2, inventory=2)

	def test_getall(self):
		menu1 = Menu.objects.get(title="Title1")
		menu2 = Menu.objects.get(title="Title2")

		self.assertEqual(str(menu1), "Title1 : 1.00")
		self.assertEqual(str(menu2), "Title2 : 2.00")