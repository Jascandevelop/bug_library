from django.urls import path
from bug_api.views import BugList, BugCreate, BugDetail

urlpatterns = [
    path('', BugCreate.as_view()),
    path('list/', BugList.as_view()),
    path('<int:pk>', BugDetail.as_view())  #<> means dynamic,type:name
]
