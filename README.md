# Oğulcan Gök Fazla Gıda Case

### How to run
 simply run setup.sh on your Docker installed machine
 

### Admin Panel

#### All CRUD operations can be done on /admin

### Endpoints

#### /api/v1/{user,store,products}

##### POST
User
```json
{
	"email":"test2@test.com",
	"fullname":"John Doe2",
	"phone":"123456789",
	"role":"owner"
}
```
Product
```json

{
	"name":"product1"
	
}
```
Store
```json
{
	"name":"shop1"
	
}
```
Creates a new item

##### GET
params: ?id=
Returns the respective item

##### PUT
body:JSON
```json
{
	"id":"",
	"phone":"123456789"
	
}
```
Updates the given id with the given parameters

##### DELETE
params: ?id=
Deletes the respective item

### Add to Favourites

#### /api/v1/shop/add-favourites

##### POST
body:JSON

Adds a shop to users favourites list
```json

{
	"user_id":1,
	"shop_id":1
	
}
```
Adds a product to users favourites list
```json

{
	"user_id":1,
	"product_id":1
	
}
```