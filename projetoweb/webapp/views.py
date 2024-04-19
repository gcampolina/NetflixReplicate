from django.shortcuts import render, redirect
from .models import Filme
from django.db.models import Q
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import CustomUser
from django.contrib.auth.decorators import login_required
from .forms import FotoPerfilForm
# Create your views here.
def home(request):
    filmes_lancamento  = Filme.objects.filter(lancamento='SIM')
    filmes_original = Filme.objects.filter(original_netflix='SIM')
    context = {
        'filmes_lancamento': filmes_lancamento,
        'filmes_original': filmes_original,
    }
    return render(request,'home.html', context)


def filmes_original(request):
    filmes = Filme.objects.filter(original_netflix='SIM')  # Filtra filmes que são originais netflix
    return render(request, 'home.html', {'filmes': filmes})

def filmes_lancamento(request):
    filmes = Filme.objects.filter(lancamento='SIM')  # Filtra filmes que são lançamentos
    return render(request, 'home.html', {'filmes': filmes})

def conta(request):
    return render(request,'conta.html')

def login_view(request):
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            # Redirecione para a página desejada após o login
            return redirect('home')
        else:
            messages.error(request, 'Usuário ou senha inválido')
           
    
    return render(request, 'login.html')

@login_required
def conta(request):
    if request.method == 'POST':
        form = FotoPerfilForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('conta')  # Redireciona para a mesma página para ver as mudanças
    else:
        form = FotoPerfilForm(instance=request.user)

    # Passe tanto o formulário quanto o usuário para o contexto
    context = {'form': form, 'usuario': request.user}
    return render(request, 'conta.html', context)




def cadastro(request):
   

    if request.method == "POST":
        username = request.POST.get('username')
        nome = request.POST.get('name')
        email = request.POST.get('email')
        senha = request.POST.get('password')
        confirmacao_senha = request.POST.get('password2')

        if senha != confirmacao_senha:
            messages.warning(request, 'As senhas não coincidem.')
            
        else:
            user = CustomUser.objects.filter(username=username).first()

            if user:
                messages.warning(request, 'O usuário fornecido já está em uso.')
                
            else:
                user = CustomUser.objects.create_user(username=username, email=email, password=senha)
                user.first_name = nome
                user.save()

                return redirect('home')  # Redirecione para a página desejada após o cadastro

    return render(request, 'cadastro.html')