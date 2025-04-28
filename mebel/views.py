from django.db.models import Q
from django.views.generic import ListView, DetailView
from .models import Mebel, Slides, Category, Characteristics


class CategoryCharacteristics:
    def get_categorys(self):
        return Category.objects.all()

    def get_characteristics(self):
        return Characteristics.objects.all()


class MebelListView(CategoryCharacteristics, ListView):
    """Список мебели"""
    model = Mebel
    queryset = Mebel.objects.filter(draft=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['slides'] = Slides.objects.all()

        context['total_mebel'] = Mebel.objects.filter(draft=False).count()

        context['list'] = True
        context['self_link'] = True


        return context


class MebelDetailView(CategoryCharacteristics, DetailView):
    """Полное описание мебели"""
    model = Mebel
    slug_field = "url"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        mebel = self.get_object()

        context['category'] = mebel.category

        context['characteristics'] = mebel.characteristics.all()

        context['detail'] = True

        return context


class FilterMebelView(CategoryCharacteristics, ListView):

    def get_queryset(self):
        queryset = Mebel.objects.filter(
            Q(category__in=self.request.GET.getlist("category")) |
            Q(characteristics__in=self.request.GET.getlist("characteristic")),
        ).distinct()
        return queryset.distinct()  # Убираем дубликаты

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()

        categories = Category.objects.filter(mebel__in=queryset).distinct()

        context['categories'] = categories


        characteristics = Characteristics.objects.filter(mebel__in=queryset).distinct()

        context['characteristics'] = characteristics


        context['total_filtered_mebel'] = queryset.count()
        context['total_mebel'] = Mebel.objects.filter(draft=False).count()

        context['list'] = True
        context['is_new_is_hit_is_sale'] = True
        return context