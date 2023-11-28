from django import forms
from django.forms import ModelForm


from .models import pizza, size


# class pizzaform(forms.Form):
#     # topping = forms.MultipleChoiceField(choices=[('pep','peperoni'),('chese','chese'),('olives','olives')],widget = forms.CheckboxSelectMultiple)
#     topping1 = forms.CharField(label = 'topping 1', max_length = 250)
#     topping2 = forms.CharField(label = 'topping 2', max_length = 250)
#     size = forms.ChoiceField(label = 'size', choices = [('small','small'),('mediom','mediom'),('larg','larg')])


class pizzaform(forms.ModelForm):
    # size = forms.ModelChoiceField(queryset=size.objects, empty_label=None, widget=forms.RadioSelect)
    # image = forms.ImageField()
    class Meta:
        model = pizza
        fields = ['topping1','topping2','size']
        labels = {'topping1':'Topping 1','topping2':'Topping 2'}



class multiplepizzaform(forms.Form):
    number = forms.IntegerField(min_value=2, max_value=6)
                        