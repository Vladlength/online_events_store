from django.shortcuts import render
from .forms import CreateEventForm, CreateEventPrice
from event_information import models
from django.urls import reverse_lazy
from django.shortcuts import redirect


def main_creation(request):
    # нужен объект модели для дальнейшей привязки обЪекта формы
    form = CreateEventForm()

    if request.method == 'POST':
        form = CreateEventForm(request.POST, request.FILES)

        #     output tied to field maker_id something like that
        if form.is_valid():
            form.save()
    prices = models.EventPrice.objects.all()
    # prescribe the case when validity does not pass
    context = {
        'form': form,
        'prices': prices
    }

    return render(request, 'main_creation.html', context)


def create_price(request):
    form = CreateEventPrice()

    if request.method == 'POST':
        form = CreateEventPrice(request.POST)

        #     output tied to field maker_id something like that
        if form.is_valid():
            form.save()

    prices = models.EventPrice.objects.all()
    # prescribe the case when validity does not pass
    context = {
        'form': form,
        'prices': prices
    }

    return render(request, 'price_creation.html', context)

# def my_form_submit(request):
#     if request.method == 'POST':
#         form = MyForm(request.POST)
#         if form.is_valid():
#             # Обработка данных формы
#             return redirect('my_success_page')
#     else:
#         form = MyForm()
#     return render(request, 'my_template.html', {'form': form})
