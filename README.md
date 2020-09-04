# Django Rest Framework assignment
**Problem Statement:** https://docs.google.com/document/d/1F90KvSqxxPzIRyeX7kD3wULrT0xNJMLdIgGVHq4KMxk/ 
<br><br>**Code Evaluation Criteria:** https://docs.google.com/document/d/1yA7S1w62iJFJpXQRsHHMfUEbs1ibaz8jn3P9S4n5rJQ/
<br><br> Other than local install, the api has also been hosted live at https://djangorestkj.herokuapp.com/api/. Admin panel available at https://djangorestkj.herokuapp.com/admin 
## NOTE: For a detailed documentation of the project with screenshots and details, refer the <a href ="https://github.com/kaushikjadhav01/django_rest_kaushik_jadhav/blob/master/Documentation.pdf">Documentation.pdf</a> file of this repository.

# Installation
Download this repository and change into directory of project. Then use pip to install all required pacakages. <pre>pip install -r requirements.txt</pre>

# Files and Directory Structure
<pre>
django_rest_kaushik_jadhav: Root folder of project

|---- cms_api : This folder contains our main api

|---- django_rest_kaushik_jadhav: This folder contains essential settings and configuration files of project.
</pre>

# Launching the API
cd into the root folder of the project and run the following command:
<pre>python manage.py runserver</pre>

# Routes
### 127.0.0.1:8000/api/register/ or https://djangorestkj.herokuapp.com/api/register/
POST request: Register a new user to get back user details and token

### 127.0.0.1:8000/api/login/ or https://djangorestkj.herokuapp.com/api/login/
POST request: Login an existing user to get token

### 127.0.0.1:8000/api/content/ or https://djangorestkj.herokuapp.com/api/content/
Protected Route, need to provide token in Authorization HTTP header before using
GET request: View All contents created by user<br>
POST request: Add a new content

### 127.0.0.1:8000/api/content/:content_id/ or https://djangorestkj.herokuapp.com/api/content/content_id/
Protected Route, need to provide token in Authorization HTTP header before using
DELETE request: Delete particular content by id<br>
UPDATE request: Update particular content by id

# Searching and Filtering
Search fields by specifying fields in route followed by suffix **'__icontains'** followed by your desired query.
<br>Example: 127.0.0.1:8000/api/content/?title__icontains=MyPostj&body__icontains=Post&summary__icontains=Summary&categories__icontains=Sports

# Creating Admin via seeding
To create an Admin user via seeding, run the following command:
<pre>python manage.py createsuperuser</pre>

