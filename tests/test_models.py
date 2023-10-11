from django.test import TestCase
from reservation.models import Booking, Menu
from decimal import Decimal
from datetime import datetime

class MenuTest(TestCase):

    def test_create_item(self):
        item = Menu.objects.create(
            title="IceCream",
            inventory=100,
            price=Decimal('80.00')
        )
        self.assertEqual(str(item), "IceCream : 80.00")

    def test_default_inventory(self):
        item = Menu.objects.create(
            title="Cake",
            price=Decimal('50.00')
        )
        self.assertEqual(item.inventory, 5)

class BookingTest(TestCase):

    def test_create_booking(self):
        time = datetime.now()
        booking = Booking.objects.create(
            name="John Doe",
            no_of_guests=4,
            booking_date=time
        )
        expected_str = "John Doe for 4 on " + str(time)
        self.assertEqual(str(booking), expected_str)

    def test_default_guests(self):
        time = datetime.now()
        booking = Booking.objects.create(
            name="Jane Doe",
            booking_date=time
        )
        self.assertEqual(booking.no_of_guests, 6)