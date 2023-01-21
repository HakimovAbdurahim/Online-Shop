from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django import shortcuts
# Project
from .models import Category, Product


class ProductListView(ListView):
    queryset = Category.objects.all()
    template_name = 'product/list.html'

    def get(self, request, category_slug=None):
        self.category = None
        self.products = Product.objects.filter(available=True)
        if category_slug:
            self.category = get_object_or_404(self.queryset, slug=category_slug)
            self.products = self.products.filter(category=self.category)
        context = {'category': self.category, 'categories': self.queryset, 'products': self.products}
        return render(request, 'product/list.html', context)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/detail.html'

    def get(self, request, id, slug):
        self.product = get_object_or_404(self.model, id=id, slug=slug,
                                         available=True)
        context = {'product': self.product}
        return render(request, 'product/detail.html', context)
