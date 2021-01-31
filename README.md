# simple-restful-api-pokedex
A restful api written in python Django, implements basic CRUD api interface.

## Setup
1. `git clone https://github.com/JohnCSW/simple-restful-api-pokedex.git `
2.  Make sure you're using python3, would be better using virtual environment.
3. ```bash
   pip install django
   pip install djangorestframework
   ```
4. `python manage.py runserver`
5. A default data set has been created for you,
   go to [localhost:8000/admin](localhost:8000/admin),
   log in with 
   ```
      username: john
      password: 1234
   ```
   to see more details about schema or to create your own data set. 
## Usage
   ### Get a pokemon by number
   - path:`GET /api/pokemon/001`
   - response
   ```json
{
    "number": "001",
    "name": "Bulbasaur",
    "types": [
        "Grass",
        "Poison"
    ],
    "evolutions": [
        {
            "number": "002",
            "name": "Ivysaur",
            "types": [
                "Grass",
                "Poison"
            ]
        }
    ]
}
```


### Get a pokemon list
- path:`GET /api/pokemon`
- with type: `GET /api/pokemon?types=Grass,Poison`
- response
```json
{
    "number": "001",
    "name": "Bulbasaur",
    "types": [
        "Grass",
        "Poison"
    ],
    "evolutions": [
        {
            "number": "002",
            "name": "Ivysaur",
            "types": [
                "Grass",
                "Poison"
            ]
        }
    ]
}
```

   ### Create a pokemon 
   - path: `POST /api/pokemon/`
   - request body:
   ```json
   {
      "number": "002",
      "name": "Ivysaur",
      "types": [
         "Grass",
         "Poison"
      ]
   } 
   ```
-  response:
```json
   {
      "number": "002",
      "name": "Ivysaur",
      "types": [
         "Grass",
         "Poison"
      ]
   } 
```

### Update a pokemon by number
- path: `/api/pokemon/002/`
- request body:
   ```json
   {
      "number": "002",
      "name": "Ivysaur!!!",
      "types": [
         "Grass",
         "Poison"
      ]
   } 
   ```
-  response:
```json
   {
      "number": "002",
      "name": "Ivysaur!!!",
      "types": [
         "Grass",
         "Poison"
      ]
   } 
```

### Delete a pokemon by number
- note: if the pokemon is the evolution of
  some pokemon, errors will be raised.
- path: `DELETE /api/pokemon/002/`
-  response:
```json
   {
      "number": "002",
      "name": "Ivysaur",
      "types": [
         "Grass",
         "Poison"
      ]
   } 
```

### Add an evolution of a pokemon
- note: If the evolved pokemon does not exists,
        it will be automatically created. 
- path: `PUT /api/pokemon/002/evolution`
- request body:
```json
   {
      "number": "003",
      "name": "Venusaur",
      "types": [
         "Grass",
         "Poison"
      ]
   } 
```
-  response:
```json
{
    "number": "002",
    "name": "Ivysaur",
    "types": [
        "Grass",
        "Poison"
    ],
    "evolutions": [
        {
            "number": "003",
            "name": "Venusaur",
            "types": [
                "Grass",
                "Poison"
            ]
        }
    ]
}
```

### Delete an evolution of a pokemon
- note: If the evolved pokemon does not exists,
  it will raise errors.
- path: `DELETE /api/pokemon/002/evolution`
- request body:
```json
   {
      "number": "003",
      "name": "Venusaur",
      "types": [
         "Grass",
         "Poison"
      ]
   } 
```
-  response:
```json
{
    "number": "002",
    "name": "Ivysaur",
    "types": [
        "Grass",
        "Poison"
    ],
    "evolutions": []
}
```
