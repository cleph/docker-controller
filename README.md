# Flask Docker Container Manager

This is a simple Flask web application that allows you to view, restart, stop, and delete Docker containers running on your server. It uses the `docker-py` library to interact with Docker.

## Features

- **View all containers**: Lists all running and stopped containers.
- **Restart**: Restart any container with a single click.
- **Stop**: Stop a running container.
- **Delete**: Permanently delete a container.

## Prerequisites

- Python 3.x
- Docker installed and running on your server
- `docker-py` library for Python

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/cleph/flask-docker-manager.git
   cd flask-docker-manager
Install the required dependencies:

```
pip install -r requirements.txt
```
Run the application:

```
python app.py
```
Open a browser and go to http://127.0.0.1:5000/ to access the application.

Usage
The main page displays a list of all containers with their ID, name, and status. Each container has the following actions:

Restart: Click to restart the container.
Stop: Click to stop the container if it is running.
Delete: Click to delete the container.
Project Structure
bash
Copy code
flask-docker-manager/
├── app.py                # Main application file
├── requirements.txt      # List of dependencies
└── templates/
    └── containers.html   # HTML template for displaying containers
Dependencies
Flask: Web framework used for the application
docker-py: SDK for managing Docker containers in Python
To install dependencies:

```
pip install -r requirements.txt
```
Screenshots

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contributing
Contributions are welcome! Please submit a pull request or open an issue for suggestions or improvements.

This project was created to provide a simple way to manage Docker containers through a web interface built with Flask.


