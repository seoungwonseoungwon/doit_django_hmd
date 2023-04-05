from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

# Create your views here.
# def index(request):

#     posts = Post.objects.all().order_by('-pk')



#     return render(
#         request,
#         'blog/index.html',
#         {
#             'posts':posts,
#         }
#     )

class PostList(ListView):
    model = Post
    ordering = '-pk'
    # post_list.html : class이름_list.html 내부적으로 정의가 되어있기 때문에 생략 가능
    # 파일명을 위에 있는 규칙으로 하지 않을 경우 명시해줘야함 .
    # template_name = 'blog/post_list.html'

def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)

    return render(
        request,
        'blog/single_post_page.html',
        {
            'post':post,
        }
    )