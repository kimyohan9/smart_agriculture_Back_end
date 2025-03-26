from django.urls import path
from .views import fetch_and_store, get_crawled_data,get_crop_html,get_crop_dropdown_data,crop_links

urlpatterns = [
    path("", fetch_and_store, name="crawl"),
    path('', get_crawled_data),  # POST 요청 받는 엔드포인트
    path("get-crop/", get_crop_html),  # ✅ 여기 추가
    path('get-crop-options/', get_crop_dropdown_data),  # 👈 추가
    path("get-links/", crop_links, name="crop_links"),

]
