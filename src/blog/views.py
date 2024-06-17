from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Prefetch
from django.views.generic import ListView, DetailView
from blog.models import Post, Category


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.GET.get('category')
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset.select_related('category').order_by('-published_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.prefetch_related('posts').all()

        selected_category_id = self.request.GET.get('category')
        if selected_category_id:
            try:
                selected_category = Category.objects.get(id=selected_category_id)
                context['selected_category'] = selected_category
            except Category.DoesNotExist:
                pass

        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset