# Course Recommendation API (Flask + TF-IDF)

This project is a **Flask-based REST API** that recommends similar courses based on a given course name and description.  
It supports **English and Arabic languages** and uses **TF-IDF vectorization with cosine similarity** to generate recommendations.


---


## Features

- REST API endpoint for course recommendations
- Supports **English** and **Arabic**
- Uses **TF-IDF + Cosine Similarity**
- SQL Server database integration
- Returns **Top-N similar courses**


---


## Project Structure

├── app.py # Flask application
├── database.py # Database connection and queries
├── recommendation.py # Course recommendation logic
├── constant.py # Language constants
└── README.md


---


## Technologies Used

- Python
- Flask
- Pandas
- scikit-learn
- pyodbc
- SQL Server
- TF-IDF Vectorizer


---


## Language Support

| Language | ID |
|----------|----|
| Arabic   |  7 |
| English  |  8 |

Defined in `constant.py`:
```python
LANG_ARABIC = 7
LANG_ENGLISH = 8
```

---


## Database Tables Used

**English Courses**

- Table: Course
- Columns used: CourseName, Description

**Arabic Courses**

- Table: CourseTranslation
- Columns used: CourseName, Description


---


## API Endpoint(POST /recommend)
**Request Body (JSON):**
{
  "CourseName": "Machine Learning",
  "Description": "Introduction to ML algorithms",
  "IdLang": 8
}

**Response (JSON):**
[
    {
        "CourseName": "Machine Learning",
        "Description": ""
    },
    {
        "CourseName": "Applying Artificial Intelligence and Machine Learning Algorithms in Conducting Applied Scientific Research Without Programming Using Orange Software Across Various Scientific Fields.",
        "Description": "<p>This training module introduces participants to the practical use of Artificial Intelligence (AI) and Machine Learning (ML) in scientific research without programming or advanced mathematics. The course relies on Orange Data Mining as a visual, user-friendly platform that enables researchers to analyze data, discover patterns, and generate research insights efficiently.</p><p> </p><p>The course focuses on hands-on applications of AI and ML algorithms using <strong>Orange software</strong>.</p><p>Participants will learn data preparation, exploratory data analysis, classification, clustering, prediction, and model evaluation for academic research purposes.</p>"
    },
    {
        "CourseName": "Introduction to DevOps",
        "Description": ""
    },
    {
        "CourseName": "Introduction to Digital Diplomacy",
        "Description": ""
    },
    {
        "CourseName": "Introduction to ChatGPT Applications in Business",
        "Description": ""
    }
]


---


## Recommendation Logic

- Combine CourseName and Description
- Apply TF-IDF vectorization
- Remove stop words (English or Arabic)
- Compute cosine similarity
- Return Top 5 most similar courses


---


## How to Run
- Install Dependencies: pip install flask pandas scikit-learn pyodbc
- Configure Database: Make sure SQL Server is running and update connection settings in database.py.
- Run the Application: python app.py
- The API will be available at: http://127.0.0.1:5000/recommend


---


## Future Improvements

- Cache TF-IDF matrix
- Improve Arabic NLP preprocessing
- Add authentication
- Dockerize the application