import random
from decimal import Decimal

from django.contrib.auth.hashers import make_password
from django.core.management.base import BaseCommand
from django.db import transaction
from faker import Faker

from customer.models import Customer
from orders.models import Order
from product.models import category, Product
from suppliers.models import Supplier
from user.models import Role, User

CATEGORY_NAMES = [
    "Electronics", "Groceries", "Furniture", "Apparel", "Stationery",
    "Toys", "Beauty", "Automotive", "Sports", "Books",
    "Home Appliances", "Garden", "Pet Supplies", "Health", "Music",
]

ROLE_NAMES = ["Admin", "Manager", "Staff"]


class Command(BaseCommand):
    help = "Seed database with fake data"

    def add_arguments(self, parser):
        parser.add_argument("--users", type=int, default=10)
        parser.add_argument("--categories", type=int, default=10)
        parser.add_argument("--products", type=int, default=20)
        parser.add_argument("--suppliers", type=int, default=8)
        parser.add_argument("--customers", type=int, default=15)
        parser.add_argument("--orders", type=int, default=10)
        parser.add_argument("--flush", action="store_true", help="Clear existing data first")

    @transaction.atomic
    def handle(self, *args, **options):
        fake = Faker()

        if options["flush"]:
            self._clear_data()

        roles = self._seed_roles()
        users = self._seed_users(fake, options["users"], roles)
        categories = self._seed_categories(fake, options["categories"])
        products = self._seed_products(fake, options["products"], categories)
        suppliers = self._seed_suppliers(fake, options["suppliers"])
        customers = self._seed_customers(fake, options["customers"])
        orders = self._seed_orders(fake, options["orders"], customers, products)

        self.stdout.write(self.style.SUCCESS(
            f"Seeded: {len(users)} users, {len(categories)} categories, "
            f"{len(products)} products, {len(suppliers)} suppliers, "
            f"{len(customers)} customers, {len(orders)} orders."
        ))

    def _clear_data(self):
        Order.objects.all().delete()
        Product.objects.all().delete()
        category.objects.all().delete()
        User.objects.all().delete()
        Role.objects.all().delete()
        Supplier.objects.all().delete()
        Customer.objects.all().delete()

        self.stdout.write(self.style.WARNING("All existing data cleared."))

    def _seed_roles(self):
        return [Role.objects.get_or_create(name=name)[0] for name in ROLE_NAMES]

    def _seed_users(self, fake, count, roles):
        users = []
        for _ in range(count):
            user, created = User.objects.get_or_create(
                email=fake.unique.email(),
                defaults={
                    "name": fake.name(),
                    "phone": fake.phone_number()[:15],
                    "password": make_password("password123"),
                    "address": fake.address(),
                    "role": random.choice(roles),
                }
            )
            if created:
                users.append(user)
        return users

    def _seed_categories(self, fake, count):
        names = random.sample(CATEGORY_NAMES, k=min(count, len(CATEGORY_NAMES)))

        while len(names) < count:
            names.append(fake.unique.word().capitalize())

        categories = []
        for name in names:
            obj, _ = category.objects.get_or_create(
                name=name,
                defaults={
                    "description": fake.sentence(),
                    "expiry_date": fake.date_time_this_year(),
                }
            )
            categories.append(obj)

        return categories

    def _seed_products(self, fake, count, categories):
        if not categories:
            categories = list(category.objects.all())

        products = []
        for _ in range(count):
            selected_category = random.choice(categories) if categories else None
            product = Product.objects.create(
                name=fake.unique.catch_phrase(),
                description=fake.sentence(),
                price=Decimal(f"{random.uniform(5, 999):.2f}"),
                category=selected_category.name if selected_category else "",
            )
            products.append(product)

        return products

    def _seed_suppliers(self, fake, count):
        suppliers = []
        for _ in range(count):
            supplier, created = Supplier.objects.get_or_create(
                email=fake.unique.company_email(),
                defaults={
                    "name": fake.company(),
                    "phone": fake.phone_number()[:20],
                    "address": fake.address(),
                    "is_active": True,
                }
            )
            if created:
                suppliers.append(supplier)

        return suppliers

    def _seed_customers(self, fake, count):
        customers = []
        for _ in range(count):
            customer, created = Customer.objects.get_or_create(
                email=fake.unique.email(),
                defaults={
                    "name": fake.name(),
                    "phone": fake.phone_number()[:15],
                    "address": fake.address(),
                }
            )
            if created:
                customers.append(customer)

        return customers

    def _seed_orders(self, fake, count, customers, products):
        if not customers or not products:
            self.stdout.write(self.style.WARNING(
                "Skipping orders: Need at least one customer and product."
            ))
            return []

        statuses = [choice[0] for choice in Order.OrderStatus.choices]
        orders = []

        for _ in range(count):
            order = Order.objects.create(
                customer=random.choice(customers),
                order_date=fake.date_this_year(),
                status=random.choice(statuses),
            )

            order.order_details.set(
                random.sample(products, k=random.randint(1, min(4, len(products))))
            )

            orders.append(order)

        return orders

