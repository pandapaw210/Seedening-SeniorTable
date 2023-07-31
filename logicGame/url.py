from django.urls import path

urlpatterns = [
    path('dots/', views.dots, name='dots'),
    path('freecell/', views.freecell, name='freecell'),
    path('hanoi/', views.hanoi, name='hanoi'),
]
