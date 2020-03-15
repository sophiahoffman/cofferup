from django.urls import include,path
from .views import *
from .models import *

app_name = "cofferupApp"

urlpatterns = [
    path('', home, name='home'),
    path('coffers/mycoffers/', my_coffers_list, name = 'my_coffers'),
    path('coffers', coffers_list, name = 'coffers'),
    path('profile', user_detail, name='profile'),
    path('accounts', include('django.contrib.auth.urls')),
    path('logout', logout_user, name='logout'),
    path('coffers/form', coffer_form, name='coffer_form'),
    path('profile/form', profile_form, name='profile_form'),
    path('coffers/<int:book_id>/', coffer_detail, name='coffer'),
    path('coffers/mysettledcoffers', my_settled_coffers_list, name = 'my_settled_coffers'),
    # path('libraries/<int:library_id>', library_details, name='library'),
    # path('books/<int:book_id>/form/', book_edit_form, name='book_edit_form')
    path('register', user_register, name='user_register'),
    path('login', login_user),
]