# 🍀 프로젝트명 ” fArmIng “ 🍀

## 🧑‍🌾 프로젝트 소개

귀농 귀촌인이 늘어남으로써 처음 농사 짓는사람들은 처음에 실수를 할 경우 다시 회복하기 쉽지 않는 경우를 많이 보 았습니다. 그래서 농사를 시작하기전에 최소한의 필요한 사전조사를 쉽게 할 수 있도록 도와주는 AI 서비스 입니다.

AI 기반의 맞춤형 농업 지원 플랫폼으로, 사용자의 위치와 토양 데이터를 분석하여 최적의 작물을 추천하고, 농사에 필요한 퇴비 및 비료 정보를 제공하는 서비스입니다. 기존의 경험 중심 농사 방식에서 벗어나 데이터를 기반으로 한 스마트 농업을 실현하고자 합니다.

한 줄 정리 :  농사를 지으면서 필요한 데이터를 활용하여 작물, 비료를 추천해주는 AI 서비스

## 주요 기능
센서 데이터 수집 및 저장: 온도, 습도, 토양 수분 등의 데이터를 실시간으로 수집하고 저장
사용자 관리: 회원가입, 로그인 및 인증 시스템 제공
농업 환경 모니터링: 수집된 데이터를 분석하여 사용자에게 알림 및 대시보드 제공
자동화 제어: 특정 조건이 충족될 경우 자동으로 농업 장비를 제어
API 제공: RESTful API를 통해 외부 시스템과 연동 가능

## 기술 스택
언어: Java (Spring Boot)
데이터베이스: MySQL
서버 프레임워크: Spring Boot
인증 및 보안: JWT (JSON Web Token)
기타: JPA, Hibernate, Swagger API 문서화, Docker

#설치 및 실행 방법

## 1. 프로젝트 클론
git clone https://github.com/kimyohan9/smart_agriculture_Back_end.git
cd smart_agriculture_Back_end

## 2. 환경 변수 설정
.env 파일을 생성하고 필요한 설정 값을 추가합니다.
DB_URL=jdbc:mysql://localhost:3306/smart_agriculture
DB_USERNAME=root
DB_PASSWORD=yourpassword
JWT_SECRET=your_jwt_secret

## 3. 종속성 설치 및 빌드
./mvnw clean install

## 4. 서버 실행
./mvnw spring-boot:run

## API 문서
Swagger를 사용하여 API 문서를 제공합니다. 서버 실행 후 http://localhost:8080/swagger-ui/에서 확인할 수 있습니다.

## 기여 방법
이 프로젝트를 포크합니다.
새로운 브랜치를 생성합니다 (feature/새로운기능).
변경 사항을 커밋합니다 (git commit -m 'Add 새로운 기능').
브랜치에 푸시합니다 (git push origin feature/새로운기능).
Pull Request를 생성합니다.

## 라이선스
이 프로젝트는 MIT 라이선스를 따릅니다.
