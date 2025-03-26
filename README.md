# 🍀 프로젝트명 ” fArmIng “ 🍀

## 🧑‍🌾 프로젝트 소개 

귀농 귀촌인이 늘어남으로써 처음 농사 짓는사람들은 처음에 실수를 할 경우 다시 회복하기 쉽지 않는 경우를 많이 보 았습니다. 그래서 농사를 시작하기전에 최소한의 필요한 사전조사를 쉽게 할 수 있도록 도와주는 AI 서비스 입니다.

AI 기반의 맞춤형 농업 지원 플랫폼으로, 사용자의 위치와 토양 데이터를 분석하여 최적의 작물을 추천하고, 농사에 필요한 퇴비 및 비료 정보를 제공하는 서비스입니다. 기존의 경험 중심 농사 방식에서 벗어나 데이터를 기반으로 한 스마트 농업을 실현하고자 합니다.

한 줄 정리 :  농사를 지으면서 필요한 데이터를 활용하여 작물, 비료를 추천해주는 AI 서비스

# Smart 8 팀원

- **김요한 (팀장)**  
  - API 및 PDF 데이터의 ChromaDB 인덱싱 및 저장 로직 구현  
  - 고급 검색을 위한 리트리버(Retriever) 시스템 구현

- **신제창 (부팀장)**  
  - JWT 기반 회원 기능 (가입, 로그인, 프로필)  
  - 백엔드 EC2 배포  
  - 프론트 S3 + CloudFront 배포  
  - HTTPS 적용 (Route53 + ACM)

- **맹주형 (서기)**  
  - LLM 및 Prompt 작성  
  - LangChain을 활용한 로직 구현
 
- **이현수 (서기)**  
  - WebSocket 기반 챗봇 구현  
  - 도커를 활용한 애플리케이션 및 레디스 컨테이너화  
  - 챗봇 UI 및 프론트엔드 개발

- **조규민 (총무)**  
  - WebSocket 기반 챗봇 구현  
  - WebSocket에서 JWT 인증 미들웨어 적용  
  - 챗봇 관리 및 운영


## 주요 기능

### **📌 주소 검색 및 토양 분석**

- 입력된 주소를 **법정동 코드**로 변환하여 해당 지역의 **토양 화학성 데이터** 조회
- 토양 분석 데이터를 활용하여 **배수등급, 토질 등급, pH, 유기물 함량 등** 제공

### **📌 작물 추천 및 농사 지원**

- 토양 환경과 사용자 입력 데이터를 분석하여 **적합한 작물 추천**
- 농작물별 적절한 **퇴비 및 비료 사용량 추천 → 사이트 연결**
- 농작물 선택 UI (과수류, 과채류, 근채류, 서류, 엽채류 등 카테고리 제공)

### **📌 농업 지원 서비스**

- 초보 농업인을 위한 농사 가이드 및 참고 자료 제공

### **📌 기상 정보 및 수익성 계산**

- **기상청 API 연동**을 통한 실시간 날씨 정보 제공

### **📌 회원 관리 및 개인화 서비스**

- **회원가입 및 로그인 (JWT 인증 적용)**
- 사용자의 **관심 작물 저장 및 관리 기능**
- 회원가입 시 농업 연차, 작물 선호도, 보유 장비 입력 기능
- 프로필 수정, 비밀번호 변경, 회원 탈퇴 기능 지원
- 소셜로그인 (카카오톡,구글) 연동

### **📌 데이터 저장 및 시스템 관리 → 현재 테스트 준비중.**

- PostgreSQL을 활용한 **사용자 정보, 작물 추천 데이터, 토양 분석 데이터 저장**
- API 호출 로그 저장 및 모니터링 기능
- 주기적인 **DB 백업 및 복구 시스템 구축**

### **📌 UI/UX 및 기타 기능**

- 반응형 웹 디자인 적용 (모바일 및 다양한 해상도 지원)
- 직관적인 검색 UI
- 사용자 피드백을 수집할 수 있는 **문의게시판 운영**
- 추천 API 연계 시 **외부 API 로고 삽입**

### **📌 추후 업데이트**

- **카카오 주소검색 API**를 활용한 주소 자동완성 기능 지원.
- 농작업 일정 생성 기능 (파종, 관리, 수확 일정 자동 생성)
- **추천 작물의 예상 수익성 계산 기능**
- **연차별(1년차, 3년 차, 7년 이상 등) 농업 지원사업 추천**
- 정부 및 지방자치단체의 **보조금, 지원금 정보 제공**
- 수익성 분석을 통해 **최적의 작물 선정 및 생산 계획 수립 지원**
- 사용자의 1년치 농사관련 정보를 입력하는 농영다이어리(리뷰페이지) 운영

# 서비스 아키텍처

![시스템아키텍처](https://github.com/user-attachments/assets/516a8208-ef61-49b2-a1ec-8371a38185fc)

## 기술 스택
### **🔹 백엔드 (Backend)**

- Python (Django, Django Rest Framework)
- PostgreSQL (데이터 저장 및 관리)
- JWT (회원 인증 및 보안)

### **🔹 프론트엔드 (Frontend)**

- HTML, CSS, JavaScript (추가적인 인터페이스 개선)

### **🔹 API 및 데이터 연동**

- V-WORD 주소검색 API
- 기상청 API (실시간 날씨 정보 제공)
- 정부 및 공공 API (농업 지원사업 정보 연동)

### **🔹 DB 관리**

- PostgrsSQL로 DB 저장 및 관리
- OCR을 활용하여 흙토람에서 제공된 pdf 파일의 이미지 텍스트에서 텍스트 추출
  
# 설치 및 실행 방법

## 1. 프로젝트 클론
```  git clone https://github.com/kimyohan9/smart_agriculture_Back_end.git
cd smart_agriculture_Back_end
``` 

## 2. 환경 변수 설정
```  .env 파일을 생성하고 필요한 설정 값을 추가합니다.
DB_URL=jdbc:mysql://localhost:3306/smart_agriculture
DB_USERNAME=root
DB_PASSWORD=yourpassword
JWT_SECRET=your_jwt_secret
```

## 3. 종속성 설치 및 빌드
```  ./mvnw clean install ``` 

## 4. 서버 실행
```  ./mvnw spring-boot:run ``` 
 
## API 문서
API 문서를 제공합니다. (https://docs.google.com/spreadsheets/d/1Xkh334sfGg3QoqF4LsRJbUZzoSNluGOqZHoSaY4zB0g/edit?gid=0#gid=0) 에서 확인할 수 있습니다. 

## 기여 방법
이 프로젝트를 포크합니다.
새로운 브랜치를 생성합니다 (feature/새로운기능).
변경 사항을 커밋합니다 (git commit -m 'Add 새로운 기능').
브랜치에 푸시합니다 (git push origin feature/새로운기능).
Pull Request를 생성합니다.

## 라이선스
이 프로젝트는 MIT 라이선스를 따릅니다.
