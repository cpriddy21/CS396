# CS396
Online Learning System Project
Overview
The Online Learning System project aims to create an educational platform to facilitate student learning. This project encompasses three components: the web server, the database, and the web interface. This README provides an overview of the project's objectives, features, and implementation details.

Project Phases
Phase 1: Building Website Using Django 
In the first phase of the project, we will focus on implementing essential functionalities of the Online Learning System. These functionalities include:

Administrator Account: The system will support an administrator role with Django's built in admin tool with privileges to delete other users, edit/delete all posts, and create new discussion topics.

User Account Types: The system will accommodate two types of user accounts: students and teachers. Student accounts allow access to study materials such as text documents, animations, videos, and exercises (e.g., multiple-choice questions). Teacher accounts enable monitoring of student performance through practice results. Students can view only their own results, while teachers have access to all students' results.

User Authentication: The project will provide user authentication features, including login and sign-up functionalities for new users.

Discussion Forum: Any registered user can create new discussion posts, reply to existing posts, and upload multiple files within the posts.

User-Friendly Interface: The web interface will be designed to be user-friendly and intuitive.

Getting Started
To set up and run the Online Learning System project, follow these steps:

Requirements: Ensure you have Python and Django installed on your system.

Database Setup: Configure the database settings in the project to match your environment.

Initialize Database: Run database migrations and create the necessary tables by executing the following commands:

Code:
python manage.py makemigrations
python manage.py migrate

Create an Administrator Account: Create an initial administrator account using the following command:

Code:
python manage.py createsuperuser

Run the Development Server: Start the development server with the following command:

COde:
python manage.py runserver

Access the Web Interface: Open a web browser and navigate to the provided URL 

Duplicating the GitHub Project
To duplicate the Online Learning System project from GitHub and replicate it on your local machine, follow these steps:

Clone the Repository: Open a terminal or command prompt and navigate to the directory where you want to store the project. Then, run the following command to clone the GitHub repository:

git clone https://github.com/cpriddy21/CS396/



Usage and Features
User Registration: New users can sign up for student or teacher accounts.
User Authentication: Registered users can log in to their accounts.
Administrator Privileges: Administrators have control over user management, posts, and discussion topics.
Study Materials: Students can access and study various learning materials, including text documents, animations, videos, and exercises.
Practice Exercises: Students can practice with exercises, and their results are tracked.
Discussion Forum: Users can create and participate in discussion posts, upload files, and interact with others.
User-Friendly Interface: The web interface is designed to be intuitive and user-friendly.

Contributors
Cassandra Priddy
