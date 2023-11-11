# car_access
## Описание
Бэкенд для приложения пропуска автомобилей на охраняемую территорию. Для администраторов реализована админ панель с таблицами, в которых они могут добавлять пользователей-охранников и информацию о машинах, которым разрешен въезд.
Также реализован GraphQL API, поддерживающий CRUD операции с автомобилями, для отрисовки информации о всех имеющихся автомобилях на фронтенде. 

Админ панель 127.0.0.1:8000/admin/

API 127.0.0.1:8000/api/v1/graphql/

## Запуск проекта
1. Клонировать репозиторий:
   ```
   git clone git@github.com:DOSuzer/car_access.git
   ```
2. Перейти в папку с docker-compose.yml:
   ```
   cd car_access/infra
   ```
3. Создать файл .env с содержимым:
   ```
   DB_ENGINE=django.db.backends.postgresql
   DB_NAME=postgres
   POSTGRES_USER=postgres
   POSTGRES_PASSWORD=<пароль>
   DB_HOST=db
   DB_PORT=5432
   SECRET_KEY==<секретный ключ Django>
   DEBUG=True
   ```
   
4. Запустить сборку:
   ```
   docker-compose up -d
   ```
5. Выполнить миграции и создать суперпользователя:
   ```
   docker exec -it backend python manage.py migrate
   docker exec -it backend python manage.py createsuperuser
   ```


## Работа с API:
+ /api/v1/graphql/
  * Через Postman с автоматическим получением schema;
  * Через браузер с помощью graphiql.
