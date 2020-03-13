from django.urls import include,path
from .views import *
from .models import *
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token


app_name = "cofferupApp"

router = routers.DefaultRouter(trailing_slash=False)
# router.register(r'coffers', Coffers, 'coffer')

urlpatterns = [
    path('', include(router.urls)),
    path('home', home, name='home'),
    path('coffers/mycoffers/', my_coffers_list, name = 'my_coffers'),
    # path('librarians/', librarian_list, name = 'librarians'),
    # path('libraries/', library_list, name='libraries'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout', logout_user, name='logout'),
    # path('book/form', book_form, name='book_form'),
    # path('library/form', library_form, name='library_form'),
    # path('books/<int:book_id>/', book_details, name='book'),
    # path('librarians/<int:librarian_id>', librarian_details, name = 'librarian'),
    # path('libraries/<int:library_id>', library_details, name='library'),
    # path('books/<int:book_id>/form/', book_edit_form, name='book_edit_form')
    path('register', user_register, name='user_register'),
    path('login', login_user),
]