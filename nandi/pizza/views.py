from django.shortcuts import render
from .forms import pizzaform, multiplepizzaform
from django.forms import formset_factory

def home(request):
    return render(request, 'pizza/home.html')

def order(request):
    multiple_form = multiplepizzaform()
    if request.method == 'POST':
        filled_form = pizzaform(request.POST, request.FILES)
        if filled_form.is_valid():
            note = 'thanks %s %s %s' %(filled_form.cleaned_data['size'],
            filled_form.cleaned_data['topping1'],
            filled_form.cleaned_data['topping2'])
            new_form = pizzaform()
            return render(request, 'pizza/order.html',{'pizzaform':new_form,'note':note,'multiple_form':multiple_form})
            

    else:
        form = pizzaform()
        return render(request, 'pizza/order.html',{'pizzaform':form,'multiple_form':multiple_form})
    

def pizzas(request):
    number_of_pizzas = 2
    filled_multiple_pizza_form = multiplepizzaform(request.GET)
    if filled_multiple_pizza_form.is_valid():
        number_of_pizzas = filled_multiple_pizza_form.cleaned_data['number']
    pizzaformset = formset_factory(pizzaform, extra=number_of_pizzas)
    formset = pizzaformset()
    if request.method == 'POST':
        filled_formset = pizzaformset(request.POST)
        if filled_formset.is_valid():
            for form in filled_formset:
                print(form.cleaned_data['topping1'])

            note = 'pizzas have been ordred'

        else:
            note = 'order was not created suc'

        return render(request,'pizza/pizzas.html', {'note':note,'formset':formset})