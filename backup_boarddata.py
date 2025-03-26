import json
from django.core.serializers import serialize
from crawled_data.models import BoardData

# 직렬화
data = serialize("json", BoardData.objects.all(), indent=2)

# 파싱 → 저장
parsed = json.loads(data)
with open("boarddata_backup.json", "w", encoding="utf-8") as f:
    json.dump(parsed, f, ensure_ascii=False, indent=2)

print("✅ BoardData 백업 완료!")
