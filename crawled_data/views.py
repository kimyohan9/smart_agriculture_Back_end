
from django.views.decorators.csrf import csrf_exempt

import json
from django.http import JsonResponse
from .crawl import crawl_and_save
from .utils import save_crawled_html  # 🧠 저장 함수 따로 만들었을 경우
from rest_framework.response import Response
from rest_framework.decorators import api_view
from crawled_data.models import BoardData  # ✅ 모델 임포트 먼저 해줘야 해!



@csrf_exempt
def fetch_and_store(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))
            cntns_no = data.get("cntns_no")
            if not cntns_no:
                return JsonResponse({"error": "cntns_no 값이 필요합니다."}, status=400)

            # 🔥 크롤링 실행
            html_content = crawl_and_save(cntns_no)

            # 🔥 static 폴더에 저장
            save_crawled_html(cntns_no)  # 🧠 저장 함수 따로 만들었을 경우

            return JsonResponse({"message": "크롤링 및 저장 완료!", "cntns_no": cntns_no})

        except json.JSONDecodeError:
            return JsonResponse({"error": "유효한 JSON 형식이 아닙니다."}, status=400)

    return JsonResponse({"error": "POST 요청만 허용됩니다."}, status=405)

@api_view(['POST'])
def get_crawled_data(request):
    
    return Response({"message": "테스트용 응답입니다."})

from crawled_data.models import BoardData  # ✅ 모델 임포트 먼저 해줘야 해!

@api_view(['POST'])
def get_crop_html(request):
    crop_name = request.data.get("crop_name")  # 프론트에서 받은 작물명 (예: 감자)

    if not crop_name:
        return Response({"error": "작물명이 없습니다."}, status=400)

    try:
        # 가장 최근에 저장된 해당 작물 데이터 불러오기
        data = BoardData.objects.filter(vegetablename=crop_name).last()

        if not data:
            return Response({"error": "해당 작물 정보가 없습니다."}, status=404)

        return Response({"html": data.tag, "name": data.vegetablename})

    except Exception as e:
        return Response({"error": str(e)}, status=500)

@api_view(['GET'])
def get_crop_dropdown_data(request):
    crops = BoardData.objects.values_list('vegetablename', flat=True)

    category_dict = {}
    for item in crops:
        if '-' in item:
            category, name = map(str.strip, item.split('-', 1))
            category_dict.setdefault(category, []).append(name)

    return Response(category_dict)

@api_view(["GET"])
def crop_links(request):
    data = {}
    all_data = BoardData.objects.values("vegetablename", "link")

    for item in all_data:
        category_crop = item["vegetablename"]  # ex) 밭농사 - 감자
        data[category_crop] = item["link"]

    return JsonResponse(data)