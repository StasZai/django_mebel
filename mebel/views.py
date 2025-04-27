from django.views.generic import ListView, DetailView

from .models import Mebel, Slides, Category, Characteristics


class MebelListView(ListView):
    """Список мебели"""
    model = Mebel
    queryset = Mebel.objects.filter(draft=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['slides'] = Slides.objects.all()
        context['categorys'] = Category.objects.all()
        context['characteristics'] = Characteristics.objects.all()

        context['total_mebel'] = Mebel.objects.filter(draft=False).count()

        return context


class MebelDetailView(DetailView):
    """Полное описание мебели"""
    model = Mebel
    slug_field = "url"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        mebel = self.object

        context['category'] = mebel.category
        context['characteristics'] = mebel.characteristics.all()

        context['characteristics_flag'] = True

        return context