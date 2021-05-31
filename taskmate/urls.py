
from django.contrib import admin
from django.urls import path,include
from todolist_app import views as todolist_views
#from users_app import views as users_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todolist_views.index,name='index'),
    path('account/',include('users_app.urls')),
    path('todolist/',include('todolist_app.url')),
    path('contact_us', todolist_views.contacts,name='contact_us'),
    path('about_us', todolist_views.about,name='about_us'),

]
