# How to Run the Application
1. Put the key from service-account that has a Storage Object Administrator role in the ./Cloud Computing/ directory
2. Create a .env file that has these variable MYSQL_ROOT_PASSWORD, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE, and DB_HOST in the ./Cloud Computing./ directory
3. Change machine learning endpoint in ./Cloud Computing/src/handler/prediction_handler.js and the projectid & bucket name in ./Cloud Computing/src/service/storage_service.js
4. Run your MySQL server in your local environment that listens in port 3306
5. Run "npm install" in the terminal
6. Run "npm run start" in the terminal

# How to Run the Application using Docker
1. Put the key from service-account that has a Storage Object Administrator role in the ./Cloud Computing./ directory
2. Create a .env file that has these variable MYSQL_ROOT_PASSWORD, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE, and DB_HOST in the ./Cloud Computing/ directory
3. Change machine learning endpoint in <a href="https://github.com/farreljordan80/agroaid/blob/main/Cloud%20Computing/src/handler/prediction_handler.js">./Cloud Computing/src/handler/prediction_handler.js<a/> and the projectid & bucket name in <a href="https://github.com/farreljordan80/agroaid/blob/main/Cloud%20Computing/src/service/storage_service.js">./Cloud Computing/src/service/storage_service.js<a/>
4. Make sure your docker daemon is running
5. Run "docker compose up" in the terminal

# Test the Applicaiton
You can test the application using the files in <a href="https://github.com/farreljordan80/agroaid/blob/main/Cloud%20Computing/src/service/storage_service.js">./Cloud Computing/postman<a/> directory and import it on postman

# API Documentation
<a href="https://docs.google.com/document/d/1uaIMPnmDC0Pq4dU3m8ATFstdMVRH9fKyD2HgUmBfQC0/edit?usp=sharing">Link for the API Documentation<a/>
