# Django - CRM

A Django based CRM Application where user can manage client information.

## Features

- **User Registration, Sign in, Sign Out**
- **Add Client**
- **View Client**
- **Update Client**
- **Delete Client**
- **Admin Features:**
  - Manage Users, Clients

## Installation

1. Clone the repository.
2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```
3. Configure database settings in `clienthub/settings.py`. Update the `DATABASES` setting to configure the MySQL database connection. You can use the following example configuration as a reference:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'your_database_name',
            'USER': 'your_database_user',
            'PASSWORD': 'your_database_password',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }
    ```
6. Run the Django migrations:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

7. Create a superuser to access the admin panel:

    ```bash
    python manage.py createsuperuser
    ```

8. Run the Django development server:

    ```bash
    python manage.py runserver
    ```
## Usage
- Access the application through a web browser.
- Use the provided user authentication system to create a new account.
- Manage client information by adding, viewing, updating, and deleting client records.

## Technologies Used

- Python
- Django
- HTML
- Bootstrap
- CSS
- JavaScript
- MySQL

![Screenshot 2024-03-25 at 15 28 47](https://github.com/arifurtuc/CRM-Django/assets/47160627/e0f481b3-e290-41dd-b430-eb642ef366b7)
