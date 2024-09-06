Тестовое задание</br>

Комманды для установки:</br>
git clone github.com/Rastowerin/FastApiTest</br>
cd FastApiTest</br>
docker-compose up</br>


Задача 2</br>

UPDATE full_names</br>
INNER JOIN short_names</br>
ON SUBSTRING_INDEX(full_names.name, '.', 1) = short_names.name</br>
SET full_names.status = short_names.status</br>
