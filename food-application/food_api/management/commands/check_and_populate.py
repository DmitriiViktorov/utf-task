from django.core.management import BaseCommand
from django.db import connection, transaction
from food_api.models import Food, FoodCategory

class Command(BaseCommand):
    help = 'Check if tables exists and are empty, then populate with initial data'

    def handle(self, *args, **options):
        self.check_and_populate()

    def check_and_populate(self):
        tables_names = connection.introspection.table_names()

        required_tables = ["food_api_food", "food_api_foodcategory"]

        for table in required_tables:
            if table not in tables_names:
                self.stdout.write(self.style.ERROR("Table '{}' not found, skipping...".format(table)))
                return

        if Food.objects.exists() and FoodCategory.objects.exists():
            self.stdout.write(self.style.ERROR('Tables are not empty. Initial data will not be populated.'))
            return

        self.populate_init_data()

    @transaction.atomic
    def populate_init_data(self):
        categories = [
            {'name_ru': 'Напитки', 'order_id': 10},
            {'name_ru': 'Выпечка', 'order_id': 20},
            {'name_ru': 'Основные блюда', 'order_id': 30},
            {'name_ru': 'Десерты', 'order_id': 40},
        ]

        foods = [
            {'category_id': 1, 'internal_code': 100, 'code': 1, 'name_ru': 'Чай', 'description_ru': 'Чай 100 гр', 'cost': '123.00', 'is_publish': True},
            {'category_id': 1, 'internal_code': 200, 'code': 2, 'name_ru': 'Кола', 'description_ru': 'Кола', 'cost': '123.00', 'is_publish': False},
            {'category_id': 2, 'internal_code': 300, 'code': 3, 'name_ru': 'Пирожок', 'description_ru': 'Пирожок с капустой', 'cost': '50.00', 'is_publish': True},
            {'category_id': 3, 'internal_code': 400, 'code': 4, 'name_ru': 'Борщ', 'description_ru': 'Борщ украинский', 'cost': '80.00', 'is_publish': True},
            {'category_id': 4, 'internal_code': 500, 'code': 5, 'name_ru': 'Тирамису', 'description_ru': 'Тирамису классический', 'cost': '200.00', 'is_publish': False},
            {'category_id': 4, 'internal_code': 600, 'code': 6, 'name_ru': 'Чизкейк', 'description_ru': 'Чизкейк с малиной', 'cost': '180.00', 'is_publish': False},
        ]

        for category in categories:
            FoodCategory.objects.create(**category)

        for food in foods:
            Food.objects.create(**food)

        self.stdout.write(self.style.SUCCESS('Data populated successfully.'))