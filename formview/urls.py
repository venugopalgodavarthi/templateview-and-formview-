from django.urls import path
from formview import views
urlpatterns=[
    path('',views.Formview.as_view(),name="formview")
]