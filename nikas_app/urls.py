from django.urls import path
from .views import view_name
from .views import view_name1
from .views import view_name2
from .views import view_name3
from .views import archive_view



urlpatterns = [
    path('', view_name),
    path('<int:art_num>/', archive_view, name='archives'),
    path('<int:art_num>/<slug:slug_text>/', archive_view, name='archives')

]
