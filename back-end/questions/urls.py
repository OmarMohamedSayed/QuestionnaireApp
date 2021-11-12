from django.contrib import admin
from django.urls import path,include 
from app import views
from rest_framework import routers
from django.conf.urls import url


router = routers.DefaultRouter()
router.register(r'questions', views.QuestionViewSet)
router.register(r'customers', views.CustomerViewSet)
router.register(r'customeranswers', views.CustomerAnswerViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    url(r'customeranswers/countanswers/(?P<pk>\d+)', views.CustomerAnswerViewSet.as_view({'get':'list'})),
]
