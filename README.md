
## Chad Jemmett's Backend Practical project for Lofty


Thank you for considering me for a role at Lofty. Please review my project and we can set up a time where I can answer any questions you may have.

### Basic Setup

Clone the project from Github. 


This project requires Docker Compose you can download it [here](https://docs.docker.com/compose/install/)

Navigate to the root of the project.

``` cd lofty_project_keys_dogs ```

Then build the project in Docker by typing:

```docker-compose build```

After the build completes:

```docker-compose up```


make a `.env` file in the lofty_app directory


Things to do 
[  ] Migrate the database by going to the  

``` docker exec -t < container id> ./manage.py makemigrations ```
``` docker exec -t < container id> ./manage.py migrate ```


### Doggos App



