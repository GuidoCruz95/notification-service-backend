# Notification Service, backend
A REST api written with Django to provide data management for notification service.

## Technologies used
* [DRF](www.django-rest-framework.org/): A powerful and flexible toolkit for building Web APIs


## Installation
* If you wish to run your own build, first ensure you have python globally installed in your computer. If not, you can get python [here](https://www.python.org").
* After doing this, confirm that you have installed virtualenv globally as well. If not, run this:
    ```bash
        $ pip install virtualenv
    ```
* Then, Git clone this repo to your PC using SSH or HTTP protocol.
    ```bash
        # Using SSH protocol(recommended)
        $ git clone git@github.com:GuidoCruz95/notification-service-backend.git
        # Using HTTP protocol
        $ git clone https://github.com/GuidoCruz95/notification-service-backend.git
    ```

* #### Dependencies
    1. Go into your cloned repo as such:
        ```bash
            $ cd notification-service-backend
        ```
    2. Create and fire up your virtual environment:
        ```bash
            $ virtualenv  venv -p python3
            $ source venv/bin/activate
        ```
    3. Install the dependencies needed to run the app:
        ```bash
            $ pip install -r requirements.txt
        ```
    4. Make those migrations work
        ```bash
            $ python manage.py makemigrations
            $ python manage.py migrate
        ```

* #### Run It
    Fire up the server using this one simple command:
    ```bash
        $ python manage.py runserver
    ```
    You can now access the file api service on your browser by using
    ```
        http://localhost:8000/notification-service
    ```
