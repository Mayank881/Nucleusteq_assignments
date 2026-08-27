from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection

from app.config import DATABASE_NAME, MONGODB_URL
from app.constants.app_constants import (
    COMMENT_COLLECTION,
    ISSUE_COLLECTION,
    PROJECT_COLLECTION,
    SPRINT_COLLECTION,
    USER_COLLECTION,
)

client: MongoClient = MongoClient(MONGODB_URL)

db: Database = client[DATABASE_NAME]

users_collection: Collection = db[USER_COLLECTION]
projects_collection: Collection = db[PROJECT_COLLECTION]
issues_collection: Collection = db[ISSUE_COLLECTION]
sprints_collection: Collection = db[SPRINT_COLLECTION]
comments_collection: Collection = db[COMMENT_COLLECTION]