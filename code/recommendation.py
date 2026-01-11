from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from constant import LANG_ARABIC,LANG_ENGLISH

class CourseRecommender:
    def __init__(self, df,IdLang):
        self.df = df.copy()
        self.df["CourseName"] = self.df["CourseName"].fillna("").astype(str)
        self.df["Description"] = self.df["Description"].fillna("").astype(str)

        self.df["text"] = self.df["CourseName"].str.strip() + " " + self.df["Description"].str.strip()
        if(IdLang==LANG_ENGLISH):
            self.vectorizer = TfidfVectorizer(stop_words="english")
          
        
        elif(IdLang==LANG_ARABIC):
            stop_words_arabic=[    "و","في","على","من","إلى","عن","مع","ما","ماذا",
                                 "هذا","هذه","ذلك","الذي","التي",
                                "كان","كانت","يكون","تكون",
                                    "هو","هي","هم","هن",
                                "أنا","نحن","أنت","أنتم"]
            self.vectorizer = TfidfVectorizer(stop_words=stop_words_arabic)
        self.tfidf_matrix = self.vectorizer.fit_transform(self.df["text"])
    def recommend_input(self, CourseName, Description, top=5):
        input_text = f"{CourseName} {Description}"
        input_vector = self.vectorizer.transform([input_text])
        scores = cosine_similarity(input_vector, self.tfidf_matrix).flatten()
        indices = scores.argsort()[::-1][:top]
        result = self.df.iloc[indices]

        
        return result[["CourseName", "Description"]].to_dict(orient="records")
    
