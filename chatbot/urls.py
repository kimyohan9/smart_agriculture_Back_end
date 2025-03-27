from django.urls import path
from .views import (get_address_info_view,
                    get_soil_data,
                    crop_recommendation_view,
                    get_add_to_soil_data,
                    get_add_to_crop_recm,
                    )


appname = 'chatbot'



urlpatterns = [
    #### 
    path('address/', get_address_info_view, name='address_info'),
    path('soildata/', get_soil_data, name='soil_data'),
    path('recommendation/', crop_recommendation_view, name='crop_recommendation'),
    
    #### add to some
    path('add_to_soil/', get_add_to_soil_data, name='add_to_soil'),
    path('add_to_crop/', get_add_to_crop_recm, name='add_to_crop'),

]
