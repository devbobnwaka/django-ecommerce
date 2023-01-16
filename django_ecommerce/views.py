from django.shortcuts import render
from django.core.paginator import Paginator
from store.models import Product, ProductImage
# Create your views here.

def home(request):
    # del request.session['slug']
    # request.session.flush()
    # request.session.modified = True
    # for key, value in request.session.items():
    #     print('{} => {}'.format(key, value))

    product_qs = Product.objects.all()
    paginator = Paginator(product_qs, 10)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    for product in products:
        print(product.productimage_set.first())
        
    context = {
        "products":products
    }

    return render(request, 'home.html', context)