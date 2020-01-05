from django.shortcuts import render

from .models import PriceInput

from .forms import PriceInputForm
# Create your views here.
def price_list(request):
    '''Renders view of all previously registered price datasets
    '''
    query_results = PriceInput.objects.all()
    context = {
        'query_results':query_results
    }
    return render(request, "price_list.html", context)


def new_price(request):
    '''Renders form allowing users to input prices and 
    submit data to databse.
    '''
    if request.method == 'POST':
        if my_form.is_valid():
            PriceInput.objects.create(**my_form.cleaned_data)
            my_form = PriceInputForm()
    else: #if it's an initial rendering with method == GET, generate blank page
        my_form = PriceInputForm()

    context = {
        'form': my_form
    }
    return render(request, "price_input.html", context)

