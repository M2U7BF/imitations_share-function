from django.shortcuts import render
from django.views.generic import DetailView, TemplateView
from .models import *
from django.shortcuts import render, get_object_or_404

# Create your views here.
class HomePageView(DetailView):
    template_name = '_main.html'
    model = ArticleModel

    def get_context_data(self, **kwargs):
        ctxt = super().get_context_data()
        ctxt["object_list"] = ArticleModel.objects.all()
        return ctxt
    
    def get_object(self):
        return get_object_or_404(User, pk=self.request.session['user_id'])

class index_view(TemplateView):
    template_name="index.html"

    def get_context_data(self, **kwargs):
        ctxt = super().get_context_data()
        ctxt["user_list"] = User.objects.all()
        return ctxt
