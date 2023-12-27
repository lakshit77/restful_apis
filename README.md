# Django Movie Booking API

Welcome to the Django Movie Booking API project! 🎬 This project provides a RESTful API for managing movies, bookings

## Features

- CRUD operations for Movies and Bookings
- Swagger documentation
- Docker support for easy deployment

### Prerequisites

- Python 3.9 or higher
- Django
- Docker (optional)

### Installation

1. Clone the repository
```bash
git clone https://github.com/<your-username>/restful_apis.git .
```
2. Create Virtual Enviornment
3. Install dependency from requirements.txt
```bash
pip install -r requirements.txt
```

### Database Setup 
```bash
python manage.py migrate
```

### Running the Project 
```bash
python manage.py runserver
```

```bash
Visit http://127.0.0.1:8000/swagger to access the API with Documentation
```


### With Docker 

```bash
docker build -t movie-booking-app .
docker run -p 8000:8000 movie-booking-app
```

```bash
Visit http://localhost:8000/swagger to access the API with Documentation
```




## Future Scope

The Django Movie Booking API is an evolving project, and there are several exciting features and improvements planned for the future. Here are some ideas for the project's future scope:

### 1. User Roles and Permissions

Enhance user authentication by implementing roles and permissions. For example, differentiate between regular users, administrators, and staff members with varying levels of access.

### 2. User Profiles

Implement user profiles to allow users to customize their experience, view their booking history, and save favorite movies or genres.

### 3. Social Media Integration

Integrate social media authentication and sharing features to enhance user engagement and simplify the signup process.

### 4. Testing and CI/CD

Implement comprehensive unit and integration tests to ensure the reliability of the application. Set up continuous integration and deployment (CI/CD) pipelines for automated testing and deployment.

### 5. Advanced Search and Filters

Enhance the movie search functionality with advanced filters, sorting options, and additional metadata to help users find movies more easily.

