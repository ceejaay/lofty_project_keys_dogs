
## Chad Jemmett's Backend Practical project for Lofty


Thank you for considering me for a role at Lofty. Please review my project and we can set up a time where I can answer any questions you may have. Email me at chad.jemmett@gmail.com or call me at 208-350-0359

### Basic Setup

Clone the project from Github. In your terminal type:

`git clone git@github.com:ceejaay/lofty_project_keys_dogs.git`

This project requires Docker Compose you can download it [here](https://docs.docker.com/compose/install/)

Navigate to the root of the project.

``` $ cd lofty_project_keys_dogs ```


Then build the project in Docker by typing:

```$ docker-compose build```

After the build completes:

```$ docker-compose up```


Next, migrate the database inside the Docker container:

```$  docker exec -t < container id> ./manage.py makemigrations ```
```$  docker exec -t < container id> ./manage.py migrate ```

make a `.env` file in the `lofty_app` directory. In the `.env` file add this variable:

`IMGUR_SECRET=xxxxxxxxxxxxxxx`


Please get the secret ID from chad.jemmett@gmail.com

Finally, type `ctrl+c` to stop the docker containers. Start it up again by typing 

`$ docker-compse up`

These are the two applications contained in the project.


### Doggos App

This is an application that will provide your site or project with images of dogs. Getting data from this endpoint will
give you two similar images. They only differ by color.

With the Docker container running, navigate to `http://localhost:8000/dogs/` You can use the browser or Postman to make
GET requests to this endpoint.

If everything is working you will see this in your browser:

```
{
    "url": "https://i.imgur.com/i5WJ6DZ.jpg",
    "duplicate_url": "https://i.imgur.com/aNuf9Dt.jpg",
    "id": 104,
    "file_type": "image/jpeg",
    "height": 333,
    "width": 500,
    "filename": "Monica",
    "preview_link": "http://localhost:8000/dogs/preview/104"
}
```

The return data includes, three URLs 

1. One for the original image.
2. One for the altered image.
3. A preview link so you can see both images side-by-side.

The remaining data is metadata related to the photos.

These are the four endpoints avaiable for requests on this application.

* GET `localhost:8000/dogs` This returns links to the images and the metadata.
* GET 'http://localhost:8000/dogs/preview/<id of dog resource>' This Is the preview of the two images. It contains both
    images with their relevant metadata.


### Testing Doggos App

To run tests on this app type the following:


``` docker exec -t < container id> ./manage.py test doggos ```

You can get the container ID by typing `$ docker ps` in your teriminal **While** the docker container is running.



### Keys application

this application has four endpoints.

1. GET `http://localhost:8000/keys/` This endpoint returns a list of all the keys.

2. POST `http://localhost:8000/keys/` On this endpoint. The requests requires a body with at least a string which is the
`key` for the entry to the database.
    
    
    Valid data looks like this.
 Valid: 
 
    `{'key': "string_for_the_name_of_the_key", "value": 99}` 
    
    The `value` in the body is an integer. Either
        positive or negative.

   Valid: 
   
   `{'key': "string_for_the_name_of_the_key"}` 
   
   A key is required. If there is no `value` the default value
        will be `0`

     Invalid: 
        
    `{}` or `{'value': 99}` 
        
        
    Any request missing a Key will be rejected and return an error.

3.  GET `http://localhost:8000/keys/key_detail/<id of key>`

     This will return the key with it's related value and the ID of the key.

    POST  
    `http://localhost:8000/keys/key_detail/<id of key>`    
        
    This endpoint will increment the key. The body of the request must contain an integer to Increment/Deincrement the `value` of the key. You can send either a positive integers to increment the value or you can send a negative integer to deincrement the value.
   
        
### Testing Keys App

To test the Keys app type this in your terminal


``` $ docker exec -t < container id> ./manage.py test keys ```