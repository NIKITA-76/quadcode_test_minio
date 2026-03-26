
## Поднимаем машины через Vagrantfile
vagrant up

## Запускаем таски в плейбуке на все хосты
ansible-playbook -i inventory.ini playbook.yml --ask-vault-pass

## Устанавливаем mc для Minio на все хосты
ansible all -i inventory.ini -m get_url -a "url=https://dl.min.io/client/mc/release/linux-amd64/mc dest=/usr/local/bin/mc mode=0755" --become

## Создать алиас myminio
ansible vm1 -i inventory.ini -m shell -a "mc alias set myminio http://127.0.0.1:9000 minioadmin minioadmin123" --become
##### Эту команду я бы засунул в плейбук чтобы использовать пароли из vault, но по условию тествого было сказано именно через ad-hoc 

## Создать юзера
ansible vm1 -i inventory.ini -m shell -a "mc admin user add myminio readwrite readwrite123" --become
##### Эту команду так же бы засунул в плейбук чтобы использовать пароли из vault, но по условию тествого было сказано именно через ad-hoc 

## Выдать права на чтение/запись
ansible vm1 -i inventory.ini -m shell -a "mc admin policy attach myminio readwrite --user readwrite" --become

## Создаем бакет
ansible vm1 -i inventory.ini -m shell -a "mc mb myminio/mybucket" --become

## Передаем на вм файл с локальной машины
ansible vm1 -i inventory.ini -m copy  -a "src=/tmp/test.jpg dest=/tmp/test.jpg" --become

## Копируем файл в сам бакет
ansible vm1 -i inventory.ini -m shell -a "mc cp /tmp/test.jpg myminio/mybucket/test.jpg" --become



## Скачать файл со смещением 1000 байт
python3 download.py


## Так как не было указано какой тип балансировщика использовать на Nginx, использовал дефолтный - Round Robin

