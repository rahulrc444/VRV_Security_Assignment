# VRV_Security_Assignment
 This project implements Role-Based Access Control (RBAC) using Django, allowing user access to be managed based on roles like admin, moderator, and user. It includes user registration, login, role-specific dashboards, and admin features to manage users (add, edit, delete). The system ensures secure, role-based access to resources.
Django Role-Based Access Control (RBAC) Project
This Django project implements a simple Role-Based Access Control (RBAC) system with user authentication, registration, and role management (Admin, Moderator, User).

Features
User Registration: New users can register with roles (Admin, Moderator, User).
Admin Dashboard: Allows the admin to manage users, including adding, editing, and deleting users.
Role-Based Views: Different dashboards for Admin, Moderator, and User with restricted access based on roles.
Setup

1. Clone the Repository
bash
Copy code
git clone <repository-url>
cd <project-directory>


2. Create a Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate


3. Install Dependencies
pip install -r requirements.txt


4. Apply Migrations
Run database migrations to set up your tables:
python manage.py migrate


5. Create a Superuser
Create a superuser to access the admin panel:
python manage.py createsuperuser


6. Run the Server
Start the Django development server:
python manage.py runserver

7. Access the Application
Admin Dashboard: http://127.0.0.1:8000/admin_dashboard/
User Dashboard: http://127.0.0.1:8000/user_dashboard/
Login Page: http://127.0.0.1:8000/accounts/login/


8. Access Admin Panel
Login with the superuser credentials and access the Django admin panel at:

http://127.0.0.1:8000/admin/

Common Commands
Run Server: python manage.py runserver
Apply Migrations: python manage.py migrate
Create Superuser: python manage.py createsuperuser
License
This project is licensed under the MIT License.

This README provides the basic setup and usage instructions for your Django RBAC project. Feel free to customize it based on your specific needs!
