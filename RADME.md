## The following are the steps to run the code
1. Install the required packages and create the docker image for the kafka producer
--- this will be done within docker container in the kafka-producer folder
    --- To do this, run the following command:
    ```docker build -t kafka-producer .```
    *make sure you are in the kafka-producer folder*
    
    --- This will create a docker image with the name `kafka-producer`

--- We do also have wait-for-it.sh script which will wait for the kafka **zookeeper** and kafka **server** to be up and running before running the **producer**

--- wthin the docker container, we have the following files:
    --- kafka-producer.py - this is the python script that will produce the messages to the kafka topic also dummy data is generated using faker library also topic declaration is done here
    --- requirements.txt - this is the list of packages that are required to run the python script
    --- wait-for-it.sh - this is the script that will wait for the kafka **zookeeper** and kafka **server** to be up and running before running the **producer**

2. Setup for tthe flink processor
---- In this folder, we have the following files and folder:
    --- wait-for-it.sh - this is the script that will wait for the kafka **zookeeper** and kafka **server** to be up and running before running the **producer**
    --- pom.xml - this is the maven pom file that will be used to build the flink processor also configuration for flink is done here
    --- Dockerfile - this is the dockerfile that will be used to build the docker image for the flink processor configure wait-for-it.sh script is also done here also target/flink-processor-1.0-SNAPSHOT.jar is copied to the docker image 
    
    NB: target folder is created after building the flink processor with some java files
    --- flink-processor-1.0-SNAPSHOT.jar is the jar file that is generated after building the flink processor
      --- how to get while inside flink-processor folder run the following command:
      ```mvn clean install```
      --- this will generate the jar file in the target folder
    
    ---src/main
        ---java
        Here we have the following files:
        --- Main.java - this is the main class that will be used to run the flink processor
        ---Weather.java - this is the class that will be used to create the weather object
        ---WeatherDeserializer.java - this is the class that will be used to deserialize the weather object

        ---resources
        Here we have the following files:
        ---log4j.properties - this is the log4j configuration file responsible for logging the flink processor
**What to do:** 
    --- run the following command to build the docker image for the flink processor:
    ```docker build -t flink-processor .```
    *make sure you are in the flink-processor folder*

3. Setup for the kafka consumer
--- Postgress will be our kafka consumer
--- In this folder, we have the following files and folder:
    --- Dockerfile - this is the dockerfile that will be used to build the docker image for the kafka consumer
    -- It will have the script for creating the database and tables `create_table.sql`
    --- create_table.sql - this is the script that will be used to create the database and tables having the following columns:
    --- id - this is the id of the city
    --- city - this is the name of the city
    --- average_temperature - this is the average temperature of the city

    --- Command for buitling the docker image:
    ```docker build -t postgres .```

4. Finally run the docker compose file to run all the containers
--- This will run the kafka producer, flink processor and kafka consumer
--- Command for running the docker compose file:
            ```docker-compose up``` -- to run the containers
            ```docker-compose down``` -- to stop the containers

    --- Reaching the postgres container:
    --- Command for reaching the postgres container:
```docker exec -it postgres psql -U postgres -d postgres```
--- you will enter the postgres container and you can run the following command to see the data in the database:
    ```/dt```
    --- you will see the created table:
--- you can also run the following command to see the data in the database:
    ```SELECT * FROM weather;```
    


