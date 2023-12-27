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