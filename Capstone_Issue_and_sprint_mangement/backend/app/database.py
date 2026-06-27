from pymongo import MongoClient

from app.config import MONGODB_URL, DATABASE_NAME

# Create MongoDB client
client = MongoClient(MONGODB_URL)

# Select database
db = client[DATABASE_NAME]

# Collections
users_collection = db["users"]
projects_collection = db["projects"]
issues_collection = db["issues"]
sprints_collection = db["sprints"]
comments_collection = db["comments"]