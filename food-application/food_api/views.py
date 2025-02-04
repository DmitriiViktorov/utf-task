from django.db.models import Prefetch
from django.views.generic import ListView
from rest_framework.generics import ListAPIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from .models import Food, FoodCategory
from .serializers import FoodListSerializer


def get_published_categories():
    return FoodCategory.objects.filter(
            food__is_publish=True
        ).distinct().prefetch_related(
            Prefetch('food', queryset=Food.objects.filter(is_publish=True))
        )


class FoodListView(ListAPIView):
    renderer_classes = [JSONRenderer]  # Явно указываем, что выдаем JSON

    @extend_schema(
        summary='Get a list of published food categories',
        description='Returns a list of categories that have published foods.',
        responses=FoodListSerializer(many=True)
    )
    def get(self, request, *args, **kwargs):
        categories = get_published_categories()

        serializer = FoodListSerializer(categories, many=True)
        return Response(serializer.data)


class FoodListTemplateView(ListView):
    template_name = 'foods_list.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return get_published_categories()
