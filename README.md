Тестовое задание

Комманды для установки:
git clone github.com/Rastowerin/FastApiTest
cd FastApiTest
docker-compose up


Задача 2

UPDATE full_names
INNER JOIN short_names
ON SUBSTRING_INDEX(full_names.name, '.', 1) = short_names.name
SET full_names.status = short_names.status
