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

    # url주소에 /blog/update_post/포스트아이디숫자를 넣으면 views.py에 PostUpdate 클래스를 실행하게함
    path('update_post/<int:pk>/', views.PostUpdate.as_view()),

]