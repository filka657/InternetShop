# InternetShop

Web application development as a course work on the subject of Methods and means of designing information systems and technologies

## Description

The project is an internet shop management system that allows the administrator to monitor the supply of goods. The implementation involves creating a web application using the Flask framework. The program consists of two parts. The first part is db_connection, which connects to the PostgreSQL database and performs queries to provide data from tables. The second part is responsible for presenting data to the client. Connection to the database is made using the sql_alchemy library.


## Database schema

![database_schema](misc/images/database_schema.png)


## Used libraries

- Flask
- SQLAlchemy
- Requests

## Project structure
```
.  
├── [db_connection](https://github.com/filka657/InternetShop/tree/develop/db_connection)/                      # folder for the database connection module  
|    ├── Task1/  
|    ├── Task2/  
|    ├── Task3/  
|    ├── Task4/  
|    ├── Qualification_Tasks.pdf        # full description of the tasks  
|    └── README.md                      # short description of the tasks  
|  
├── MainPart/  
|    ├── monolith_client/               # the latest working version  
|    ├── mqtt_gpio/                     # modern code-style, but unstabely working on robot example  
|    ├── Convert_coordinates.cpp        # cpp code for convertion for screen to floor coordinates  
|    └── mosquitto.conf                 # basic config for mqtt broker  
|
├── entities/                           # tries of the IPC implementation  
|  
├── .gitignore  
├── antivirus.png  
└── README.md                           # you are here  
```
