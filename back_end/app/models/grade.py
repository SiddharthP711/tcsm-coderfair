from flask_pymongo import PyMongo

class GradeModel:
  def __init__(self, mongo: PyMongo):
    self.collection = mongo.cx["test"]["grades"]

  def create_grade(self, concept_tier, concept_mastery, presentation, creativity, overall_grade, judge_id, project_id, overall_comments):
    grade_data = {
      "concept_tier": concept_tier,
      "concept_mastery": concept_mastery,
      "presentation": presentation,
      "creativity": creativity,
      "overall_grade": overall_grade,
      "judge_id": judge_id,
      "project_id": project_id,
      "overall_comments": overall_comments,
    }
    result = self.collection.insert_one(grade_data)
    return str(result.inserted_id)

  def find_grade_by_id(self, id):
    return list(
      self.collection.aggregate(
        [
          {"$match": {"_id": id}},
          {
            "$project": {
            "_id": 0,
            "judge_id": 0,
            "project_id": 0,
            }
          },
        ]
      )
    )

  def list_project_grades(self, project_id):
    return list(self.collection.find({"project_id": project_id}))

  def list_judge_grades(self, judge_id):
    return list(self.collection.find({"judge_id": judge_id}))
  
  def list_grades(self):
    grades = self.collection.aggregate(
      [
        {
          "$project": {"_id": 0}
        }
      ]
    )
    return list(grades)
  
  def update_grade(self, id, update_data):
    result = self.collection.update_one({"_id": id}, {"$set": update_data})
    return result
  
  def delete_grade(self, id):
    result = self.collection.delete_one({"_id": id})
    return result