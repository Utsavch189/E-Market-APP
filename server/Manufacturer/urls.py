from django.urls import path
from .views import *

urlpatterns = [
    path('get_products',get_products),
    path('set_delete_update_products',set_delete_update_products),
    path('entry_production',entry_production),
    path('a_user',a_user),
    path('distribute',distribute),
    path('DayByDayEntry',DayByDayEntry),
    path('post_dayBYdayDistribute',post_dayBYdayDistribute),
    path('get_dayBYdayDistribute',get_dayBYdayDistribute),
    path('get_DayByDayEntry',get_DayByDayEntry)
]
