from django.urls import path
from . import views

urlpatterns = [
    path('search/<str:q>/', views.PostSearch.as_view()),
    # path('<int:pk>/', views.single_post_page, name='single_post_page'),
    path('<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('', views.PostList.as_view(), name='post_list'),
    path('category/<str:slug>/', views.category_page, name='category_filter'),
    path('tag/<str:slug>/', views.tag_page),
    path('create_post/', views.PostCreate.as_view()),

    # url주소에 /blog/update_post/포스트아이디숫자를 넣으면 views.py안에 PostUpdate 클래스를 실행하게함
    path('update_post/<int:pk>/', views.PostUpdate.as_view()),

    # pk/new_comment 들어가면 views안에있는 new_comment 함수 실행
    path('<int:pk>/new_comment/', views.new_comment),

    # update_comment/pk 주소에 들어오면 views안에 CommentUpdate 클래스 실행함
    path('update_comment/<int:pk>/', views.CommentUpdate.as_view()),

]