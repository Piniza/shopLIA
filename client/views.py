from django.shortcuts import render
from .import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from produit.models import Produit
from .models import UserProfile
from .forms import UserProfileForm, CustomUserCreationForm, SignupForm
from django.contrib.auth.models import User
from category.models import Category
# Create your views here.

@login_required
def search_feature(request):    
    defquery=request.session.get('defquery')
    sort_by = request.POST.get('sort_by', 'id')
    if request.method == 'POST':        
        search_query = request.POST.get('search_query', defquery)
        produits = Produit.objects.filter(name__icontains=search_query)          
        produits= produits.order_by(sort_by)   
        sort_by = request.POST.get('sort_by', 'id')
        request.session['defquery'] = search_query
        return render(request, 'client/search.html', {'query':search_query, 'produits':produits,'sort_by': sort_by})
    else:
        return render(request, 'client/espace_utilisateur.html')

@login_required
def espace_utilisateur(request):    
    categorie=Category.objects.all().order_by('-id')[:3]                
    return render(request, 'client/espace_utilisateur.html',{"categorie":categorie})

@login_required
def categories(request):
    category= Category.objects.all()
    return render(request, 'client/categories.html',{"category":category})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('firstName')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('espace_utilisateur')
    return render(request, 'client/login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # Create the User instance
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
            )
            # Create the UserProfile instance
            profile = UserProfile(
                user=user,
                address=form.cleaned_data['address'],
                gender=form.cleaned_data['gender']
            )
            profile.save()
            return redirect('login')  # You can define a URL for signup success
    else:
        form = SignupForm()
    return render(request, 'client/signup.html', {'form': form})