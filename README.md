# Mediphore SkillMatch

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Django-based resource scheduling and management system that helps in assigning the right resources to tasks based on their skills and availability.

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Data Models](#data-models)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [License](#license)


## Features

- **Project Management**: Create and manage projects with multiple tasks
- **Resource Management**: Track team members and their skills
- **Task Tracking**: Monitor task status and assignments
- **Admin Interface**: Built-in Django admin for easy management

## Tech Stack

- **Backend**: Django 4.2+
- **Database**: SQLite (included)
- **Frontend**: Django Templates, Bootstrap
- **Dependencies**: See requirements.txt

## Data Models

### Project
- `name`: Project name (String)
- `description`: Project details (Text, optional)
- `start_date`, `end_date`: Project timeline (Date)
- `status`: Project status (String: 'not_started', 'in_progress', 'completed')
- `created_at`, `updated_at`: Timestamps (auto)

### Task
- `name`: Task name (String)
- `description`: Task details (Text, optional)
- `start_time`, `end_time`: Task schedule (DateTime)
- `status`: Task status (String: 'pending', 'in_progress', 'completed', 'blocked')
- `project`: Associated project (ForeignKey)
- `assigned_resource`: Assigned team member (ForeignKey, optional)
- `required_skills`: Skills needed (ManyToMany to Skill)
- `created_at`, `updated_at`: Timestamps (auto)

### Resource
- `name`: Full name (String)
- `email`: Contact email (String, unique)
- `skills`: Skills possessed (ManyToMany to Skill)
- `status`: Availability (String: 'available', 'unavailable', 'on_leave')
- `created_at`, `updated_at`: Timestamps (auto)

### Skill
- `name`: Skill name (String, unique)
- `description`: Skill details (Text, optional)

### ResourceAvailability
- `resource`: Associated resource (ForeignKey)
- `start_time`, `end_time`: Availability window (DateTime)
- `status`: Current status (String: 'available', 'unavailable', 'in_meeting')
- `notes`: Additional notes (Text, optional)

## Prerequisites

- pip (Python package manager)
- Git (for version control)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/shanusaras/Mediphore_SkillMatch.git
   cd Mediphore_SkillMatch
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # On Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser (admin):
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```
7. Access the application:
   - Admin interface: `http://127.0.0.1:8000/admin/`
   - Main application: `http://127.0.0.1:8000/`

## Project Structure
```
.
├── mediphore_task/         # Project configuration
│   ├── __init__.py
│   ├── asgi.py           # ASGI configuration
│   ├── settings.py        # Django settings
│   ├── urls.py           # Main URL routing
│   └── wsgi.py           # WSGI configuration
│
├── scheduler/             # Main application
│   ├── migrations/       # Database migrations
│   ├── templates/        # HTML templates
│   │   ├── base.html        # Base template
│   │   ├── projects.html    # Projects listing
│   │   ├── tasks.html       # Tasks listing
│   │   └── taskDetails.html # Task details
│   ├── __init__.py
│   ├── admin.py          # Admin interface
│   ├── apps.py           # App configuration
│   ├── models.py         # Database models
│   ├── urls.py           # App URL routing
│   └── views.py          # Request handlers
│
├── manage.py            # Django command-line utility
└── requirements.txt     # Python dependencies
```


## Usage

1. **Access the Admin Panel**
   - Navigate to `/admin`
   - Log in with your superuser credentials
   - Add Skills, Resources, and Projects through the admin interface

2. **User Interface**
   - View projects at `/projects`
   - View tasks at `/tasks`
   - Assign resources to tasks from the task detail page


## Screenshots

![Projects List](screenshots/projects.png)
*Figure 1: View and manage all projects*

![Task Management](screenshots/tasks.png)
*Figure 2: Assign and track tasks*

## License

MIT

