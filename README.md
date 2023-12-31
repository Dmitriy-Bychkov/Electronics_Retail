# Online platform for an electronic trading network.
--------------------------------------------------------------------

## Implementation requirements
The network represents a hierarchical structure consisting of 3 levels:

- Factory
- Retail network
- Individual entrepreneur
Each level of the network is linked to only one equipment supplier d
(not necessarily the previous level in the hierarchy).
It is important to note that the level of hierarchy is determined by the relationship d
with other network elements, rather than the name of the entity.
For example, the factory is always at level 0, it has no suppliers, 
produces goods itself, and acts as a supplier to other entities. 
If the retail network is directly linked to the factory, bypassing other levels, 
its level is 1. Additionally, a supplier can be a company at the same level as the buyer.

Each element of the network possesses the following attributes:

- Name
- Contacts:
  - Email
  - Country
  - City
  - Street
  - House number
- Products:
  - Name
  - Model
  - Market release date
  - Supplier (previous network object in the hierarchy)
  - Debt to the supplier in monetary value (down to the cents)
  - Creation date (automatically filled upon creation)

## The main technology stack
- Python 
- Django
- Djangorestframework
- Rest_framework_simplejwt
- Drf_yasg
- PostgreSQL
- Git


## 1. Set Up your personal settings
- Create and fill out the .env configuration file in the root of the project with your personal data,
according to the sample, specified in .env.sample.

## 2. Install and acivate the virtual environment
- Install a new virtual environment if it doesn't exist:
    * pip install poetry
- Create a new Poetry virtual environment using the command:
    * poetry init
- Activate the virtual environment by running the command:
    * poetry shell
- Install all dependencies from the pyproject.toml file by running the command:
    * poetry install
  
## Project settings on your server
- Create a database in postgresql by running the commands:
  (the name of the database must match the name specified in the .env file)
    * psql -h localhost -U postgres
    * create database <your_database_name>;
    * \q
- Make migrations by running the commands:
    * python manage.py makemigrations
    * python manage.py migrate
- Create the superuser by running this command in the terminal:
    * python3 manage.py csu
- Create the simple user by running this command in the terminal:
    * python3 manage.py cu
- Write the main test data to your DataBase from the data.json file 
by running this command in the terminal:
    * python3 manage.py loaddata data.json

## API Documentation
The project documentation has been prepared based on drf-yasg. 
Access the documentation on the local server at the following addresses:
* http://127.0.0.1:8000/docs/ 
and
* http://127.0.0.1:8000/redoc/.

--------------------------------------------------------------------

# Run the project
- Run your server by using this command:
    * python manage.py runserver
- You can now log in to the Django administration system to manage your entities by clicking on this link:
    * http://127.0.0.1:8000/admin/

## The main working links
- The companies page
    * http://127.0.0.1:8000/companies/
- The products page
    * http://127.0.0.1:8000/companies/list_products/
- The orders page
    * http://127.0.0.1:8000/orders/
- The users page
    * http://127.0.0.1:8000/users/
  
--------------------------------------------------------------------

### This project was developed by Dmitriy Bychkov using the PyCharm development environment
