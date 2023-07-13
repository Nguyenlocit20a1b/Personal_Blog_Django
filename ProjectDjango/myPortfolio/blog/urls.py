from django.urls import path
from . import views
from .views import PostListView , PostDetail , PostDelete , PostUpdate 
urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('new/', views.PostCreate, name='create-post'),
    path('detail/<int:pk>/',PostDetail.as_view() ,name='post-detail'),
    path('update/<int:pk>/', PostUpdate.as_view(), name='post-update'),
    path('delete/<int:pk>/', PostDelete.as_view(), name='post-delete')
]