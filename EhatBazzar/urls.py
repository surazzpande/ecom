from django.urls import path
from EhatBazzar import views

#TEMPLATE

app_name = 'EhatBazzar'

urlpatterns =[

    path('',views.index , name = "index"),
    path('about/',views.about , name ="about"),
    path('product/', views.product , name="product"),
    path('register/',views.register, name='register'),
    path('user_login/',views.user_login,name='user_login'),
]