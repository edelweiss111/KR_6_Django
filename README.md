# Mailing_service_Django

Это веб-приложение сервиса управления рассылками, администрирования и получения статистики

#### Структура проекта:
config/
1. settings.py - настройки приложений
2. urls.py - файл маршрутизации

blog/
1. templates/blog - html шаблоны для приложения blog
2. admin.py - настройки админки
3. forms.py - настройки форм
4. models.py - модели приложения
5. urls.py - файл маршрутизации приложения
6. views.py - контроллеры

mailing/
1. management/commands
   1. start_mailing - кастомная команда начала рассылки
2. static - директория с файлами для стилистического оформления сайта
3. templates/mailing - html шаблоны для приложения mamiling
4. templatetags/
   1. my_tags - кастомные тэги
5. admin.py - настройки админки
6. cron.py - задачи для Cron
7. forms.py - настройки форм
8. models.py - модели приложения
9. services.py - сервисные функции
10. urls.py - файл маршрутизации приложения
11. views.py - контроллеры

users/
1. management/commands
   1. csu - кастомная команда создания суперпользователя
2. template/users - html шаблоны для приложения users
3. admin.py - настройки админки
4. forms.py - настройки форм
5. models.py - модели приложения
6. urls.py - файл маршрутизации приложения
7. views.py - контроллеры

manage.py - точка входа веб-приложения

pyproject.toml - список зависимостей для проекта.

#### Используется виртуальное окружение poetry

#### Для запуска web-приложения используйте команду "python manage.py runserver" либо через конфигурационные настройки PyCharm.
