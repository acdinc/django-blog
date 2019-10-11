### Django blog project
***
1.Install pip
```
sudo apt-get install python3-pip
```
2.Install virtualenv
```
sudo pip3 install virtualenv
```
3.Clone the project
```
https://github.com/acdinc/django-blog.git && cd django-blog
```
4.Create a virtual environment
```
virtualenv venv
```
5.Activate the virtual environment
```
source venv/bin/activate
```
6.Install dependencies 
```
pip install -r requirements.txt
```
7.Set database
```
python manage.py makemigrations
python manage.py migrate
```
8.Create superuser 
```
python manage.py createsuperuser
```
9.Copy your CAPTCHA keys to /blog/settings.py file
```
RECAPTCHA_PUBLIC_KEY = ''
RECAPTCHA_PRIVATE_KEY = ''
```
***
After all these steps , you can start testing and developing this project. 
