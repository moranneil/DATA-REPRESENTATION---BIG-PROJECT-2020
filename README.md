# Data Representation BIG PROJECT 2020

![Image](Images/bigprojectlogo.JPG "Image")

##### Course: HD in Data Analytics
##### Module: Data Representation and Querying
##### Module ID: 52957
##### Student Name: Neil Moran
##### Student ID: G00376338
##### Date: 5th January 2020

<br>

## Introduction

This project is the final project for Data Representation and Querying module. It is a Web Application that performs CRUD operations to a table in an SQL database. The project consists of the following files and folders:

  * dbconfigTemplate.py - This is Database connection detail as used in the dbconfig.py file
  * vehicleDAO.py - This is the Data Access Object python file to connect to the MySQL database
  * restserver.py - This is the Flask python program that maps https requests to individual functions
  * /staticpages/index.html - This is the HTML/JS code that the browser runs to send HTTP requests via Flash rest server 
  * /garage_g00376338/ - This is the DB Import Files Folder containing two DB tables for importing

## Database Detail

The database can be imported in to mySQL or equivlent from the garage_g00376338/ folder. The database has been given a unique name to ensure that it can be imported to another machine for testing. The database details are given below

* Database Name: garage_g00376338
* Tables in DB: vehicle & manufacturer

See image of database detail

![Image](Images/garage_g00376338.JPG "DB garage_g00376338")

The primary key of the manufacturer table manu_code is a foreign key in the vehicle table. see image below.
