from django.shortcuts import render
from django.views.generic import DetailView, TemplateView
from .models import *
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.utils.translation import gettext as _

# Create your views here.
class HomePageView(DetailView):
    template_name = '_main.html'
    model = ArticleModel

    def get_context_data(self, **kwargs):
        ctxt = super().get_context_data()
        ctxt["object_list"] = ArticleModel.objects.all()
        return ctxt
    
    # オーバーライド
    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        
        # request に 合致するデータを取得
        # return get_object_or_404(User, pk=self.request.session['user_id'])
        pk = self.kwargs.get(self.request)
        if pk is not None:
            queryset = queryset.filter(pk=pk)
        
        try:
            # Get the single item from the filtered queryset
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404(
                _("No %(verbose_name)s found matching the query")
                % {"verbose_name": queryset.model._meta.verbose_name}
            )
        return obj

class index_view(TemplateView):
    template_name="index.html"

    def get_context_data(self, **kwargs):
        ctxt = super().get_context_data()
        ctxt["user_list"] = User.objects.all()
        return ctxt
