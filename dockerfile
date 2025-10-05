# Use Python 3.11 slim image
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Copy project files
COPY . /app

# Upgrade pip and install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Collect static files (optional)
RUN python manage.py collectstatic --noinput

# Expose port
EXPOSE 8000

# Start the Django app using Gunicorn
CMD ["gunicorn", "ProjectCMS.wsgi:application", "--bind", "0.0.0.0:8000"]
