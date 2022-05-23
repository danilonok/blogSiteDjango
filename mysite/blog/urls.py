from django.urls import path

from . import views
app_name = 'blog'
urlpatterns = [
    path(r'', views.index, name = "index"),
    path('<int:post_id>/', views.post, name = 'post'),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("create_post", views.create_post, name="create_post"),
    path("<int:post_id>/edit_post", views.edit_post, name="edit_post"),
    path("<int:post_id>/delete_post", views.delete_post, name="delete_post"),
    path("category_posts/<int:category_id>", views.category_posts, name="category_posts"),

]