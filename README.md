# InternetShop

Web application development as a course work on the subject of Methods and means of designing information systems and technologies

## Description

The project is an internet shop management system that allows the administrator to monitor the supply of goods. The implementation involves creating a web application using the Flask framework. The program consists of two parts. The first part is db_connection, which connects to the PostgreSQL database and performs queries to provide data from tables. The second part is responsible for presenting data to the client. Connection to the database is made using the sql_alchemy library.


## Database schema

![database_schema](misc/images/database_schema.png)


## Technologies

- Flask
- SQLAlchemy
- Requests

## Project structure

```
.  
├── db_connection/                       # module for connection with database
|    ├── templates/                      # html files
|    | 
|    └── main.py                         # module for connection with database 
|  
|  
├── static/                              # components for page styling  
|    ├── css/                            # css files for page styling  
|    ├── fonts/                          # used font on pages
|    └── pics/                           # used pictures on pages
|
|
├── templates/                           # contains all the project's HTML files that display the content  
|    ├── putting/                        # pages for putting entries 
|    ├── adding/                         # pages for adding entries
|    |
|    └── *.html                          # pages for display the content
|  
|  
├── main.py                              # API module
└── README.md
```
