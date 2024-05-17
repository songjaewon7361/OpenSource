# Dockerfile

# 베이스 이미지로 python 3.10 사용
FROM python:3.10-slim

# 작업 디렉토리 설정
WORKDIR /app

# 의존성 파일 복사 및 설치
COPY requirements-docker.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 소스 코드 복사
COPY . /app/

# 장고 애플리케이션의 포트를 외부에 노출
EXPOSE 8000

# 장고 개발 서버 실행
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
