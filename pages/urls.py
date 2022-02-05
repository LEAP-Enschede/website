from django.urls import path
from . import views

app_name = 'pages'
urlpatterns = [
    path('<str:page_url>', views.page, name='page'),
]
