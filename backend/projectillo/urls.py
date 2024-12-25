from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.views.generic import RedirectView

from .views import(
    ProjectViewSet,
    Register_view,
    Login_view,
    Logout_view,
    TaskViewSet,
    ProfileViewSet,
    index
)
from django.views.generic import TemplateView

from django.contrib.auth.decorators import login_required

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'Tasks', TaskViewSet)
router.register(r'users', ProfileViewSet)
urlpatterns = [

    path('', index.as_view(), name = 'index'),

    # registration and login
    path('login/', Login_view.as_view(), name = "login"),
    path('register/', Register_view.as_view(), name = "registration"),

    # api routes 
    path('api/', include(router.urls), name ="api_view"),

  

]
