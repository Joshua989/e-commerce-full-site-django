from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login, logout
from .models import Product, Category


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)  # Log in the user after registration
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'products/register.html', {'form': form})






def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'products/login.html', {'error': 'Invalid credentials'})
    return render(request, 'products/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')


def home(request):
    return render(request, 'products/home.html')

def product_list(request):
    categories = Category.objects.all()
    products = Product.objects.filter(is_active=True)

    # Filter by category
    category_slug = request.GET.get('category')
    if category_slug:
        products = products.filter(category__slug=category_slug)

    # Filter by price range
    price_min = request.GET.get('price_min')
    price_max = request.GET.get('price_max')
    if price_min:
        products = products.filter(price__gte=price_min)
    if price_max:
        products = products.filter(price__lte=price_max)

    return render(request, 'products/product_list.html', {
        'categories': categories,
        'products': products,
    })


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)[:4]

    return render(request, 'products/product_detail.html', {
        'product': product,
        'related_products': related_products,
    })