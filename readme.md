# LEAP website

This is the django website of LEAP, the roundnet association of Enschede.

## Setup

1. Clone the project to your local environment.
2. Make sure you have python, pip, virtualenv, node and yarn installed.
3. Create a new virtualenv by running `python -m virtualenv`
4. Start your virtualenv
5. Run `pip install -r requirements.txt`
6. Run `yarn`
7. Copy website/.env.example to website/.env (if needed, change any settings in this file, the default example settings should work for local development).
8. Run `python ./manage.py migrate`
9. To start the development server, run `yarn run dev`
