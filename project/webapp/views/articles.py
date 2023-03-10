from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from webapp.forms import ProjectForm
from webapp.models import Project


class ArticleCreateView(CreateView):
    template_name = 'article_create.html'
    model = Project
    form_class = ProjectForm
    print('article_create.html')

    def get_success_url(self):
        return reverse('article_detail', kwargs={'pk': self.object.pk})




class ArticleDetail(DetailView):
    template_name = 'article.html'
    model = Project



class ArticleUpdateView(UpdateView):
    template_name = 'article_update.html'
    form_class = ProjectForm
    model = Project

    def get_success_url(self):
        return reverse('article_detail', kwargs={'pk':self.object.pk})


class ArticleDeleteView(DeleteView):
    template_name = 'article_confirm_delete.html'
    model = Project
    success_url = reverse_lazy('index')