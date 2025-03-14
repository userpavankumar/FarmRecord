from django.urls import path
from . import views



urlpatterns = [
    
    # rendering Page routes
    path(route='', view=views.index_view, name=''), 
    
    path(route='check_connection/', view=views.check_connection, name='cc'),
    
    ## functionality routes    
    path(route='sw/', view=views.save_work, name='aw'),
    path(route='ap/', view=views.add_production, name='ap'),
    path(route='ew/', view=views.edit_work, name='ew'),
    path(route='dw/', view=views.delete_work, name='dw'),
    path(route='fetch/all_work/', view=views.view_all_work, name='vaw'),
     
]  

