# Mediphore SkillMatch

A Django-based resource scheduling and management system that helps in assigning the right resources to tasks based on their skills and availability.

## Features

- **Project Management**: Create and manage projects with multiple tasks
- **Resource Management**: Track team members and their skills
- **Smart Assignment**: Automatically suggests available resources based on skills and availability
- **Task Tracking**: Monitor task status and assignments

## Prerequisites

- Python 3.8+
- pip (Python package manager)
- SQLite (included with Python)

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Mediphore_SkillMatch
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional, for admin access)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Main app: http://127.0.0.1:8000/
   - Admin: http://127.0.0.1:8000/admin/

## Project Structure

```
Mediphore_SkillMatch/
├── manage.py           # Django's command-line utility
├── requirements.txt    # Project dependencies
├── mediphore_task/     # Project configuration
│   ├── __init__.py
│   ├── settings.py     # Django settings
│   ├── urls.py        # Main URL routing
│   └── wsgi.py        # WSGI configuration
└── scheduler/         # Main application
    ├── migrations/    # Database migrations
    ├── services/      # Business logic
    ├── templates/     # HTML templates
    ├── __init__.py
    ├── admin.py      # Admin interface
    ├── apps.py       # App configuration
    ├── models.py     # Database models
    ├── urls.py       # App URL routing
    └── views.py      # Request handlers
```

## Usage

1. **Access the Admin Panel**
   - Navigate to `/admin`
   - Log in with your superuser credentials
   - Add Skills, Resources, and Projects through the admin interface

2. **Using the Application**
   - View projects at `/projects`
   - View tasks at `/tasks`
   - Assign resources to tasks from the task detail page

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with Django
- Uses Bootstrap for frontend styling
