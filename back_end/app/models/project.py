from flask_pymongo import PyMongo
from datetime import datetime

class ProjectModel:

  def __init__(self, mongo: PyMongo):
    self.collection = mongo.cx["test"]["projects"]

  def create_project(self, id, student_id, coderfair_id, name, description, presentation_video_url, code_access_link, coding_language, project_username, project_password, notes):
    project_data = {
      "id": id,
      "student_id": student_id,
      "coderfair_id": coderfair_id,
      "name": name,
      "description": description,
      "presentation_video_url": presentation_video_url,
      "code_access_link": code_access_link,
      "coding_language": coding_language,
      "project_username": project_username,
      "project_password": project_password,
      "notes": notes,
      "created_at": datetime.now(datetime.timezone.utc),
      "updated_at": datetime.now(datetime.timezone.utc),
    }

    #insert_one --> add data (document) into collection
    result = self.collection.insert_one(project_data)
    #inserted_id --> id of the document 
    return str(result.inserted_id)
  
  #model methods:

  #find by username
  def find_project_by_username(self, project_username):
    return list(self.collection.find({"project_username": project_username}))
  
  #find by student id
  def find_project_by_student_id(self, student_id):
    return list(self.collection.find({"student_id": student_id}))

  #find by name
  def find_project_by_name(self, name):
    return self.collection.find_one({"name": name})
  
  #find by id 
  def find_project_by_id(self, id):
    return self.collection.find_one({"id": id})

  #list projects by coderfair
  def list_coderfair_projects(self, coderfair_id):
    return list(self.collection.find({"coderfair_id": coderfair_id}))

  #list all projects
  def list___all_projects(self):
    return list(self.collection.find())