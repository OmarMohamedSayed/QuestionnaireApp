from django.contrib import admin
from django.urls import path,include 
from app import views
from rest_framework import routers
from django.conf.urls import url
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()
router.register(r'questions', views.QuestionViewSet)
router.register(r'customeranswers', views.CustomerAnswerViewSet)
router.register(r'customers', views.CustomerView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/register/', views.RegisterView.as_view(), name="register"),
    path('api/login/', TokenObtainPairView.as_view()),
    path('api/token/refresh/',TokenRefreshView.as_view()),
]
