from django.urls import include, path
from . import views

app_name = "notes"

urlpatterns = [
    path('', views.index, name="index"),
    path('login', views.login, name="login"),
    path('signup', views.signup, name="signup"),
    path('notes_list', views.notes_list, name="notes_list"),
    path('notes', views.notes, name="notes"),
    path('create_notes', views.create_notes, name="create_notes"),
    path('update_notes', views.update_notes, name="update_notes"),
    path('manage_account', views.manage_account, name="manage_account")
]   
