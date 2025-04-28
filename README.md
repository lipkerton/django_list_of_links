## list_of_links
Я пытался сделать на веб-странице структуру меню, которое имеет подменю, а эти подменю, возможно имеют свои подменю.

# Как пользоваться? #
Установка виртуального окужения, активация, установка зависимостей (все делается внутри папки с проектом):

**MacOS/Linux**
```Bash
python -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
```
**Windows**
```PowerShell
python -m venv venv
.\venv\Scripts\activate
python -m pip install -r requirements.txt
```
Есть вероятность что Windows откажет в исполнении файла `.\venv\Scripts\activate` - так происходит, потому что в вашем Windows по-умолчанию стоит запрет на выполнение стрёмных скриптов. Я не настаиваю, но его можно снять, если ввести:
```PowerShell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
```
После снятия запрета просто повторите в папке проекта команду `.\venv\Scripts\Activate` и все дальнейшие действия.

Когда все действия выше сделаны можно запустить django-проект как обычно (из папки с файлом `manage.py`):
```Bash
python manage.py runserver
```
Я добавил одну сущность в БД для тестирования - чтобы ее увидеть нужно запустить сервер разработки и пройти в браузере по адресу `http://localhost:8000/menu`.
