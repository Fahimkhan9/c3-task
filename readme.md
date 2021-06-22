# Pizza Api

## Running Locally

1.Activate the virtual env using pipenv or any virtual env you want
```bash
pipenv shell 
```
2.Install the dependencies. It might be different if you use  any other virtaul env.
```bash
pipenv install 
```

3.Run the django server
```bash
python manage.py runserver
```


## Api endpoints

### Pizza related

Endpoints for getting,creating,editing,deleting the pizza.

* Getting all pizza : `GET /api/all/`
* Getting filtered pizza by type and size: `GET /api/all/filters?type=typename&size=sizename` <br/>
type can be either 'regular' or 'square'
* Creating pizza : `POST /api/create/:Type/` <br/>
Type can be either 'regular' or 'square' <br/>
Request body example
```json
{
"name":"name",
"size":"small",
"toppings":"Onion, Tomato, Corn, Capsicum, CheeseJalapeno,test"
}
```
* Editing pizza : `PUT /api/update/:id/` <br/>
Here id is the pizza id <br/>
Request body example
```json
{
"name":"",
"size":"high",
"Type":"regular or square",
"toppings":"Onion, Tomato, Corn, Capsicum, Cheese, Jalapeno,test"
}
```
* Deleting pizza : `DELETE /api/delete/:id/` <br/>
Here id is the pizza id <br/>
