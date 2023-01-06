from django.urls import path

from . import views

urlpatterns = [
    # path('', views.product_list_create_view),
    path('', views.ProddctMixinView.as_view()),
    path('<int:pk>/update/', views.product_update_view),
    path('<int:pk>/delete/', views.product_delete_view),
    path('<int:pk>/', views.ProddctMixinView.as_view()),
]