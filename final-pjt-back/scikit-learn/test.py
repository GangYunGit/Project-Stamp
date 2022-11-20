from sklearn.feature_extraction.text import TfidfVectorizer
sentences = ("평범하고 내성적인 고등학생 피터 파커는 우연히 방사능에 감염된 거미에 물린다.그 후, 피터는 손에서 거미줄이 튀어 나오고 벽을 기어 오를 수 있는 거미와 같은 능력을 갖게 된다.",
        "창업 1년 반 만에 직원 220명의 성공신화를 이룬 줄스(앤 해서웨이)는 TPO에 맞는 패션센스, 업무를 위해 사무실에서도 끊임 없는 체력관리 뿐만 아니라 고객을 위해 포장까지 직접 하는 열정적인 30세 여성 CEO이다. 회사에서 은퇴해 무료한 일상을 이어가고 있던 벤(로버트 드니로)은 시니어 인턴을 뽑는다는 어느 온라인 회사에 지원한다.")
tfidf_vectorizer = TfidfVectorizer()

# 문장 벡터화 하기(사전 만들기)
tfidf_matrix = tfidf_vectorizer.fit_transform(sentences)

### 코사인 유사도 ###
from sklearn.metrics.pairwise import cosine_similarity
# 첫 번째와 두 번째 문장 비교
cos_similar = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
print("코사인 유사도 측정")
print(cos_similar)