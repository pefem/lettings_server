# RESTAPI SEVER DEVELOPED FOR LETTINGS AGENTS USING FASTAPI


### Installation & Configuration
- Install the Docker Desktop and Start It
- Clone this git repository in your local machine ``.

```
You do not need to change anything here, but if you would like to change the username, password or database name, you can modify it at this point in the `.env` file attached to this project. It has been left attached for convinience. 

### Building the Project
- We can start building our projects by running `docker compose build`
- One build is done, run `docker compose up` to start the services. Leave this terminal open to check the logs.
- To stop the services you can press `Ctrl + C` - (Control + C)

# Accessing the Docker Containers
- FastAPI Application [http://localhost:8000]
- API Documentation [http://localhost:8000/docs]
- Database Access (pgAdmin) [http://localhost:5050/]
    - login credentials can be obtained from the .env file
    - Please note you do not need to run any migrations once you've registered the serve as the databse will have the required tables created on start of the web container


```

- To Run the Test
```
docker compose run web sh -c "pytest"
```

- Running a single test file
```
docker compose run web sh -c "pytest tests/test_folder/test_file.py"
```
