# Coff'ErUp
Coff'ErUp is a Django web application that allows users to create and maintain digital collection coffers (swear jars, coffee messes, etc). Users can choose to join a coffer and the coffer collectively records contributions from users.  
  
There are several categories of coffers:
* Open Coffers - Coffers that have already started and are accepting contributions/penalties
  * Future Coffers - Coffers that have been created but the start date has not arrived
  * Closed Coffers - Coffers whose end date has passed
    * Settled - Closed Coffers that have been Paid
    * Unsettled - Closed Coffers that are Unpaid  
  
Users can join as many coffers as they like.  
So get started and join your friends in filling the coffers!  

## Steps to start Coff'ErUp:

* Clone down the repo and `cd` into it

* Create your OSX virtual environment in Terminal:

  * `python -m venv CapstoneEnv`
  * `source ./CapstoneEnv/bin/activate`

* Or create your Windows virtual environment in Command Line:

  * `python -m venv cofferupEnv`
  * `source ./cofferupEnv/Scripts/activate`

* Install the app's dependencies:

  * `pip install -r requirements.txt`

* Build your database from the existing models:

  * `python manage.py makemigrations cofferupApp`
  * `python manage.py migrate`
  
* Fire up your dev server and get to work!

  * `python manage.py runserver`


## ERD

![cofferUp ERD](./cofferUpApp/assets/cofferUpERD.png)

Not that the column names do not conform to the Python community standards (PEP) for naming conventions. Make sure your models use snake case.
