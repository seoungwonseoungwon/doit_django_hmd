from django.urls import path
from . import views

urlpatterns = [
    # path('<int:pk>/', views.single_post_page, name='single_post_page'),
    path('<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('', views.PostList.as_view(), name='post_list'),
    path('category/<str:slug>/', views.category_page, name='category_filter'),
    path('tag/<str:slug>/', views.tag_page),

]