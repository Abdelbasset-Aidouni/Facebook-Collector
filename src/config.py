
CONNECTION_CONF = "mongodb://localhost:27017"
DATABASE_NAME = "facebook"


def get_database():
    from pymongo import MongoClient

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_CONF)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client[DATABASE_NAME]
    
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":    
    
    # Get the database
    dbname = get_database()