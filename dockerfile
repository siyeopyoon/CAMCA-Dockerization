FROM python:3.12-slim

WORKDIR /app

RUN python -m venv venv
RUN . venv/bin/activate


# install package
RUN apt-get update && \
    apt-get install -y python3 python3-pip

#RUN pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cu118

#RUN pip3 install numpy matplotlib scikit-learn scikit-image click requests psutil tqdm imageio imageio-ffmpeg pyspng pillow nibabel


RUN mkdir /external

COPY . /app

CMD ["python3", "main.py"]
