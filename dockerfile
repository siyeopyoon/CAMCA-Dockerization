FROM python:3.11-slim-buster

# 작업 디렉토리 설정
WORKDIR /app

# 가상 환경을 만들고 활성화합니다.
RUN python -m venv venv
RUN . venv/bin/activate


# install package
RUN apt-get update && \
    apt-get install -y python3 python3-pip

# 파이썬 패키지 설치
RUN pip3 install numpy matplotlib


# 외부 폴더와 공유할 폴더 생성 
# 컨테이너 내부에서의 이름임.
RUN mkdir /external_folder

# 파이썬 스크립트 복사
COPY . /app

# 파이썬 스크립트 실행
CMD ["python3", "main.py"]