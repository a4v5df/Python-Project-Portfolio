from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from nltk.corpus import stopwords
import re

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

documents = ["test news data"]

# 텍스트 전처리 함수 정의
def preprocess_text(text):
    text = re.sub(r'\W', ' ', text)  
    text = text.lower()            
    text = re.sub(r'\s+', ' ', text) 
    text = ' '.join([word for word in text.split() if word not in stop_words]) 
    return text

# 전처리된 문서 리스트 생성
processed_docs = [preprocess_text(doc) for doc in documents]

# TF-IDF 벡터화
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(processed_docs)

# 벡터화 결과 출력
feature_names = vectorizer.get_feature_names_out()
for i, doc in enumerate(tfidf_matrix.toarray()):
    print(f"Document {i + 1}:")
    for j, score in enumerate(doc):
        print(f"{feature_names[j]}: {score:.3f}")
    print("\n")
