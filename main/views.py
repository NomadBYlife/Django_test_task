from django.db.models import Prefetch
from django.shortcuts import render
from django import views

from .forms import FormForID
from .models import Product, Credit


class MainView(views.View):
    """Главная вью"""

    def get(self, request, *args, **kwargs):
        form = FormForID()
        context = {
            'form': form,
        }
        return render(request, 'main/main.html', context)

    def post(self, request, *args, **kwargs):
        form = FormForID()
        results = Credit.objects.prefetch_related(
            Prefetch(
                'credit', Product.objects.prefetch_related(
                    'manufacturer'
                )
            )
        ).filter(id=request.POST['id'])
        my_list = []
        for res in results:
            for i in res.credit.all():
                my_list.append(i.manufacturer.id)
        task = list(set(my_list))
        context = {
            'form': form,
            'results': results,
            'task': task,
        }
        return render(request, 'main/main.html', context)
