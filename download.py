from minio import Minio

# Подключиться к Minio
client = Minio(
    "192.168.56.11:9000",  # адрес кластера
    access_key="readwrite",  # пользователь
    secret_key="readwrite123",  # его пароль (так же не зашифрован, так же как и в ad-hoc командах)
    secure=False  # без SSL
)

# Скачать файл со смещением 1000 байт
response = client.get_object(
    "mybucket",   # название бакета
    "test.jpg",   # название файла
    offset=1000   # начать с байта 1000
)

# Сохранить результат в файл
with open("result.jpg", "wb") as f:
    for chunk in response:
        f.write(chunk)

response.close()
response.release_conn()

print("Файл скачан: result.jpg")

