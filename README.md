# Softdesk API

***
This project is part of the python developer course on [Openclassrooms](http:/openclassrooms.com).

The goal is to create an API for an issue tracking app.

***

* **[Setup](#Setup)**
  * [Virtual environment creation](#Create-a-virtual-environment)
  * [Database schema creation](#Create-the-database-schema)
* **[API endpoints documentation](#Postman-Endpoints-documentation)**


## **Setup**

***

</br>
A Python installation is required.

> The code was written using python 3.10.2. User discretion is advised when using an earlier version.

Assuming a git installation, clone the repository using:

    $git clone git clone https://github.com/Chfrlt/P10

</br>

### **Create a virtual environment**

</br>
> Following instructions are the ones recommanded for python 3.6 or greater. If your python installation is an earlier version, please consult the associated documentation.

Create a virtual environnement using:

    $python -m venv <env_name>

To activate it:

* On Windows:

        $env_name/Script/activate

* On Linux/Mac:

        $source env_name/bin/activate

Install the python dependencies using:

    $pip install -r requirements.txt

</br>

### **Create the database schema**

</br>
Go to the app folder using:

    cd .\softdeck_api\

Create the database structure using:

    $python manage.py makemigrations
    $python manage.py migrate

## **Postman Endpoints documentation**

***

You can find a list of the endpoints & the associated documentation at this adress:

    https://documenter.getpostman.com/view/23276936/2s7ZLXRGjM
