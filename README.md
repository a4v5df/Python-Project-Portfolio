# 파이썬 프로젝트 포트폴리오

## 개요
해당 리포지토리는 지금까지 학습한 프로젝트를 정리한 것 입니다.

---

### 1. 뉴스 및 유튜브 크롤러 (`Crwaling.py`)
- **설명**: `selenium`과 `youtube_transcript_api`를 사용하여 뉴스 기사와 유튜브 자막을 자동으로 수집합니다. URL이 뉴스 기사인지 유튜브 영상인지 판별한 후 해당 콘텐츠를 가져옵니다.
- **사용 기술**: Python, Selenium, YouTube Transcript API
- **학습 내용**: 웹 스크래핑 기법, 구조화된/비구조화된 데이터 처리, Selenium을 이용한 데이터 추출 자동화

---

### 2. 실시간 요소 변경 감지기 (`Web_alert.py`)
- **설명**: 웹페이지에서 특정 요소의 변화를 실시간으로 감지합니다. 변경 사항이 발생하면 데스크톱 알림을 보냅니다. 제품 재고같은 실시간 업데이트 모니터링에 사용하였습니다.
- **사용 기술**: Python, Selenium, win10toast 알림 라이브러리
- **학습 내용**: 웹 요소 모니터링, 멀티스레딩, 알림 자동화

---

### 3. Whisper를 이용한 음성 인식 (`STT.py`)
- **설명**: OpenAI의 Whisper 모델을 사용하여 오디오 파일을 텍스트로 변환하는 음성 인식 프로그램입니다. 변환 결과는 콘솔과 텍스트 파일로 출력됩니다.
- **사용 기술**: Python, Whisper 모델, win10toast
- **학습 내용**: 음성 인식 처리

---

### 4. TF-IDF 텍스트 분석 (`TF_IDF_demo.py`)
- **설명**: 문서에서 중요한 단어를 추출하기 위해 TF-IDF를 계산하는 텍스트 분석 예제입니다. NLP에서 각 단어의 중요도를 평가하는 데 사용하였습니다.
- **사용 기술**: Python, Scikit-Learn, NLTK
- **학습 내용**: 텍스트 전처리, 특징 추출, 자연어 처리 기초

---

### 5. 푸리에 급수 분석 (`f-analysis.py`)
- **설명**: 특정 함수의 푸리에 급수를 계산하고 시각화하는 스크립트로, 복소수 푸리에 변환을 통해 함수 근사치를 구하고 미적분학 학습에 사용하였습니다.
- **사용 기술**: Python, NumPy, Matplotlib
- **학습 내용**: 푸리에 급수 계산, 수학적 시각화

---

### 6. 푸리에 변환 시각화 (`F-Trans.py`)
- **설명**: 특정 함수에 대한 푸리에 변환과 주파수 도메인 표현을 시각화합니다. 두 개의 서브플롯을 통해 함수와 푸리에 변환의 진폭을 보여주는 프로그램입니다.
- **사용 기술**: Python, NumPy, Matplotlib
- **학습 내용**: 푸리에 변환, 신호 처리 시각화, 복잡한 그래프 작성법

---

### 7. 3D 벡터 필드 시각화 (`vector field.py`)
- **설명**: 3D 매개변수 곡선을 생성하고 시각화합니다. 벡터 필드와 3D 매개변수 방정식을 학습할때 시각화를 위해 사용하였습니다.
- **사용 기술**: Python, NumPy, Matplotlib, mpl_toolkits.mplot3d
- **학습 내용**: 3D 그래프 작성, 매개변수 방정식 처리, 벡터 필드 표현

---

