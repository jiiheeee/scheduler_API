## Sharing Schedule_API 
### 소개
호스트와 게스트 개념을 도입하여 호스트가 일정을 등록하면 게스트의 스케줄에 자동으로 일정이 업데이트되는 서비스

<br/>
<br/>
<br/>

## System Architecture
<img width="916" alt="스크린샷 2024-01-09 오후 6 21 02" src="https://github.com/jiiheeee/jiiheeee/assets/128598772/087ca487-f6ff-4d60-aa72-0241b0a404bf">

<br/>
<br/>
<br/>

## 개발 환경
• 프로젝트는 다음 환경에서 개발 및 배포되었습니다

• 로컬환경:M1맥북

• 배포 환경: AWS ECS

<br/>
<br/>
<br/>

## 기술 스택
• Programming: Python3.10

• Framework: Django 5.0.1

• Dockerhub

<br/>
<br/>
<br/>

## API 명세
POST /signup 

POST /signin

POST /schedule 

GET /schedule 

DELETE /schedule 

PATCH /schedule

POST /schedule/user 

DELETE /schedule/user
