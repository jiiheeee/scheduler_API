# Use the official Python image as the base image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY . /app/

# Install dependencies
RUN pip install asgiref && pip install Django
RUN pip install djangorestframework && pip install python-multipart
RUN pip install pytz && pip install sqlparse

# Copy the current directory contents into the container
COPY . /app/

# Expose the port that Django will run on
EXPOSE 8000

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
