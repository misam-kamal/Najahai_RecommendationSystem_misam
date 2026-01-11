from flask import Flask, request, jsonify
from database import get_courses, get_courses_arabic
from recommendation import CourseRecommender
from constant import LANG_ARABIC,LANG_ENGLISH


app = Flask(__name__)

@app.route("/recommend", methods=["POST"])

def recommend():
    data = request.get_json()
    CourseName = data.get("CourseName")
    Description = data.get("Description")
    IdLang=data.get("IdLang")
    if(IdLang==LANG_ENGLISH):
        df = get_courses()
        
    elif(IdLang==LANG_ARABIC):
        df=get_courses_arabic()

    recommender = CourseRecommender(df,IdLang)

    result = recommender.recommend_input(CourseName, Description, top=5)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
    
        