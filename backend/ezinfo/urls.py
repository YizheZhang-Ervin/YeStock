from django.urls import path
from ezinfo.views import codingApi,codingApi2,translatorApi
from ezinfo.visualization import getDataFromDB,WebToDB,CSVToDB

app_name="ezinfo"
urlpatterns = [
    path('api/ssec/db/', getDataFromDB),
    path('api/ssec/csv/', CSVToDB),
    path('api/ssec/web/',WebToDB),
    path('api/coding/', codingApi.as_view()),
    path('api/coding2/', codingApi2.as_view()),
    path('api/translate/', translatorApi.as_view()),
]