FROM python:3.9

WORKDIR /app

COPY . /app
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
EXPOSE 5000
RUN chmod +x /app/wifi-weihu.py

CMD ["python", "app.py"]
