# views.py
from django.http import JsonResponse
from django.shortcuts import render
from .utils import address_info,soilexam,SoilExamRAG

def get_address_info_view(request):
    address = request.GET.get('address', '전라남도 해남군 산이면 덕송리 751')  # 디폴트 값 설정
    type = request.GET.get('type', 'PARCEL')  # 디폴트 값 설정
    
    if not address:
        return JsonResponse({"error": "주소를 입력해 주세요."}, status=400)
    
    add_info = address_info(type, address)
    if not add_info:
        return JsonResponse({"error": "유효하지 않은 주소입니다."}, status=400)
    
    return JsonResponse({"address_information": add_info})

def get_soil_data(request):
    PNU_Code = request.GET.get('address_information[id]', '4682041029107510000')
    if not PNU_Code:
        return JsonResponse({"error": "PNU_Code를 찾을 수 없습니다."}, status=400)
    
    rag_system = SoilExamRAG(PNU_Code=PNU_Code)
    soil_data = rag_system.fetch_soil_data()
    if not soil_data :
        return JsonResponse({"message": "토지 정보를 얻지 못하였습니다."}, status=404)
    
    return JsonResponse({"soil_data": soil_data})

def crop_recommendation_view(request):
    PNU_Code = request.GET.get('address_information[id]', '4682041029107510000')
    if not PNU_Code:
        return JsonResponse({"error": "PNU_Code를 찾을 수 없습니다."}, status=400)
    
    rag_system = SoilExamRAG(PNU_Code=PNU_Code)
    recommendation = rag_system.get_recommendation()
    if not recommendation:
        return JsonResponse({"message": "토지 정보를 얻지 못하였습니다."}, status=404)
    
    return JsonResponse({"recommendations": recommendation})