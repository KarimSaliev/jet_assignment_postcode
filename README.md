# jet_assignment_postcode
Simple django project that allows for a data retrieval from Just Eat Takeaway API

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Tests](#tests)
- [Improvements](#improvements)

## Installation
Have Python installed on your device as a prerequisite 

First create a directory of your choice to pull the project into
```
mkdir ProjectDir
```
Access the directory and clone the project from GitHub

```
cd ProjectDir
git clone https://github.com/KarimSaliev/jet_assignment_postcode.git
```
Now set up and activate the virtual environment

```
For Mac/Unix:

python -m venv venv
source venv/bin/activate

For Windows:

python -m venv venv
venv/Scripts/activate
```
Install the requirements for the project

```
cd jet_assignment_postcode
pip install -r requirements.txt
```

Then, make migrations and migrate the tables that would contain the postcode-area data that we would soon populate

```
python manage.py makemigrations
python manage.py migrate
```

Now, using fixtures file in the project that contains the initial postcode-area data, we will use it to populate the migrated tables

```
python manage.py loaddata postcode_data.json
```

Now that everything is set up, we can run the server locally and host project
```
python manage.py runserver

Then just click on a local server address that pops up to be redirected
```

## Usage
The project itself is a one-page application that allows to look up data on 10 different restaurants from a certain area specified by a postcode.

In the middle of the page, there is a droplist that contains the postcode-area entries, click on any of them and have the restaurant data be displayed to you.


## Tests

To run the tests that test the urls, views, models use the following command

```
python manage.py test jassignment/tests
```

## Improvements

To make the most out of my project in the business context, I would add links to those restaurants
that would redirect the end users to the restaurant's websites if they have one, or GoogleMaps contact details if they don't.

I would also include some additional data for those restaurants, such as their availability, working-hours for the user
to be able to narrow down and choose an option of their preference.

Some changes on the front-end part would also be implemented that would make the visual experience for the end-user to
be more smooth and appealing. This would include using different rating units to convert them to stars. Importing some fonts,
icons to accompany the data points. For example, a burger cuisine would have a burger next to it, pizza - a pizza icon, etc.