from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Article
def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})
def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404
def create_post(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = {'text': request.POST.get("text", ""), 'title': request.POST.get("title", "")}
            if form["text"] and form["title"]:
                if Article.objects.filter(title=form["title"]).exists():
                    form['errors'] = "Статья с таким названием уже существует"
                    return render(request, 'create_post.html', {'form': form})
                article = Article.objects.create(text=form["text"], title=form["title"], author=request.user)
                return redirect('get_article', article_id=article.id)
            else:
                form['errors'] = "Не все поля заполнены"
                return render(request, 'create_post.html', {'form': form})
        else:
            return render(request, 'create_post.html', {})
    else:
        return redirect('login')
def register(request):
    if request.method == "POST":
        form = {
            'username': request.POST.get("username", ""),
            'email': request.POST.get("email", ""),
            'password': request.POST.get("password", "")
        }
        if form['username'] and form['password'] and form['email']:
            if User.objects.filter(username=form['username']).exists():
                form['errors'] = "Пользователь с таким именем уже существует"
                return render(request, 'registration.html', {'form': form})
            user = User.objects.create_user(form['username'], form['email'], form['password'])
            login(request, user)
            return redirect('archive')
        else:
            form['errors'] = "Не все поля заполнены"
            return render(request, 'registration.html', {'form': form})
    return render(request, 'registration.html', {})
def login_user(request):
    if request.method == "POST":
        form = {
            'username': request.POST.get("username", ""),
            'password': request.POST.get("password", "")
        }
        if form['username'] and form['password']:
            user = authenticate(username=form['username'], password=form['password'])
            if user is not None:
                login(request, user)
                return redirect('archive')
            else:
                form['errors'] = "Нет аккаунта с таким сочетанием никнейма и пароля"
                return render(request, 'login.html', {'form': form})
        else:
            form['errors'] = "Введите логин и пароль"
            return render(request, 'login.html', {'form': form})
    return render(request, 'login.html', {})
def logout_user(request):
    logout(request)
    return redirect('archive')