"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views



urlpatterns = [
    #### default
    path("admin/", admin.site.urls),
    
    
    #### App with db
    path("users/", include("users.urls")),
    path("post/", include("post.urls")),  # ✅ 기존 post API
    
    
    #### App
    path("crawled_data/", include("crawled_data.urls"), name="crawl"),
    path("chatbot/", include("chatbot.urls")),
    
    
    #### etc - 앱이 장고내에서는 안보이는데 삭제된 기능? 확인 필요
    # path("accounts/login/", auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    # path("accounts/", include("allauth.urls")),
    # path("api/", include("smart_agriculture_Back_end.post.api_urls")),  # ✅ 추가된 API 경로
    
]
