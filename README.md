# This django project is to display student details

<h1><b>HOW DOES THIS WORK</b></h1><br>

Make sure to have your environment setup before beginning.

The below image is when you have created a superuser

![WhatsApp Image 2024-06-30 at 18 49 53_9474f2ff](https://github.com/Mirzasheriff/my_django_student_data/assets/114513782/2ee44a7a-cc8f-4f03-8405-1d8551ec0a98)



For eg: My username: 'sheriff'   /   
        My password: 'sheriff'

![WhatsApp Image 2024-06-30 at 18 54 58_48cc204a](https://github.com/Mirzasheriff/my_django_student_data/assets/114513782/8ddc5974-7762-41d2-84cf-61de048dd088)



After running the code from project using cmd -->python/python3 manage.py runserver 8000 (port num optional), the default url would be at '127.0.0.1:8000' 
now edit the url as '127.0.0.1:8000/student/id/'
(Note: My application has ID entry from 1 to 5)
(i.e)

'127.0.0.1:8000/student/1/'

![WhatsApp Image 2024-06-30 at 18 55 12_f81552e1](https://github.com/Mirzasheriff/my_django_student_data/assets/114513782/631a0727-8eef-41bc-8cd0-a138d5a354e8)


'127.0.0.1:8000/student/2/'

'127.0.0.1:8000/student/3/'

'127.0.0.1:8000/student/4/'

'127.0.0.1:8000/student/5/'

You can now view the data you have loaded in

![WhatsApp Image 2024-06-30 at 18 56 29_64ff3332](https://github.com/Mirzasheriff/my_django_student_data/assets/114513782/e5c5ac3f-81bd-4a5e-ae3a-6e756d672a58)



<h1><b>HOW TO START THE PROJECT</b></h1>



Step 1:
     Creation of django project: Allot a directory to create a project and run cmd -> django-admin startproject 'projectname'

Step 2:
     Creation of django application: change directory(cd) into the project and start the application with cmd--> python/python3 manage.py startapp 'application_name'

     (NOTE: A project may contain more than one applications)

Step 3:
     Open setting.py and include the app_name in 'installed apps'

Step 4:
     Provide views.py with function setup

Step 5:
     Provide with the path to open the webpage and display the content by importing and calling in the views function

Step 6:
     Run your server with cmd--> python/python3 manage.py runserver 


<h1><b>TEMPLATES</b></h1>

Create a folder in main application directory(along with manage.py) and make a file for your project in which the html file is stored.This improves code reusability

and include lines 

BASE_DIR2 = os.path.dirname(os.path.dirname(os.path.abspath(_file_)))

TEMPLATE_DIR = os.path.join(BASE_DIR2, 'templates')

and add TEMPLATE_DIR in TEMPLATE_DIR = []

<h1><b>STATIC</b></h1>

Html files can be stored in templates while css,images and other files can be included here.

STATIC_DIR = os.path.join(BASE_DIR2, 'static')

Add your db to be translated code into Models.py

<h1><b>HOW DOES THIS WORK</b></h1>

<i>The basic flow of Django</i>

The url selected to search guides from user request to views.py -->models.py --> DB -->models.py -->views.py -->Templates file -->User

<h1><b>ADDITIONAL NEEDS</b></h1>

Knowledge of basic workings of <ul>
<li>html</li>
<li>css</li>
<li>JS</li>
<li>Bootstrap</li>
<li>jQuery</li>
<li>DOM</li>
<li>Jinja</li>
</ul>

Models.py

![WhatsApp Image 2024-06-30 at 03 06 46_cabe21a8](https://github.com/Mirzasheriff/my_django_student_data/assets/114513782/39ce580e-12b6-45e5-beab-60a0d52a746a)



Admin.py

![WhatsApp Image 2024-06-30 at 03 06 56_57503b90](https://github.com/Mirzasheriff/my_django_student_data/assets/114513782/905d11bb-743a-4b54-933c-141258a01a64)



Urls.py

![WhatsApp Image 2024-06-30 at 03 07 17_327c6a47](https://github.com/Mirzasheriff/my_django_student_data/assets/114513782/5095db34-8329-4acd-9df0-7b5acd42bcbc)


Views.py

![WhatsApp Image 2024-06-30 at 03 07 33_44c95ecc](https://github.com/Mirzasheriff/my_django_student_data/assets/114513782/2ae76b76-730e-47f0-802e-18fde29a9df7)


Welcome.html

![WhatsApp Image 2024-06-30 at 03 07 54_b5fe1b57](https://github.com/Mirzasheriff/my_django_student_data/assets/114513782/fc610226-31f1-441e-9c24-2fc0922f9978)

