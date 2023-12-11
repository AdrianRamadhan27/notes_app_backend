from django.urls import include, path
from . import views

app_name = "notes"

urlpatterns = [
    path('', views.index, name="index"),
    path('login', views.login_user, name="login_user"),
    path('signup', views.signup, name="signup"),
    path('notes_list', views.notes_list, name="notes_list"),
    path('notes/<int:note_id>/', views.notes, name="notes"),
    path('create_notes', views.create_notes, name="create_notes"),
    path('update_notes/<int:note_id>/', views.update_notes, name="update_notes"),
    path('manage_account', views.manage_account, name="manage_account"),
    path('logout/', views.logout_user, name='logout_user'),
    path('delete_notes/<int:note_id>/', views.delete_notes, name='delete_notes'),
]   
