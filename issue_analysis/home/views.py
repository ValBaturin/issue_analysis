from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from home.forms import HomeForm
from home.models import Post


class HomeView(TemplateView):
    template_name = 'home/add.html'

    def get(self, request):
        form = HomeForm()
        args = {
            'form': form
        }
        return render(request, self.template_name, args)

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            text = form.cleaned_data['post']
            form = HomeForm()
            return redirect('home:add')

        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)

class AllView(TemplateView):
    template_name = 'home/all.html'

    def get(self, request):
        posts = Post.objects.all().order_by('-created')
        args = {
            'posts': posts
        }
        return render(request, self.template_name, args)

class OwnView(TemplateView):
    template_name = 'home/own.html'

    def get(self, request):
        posts = Post.objects.filter(user=request.user).order_by('-created')
        args = {
            'posts': posts
        }
        return render(request, self.template_name, args)
