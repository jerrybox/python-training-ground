from django.conf.urls import url

from .views import get_province_list, get_country_list, get_city_list, region_initialize, region_update


urlpatterns = [
    # Django admin
    url(r'^initialize/', region_initialize, name='region_initialize'),
    url(r'^update/', region_update, name='region_update'),

    url(r'^province/', get_province_list, name='get_province_list'),
    url(r'^country/', get_country_list, name='get_country_list'),
    url(r'^city/', get_city_list, name='get_city_list'),
]
