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

# Likes Requirement
I would create a new table called "Likes", This table will have the id field, an id_user field and an id_property, Therefore the id_user will represents an id field from the user table and id property will represents the id field from property table, then I just have manage the likes with their registered rows, example:

- If I am a common user and I want to "like" a property and I click the like button then in  
  the backend I will register a new row with the currently user_id and the property_id from the clicked property, therefore if the row exists the property has been liked

- If the property_id and user_id in the likes table already exists I can view the "like     
  button" light up if my user has already liked de property

- If I liked it again, I will delete the relation between the user and de property and 
  the "like button" will be available again



















