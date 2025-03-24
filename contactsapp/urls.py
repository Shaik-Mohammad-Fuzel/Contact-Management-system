from django.urls import path
from .views import add_contact,dashboard,update_contact,delete_contact,search_contact,view_contact

urlpatterns = [

    path("", dashboard, name="dashboard"),
    path("add/", add_contact, name="add_contact"),
    #path("list/", contact_list, name="contact_list"),
    path("update/<int:pk>/", update_contact, name="update_contact"),
    path("delete/<int:pk>/", delete_contact, name="delete_contact"),
    path("search/",search_contact,name="search_contact"),
    path("view/<int:pk>/", view_contact, name="view_contact"),
]
