# Tools used for this project:
- fastapi
- mysql_connector
- pytest 
- python-dotenv

# Comments before starting

To achieve these requirements I will develop some endpoints, the most important, a GET endpoint to get all available properties and and another GET endpoint to get the especified information about a single property

# Requirements by technical Challenge
Just use a basic mysql-connector to make querys

# Asked JSON for the endpoint consultation

    filter = {
        "limit": 1, 
        "year": 2021, 
        "city": "bogota", 
        "address":  "carrera 100 #15-90"
    }

NOTE: the json body should be sent in query parameters, therefore the backend will parse to json and then make the query





