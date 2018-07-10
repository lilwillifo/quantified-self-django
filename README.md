# Quantified Self Back-end Django
You'll need Python3 and Django 2.0.7 installed.
## Initial Setup

1. Clone this repository and rename the repository to `quantified-self-django` in one command

  ```shell
  git clone git@github.com:lilwillifo/quantified-self-django.git
  ```
2. Change into the `quantified-self-django` directory

3. Create a virtualenv

  ```shell
  virtualenv -p python3 .venv
  source .venv/bin/activate
  ```
4. Updgrade pip and install dependencies
  ```shell
  pip3 install --upgrade pip
  pip3 install -r requirements/local.txt
  ```

3. Set up the database in psql

  ```shell
  CREATE DATABASE quantified_self;
  CREATE DATABASE quantified_self_test;
  ```

4. Migrate and Seed
  ```shell
  python3 manage.py makemigrations
  ```

5. Run test suite

  ```shell
    python3 manage.py test
  ```

## Running the Server Locally

To see your code in action locally, you need to fire up a development server. Use the command:

```shell
python3 manage.py runserver
```

Once the server is running, visit API endpoints in your browser:

* `http://localhost:8000/` to run your application.  [Spec](https://github.com/turingschool/backend-curriculum-site/blob/gh-pages/module4/projects/quantified-self/quantified-self.md)

### Endpoints

* To see the [front end](https://github.com/lilwillifo/quantified-self-fe) deployed with this app, visit https://lilwillifo.github.io/quantified-self-fe/

Back End Production Base URL:  https://rocky-basin-21915.herokuapp.com/
Local Base URL:       http://localhost:8000

#### Food Endpoints

**GET /api/v1/foods**
Return all foods in the database

Request URL
```
/api/v1/foods
```

Response Body
```
[
  {
    id: 1,
    name: "Banana",
    calories: 100
  },
  {
    id: 2,
    name: "Apple",
    calories: 200
  },
  {...}
]
```
Response Code
```
200
```


**GET /api/v1/foods/:id**
Return food corresponding to :id

Request URL
```
/api/v1/foods/:id
```

Response Body
```
{
  id: 1,
  name: "Banana",
  calories: 100
}
```

Response Code
```
200
```


**POST /api/v1/foods**
Create a new food item in the database

Request URL
```
/api/v1/foods
```

Parameters Format
_All parameters required_
```
{ food { "name": "Fried Chicken", "calories": 1000 } }
```

Response Body
```
{
  id: 1,
  name: "Fried Chicken",
  calories: 1000
}
```

Response Code
```
201
```


**PATCH /api/v1/foods/:id**
Edit food corresponding to :id

Request URL
```
/api/v1/foods/:id
```

Parameters Format
_All parameters required_
```
{ food { "name": "Banana", "calories": 150 } }
```

Response Body
```
{
  id: 1,
  name: "Banana",
  calories: 150
}
```

Response Code
```
200
```


**DELETE /api/v1/foods/:id**
Delete food corresponding to :id

Request URL
```
/api/v1/foods/:id
```

Response Code
```
204
```



##### Meal Endpoints

**GET /api/v1/meals**
Return all meals along with their associated foods

Request URL
```
/api/v1/meals
```

Response Body
```
[
    {
        "id": 1,
        "name": "Breakfast",
        "foods": [
            {
                "id": 1,
                "name": "Apple",
                "calories": 200
            }
        ]
    },
    {
        "id": 2,
        "name": "Lunch",
        "foods": [
            {
                "id": 5,
                "name": "Sandwich",
                "calories": 800
            },
            {
                "id": 9,
                "name": "Fries",
                "calories": 400
            }
        ]
    },
    {...}
  ]
```

Response Code
```
200
```


**GET /api/v1/meals/:meal_id/foods**
Return all foods associated with meal corresponding to :meal_id

Request URL
```
/api/v1/meals/:meal_id/foods
```

Response Body
```
[
  {
      "id": 1,
      "name": "Apple",
      "calories": 150
  }
]
```

Response Code
```
200
```


**POST /api/v1/meals/:meal_id/foods/:food_id**
Add food corresponding to :food_id to meal corresponding to :meal_id

Request URL
```
/api/v1/meals/:meal_id/foods/:food_id
```

Response Body
```
{
    "message": "Successfully added FOODNAME to MEALNAME"
}
```

Response Code
```
201
```

**DELETE /api/v1/meals/:meal_id/foods/:food_id**
Remove food corresponding to :food_id from meal corresponding to :meal_id

Request URL
```
/api/v1/meals/:meal_id/foods/:food_id
```

Response Body
```
{
    "message": "Successfully removed FOODNAME from MEALNAME"
}
```

Response Code
```
200
```
