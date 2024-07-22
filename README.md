# README

## Overview
The Course Allocation System project explores the integration between RDBMS and NoSQL databases using the GILHARI microservice framework, a product of Software Tree. GILHARI, available in a Docker image, is configurable to fit application-specific object and relational models. It exposes a REST interface to provide APIs (POST, GET, PUT, DELETE…) for CRUD (Create, Retrieve, Update, and Delete) operations on application-specific JSON objects, eliminating the need to write code to handle REST APIs or access the database directly.

This project demonstrates how the GILHARI microservice framework can be used to transfer JSON data between a relational database (MySQL) and a NoSQL database (MongoDB) on AWS.

## Project Objectives
The main objectives of this project are to:
1. Reverse-engineer a JSON object model and its object-relational mapping from a MySQL database using the JDX ORM.
2. Populate the MySQL database with a number of JSON objects using a Java/Python program or by configuring and using the GILHARI microservice framework (via curl commands to perform POST requests). This step is optional if the MySQL database already contains the necessary data.
3. Retrieve existing data from the MySQL database using one instance of the GILHARI microservice and transfer the data to a MongoDB NoSQL database using another instance of the GILHARI microservice configured for MongoDB.

## Description
The project simulates a library management system. On the "server" side, there is a MySQL source database with tables containing data of Books, Authors, Members, and Loans. On the "client" side, there is a MongoDB destination database configured to store the transferred data.

There are two instances of GILHARI (one for the server and one for the client). The first instance (listening on port 8080) uses GET requests to stream data from the MySQL database. The second instance (listening on port 8083) then uses POST requests to send the retrieved data to the MongoDB database.

Due to the database-agnostic nature of GILHARI, switching between the two databases is straightforward. For the NoSQL part, we utilized native MongoDB APIs for data transfer, ensuring efficient and reliable data handling.

## Setup and Implementation
### Prerequisites
- Docker installed on your local machine.
- MySQL and MongoDB instances running on your local machine or accessible via a network.
- Java Development Kit (JDK) installed.
-  MySQL Connector/J JDBC Driver (`mysql-connector-j-9.0.0`)
## Running this Project
- Launch an Amazon-Linux EC2 Instance (free tier), conifgure security and vpc as default. Note the public IPv4 address.

- Connect to the instance and install docker. Provide access to ec2-user. It is advised to use PuTTY to SSH into the instance if you are using Windows. Close the connection and reconnect to let the changes to reflect.

-On separate command terminals, ssh into the EC2 instance to run a Gilhari instance each. Pull the docker images using the command docker pull public.ecr.aws/q9i6k2u6/gillib:s3 and docker pull public.ecr.aws/q9i6k2u6/gillib:t3. Then run the docker images using docker run -p 8082:8081 public.ecr.aws/q9i6k2u6/gillib:s3 and docker run -p 8083:8081 public.ecr.aws/q9i6k2u6/gillib:t3 respectively.

-Once the Gilhari instances are up and running successfully, the transfer can be performed. Here, we use a python program to do the same.


  
