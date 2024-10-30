from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from youtube_transcript_api import YouTubeTranscriptApi
import time

# 1. 뉴스 기사 페이지 여부를 확인하는 함수
def is_news_page(url):
    if "youtube.com" in url or "youtu.be" in url:
        return False  
    elif "news" in url or "article" or "arti" in url: 
        return True
    else:
        return None  

# 2. 뉴스 기사 크롤링 함수
def crawl_news(driver):
    try:
        # 기사 본문 크롤링 - 모든 <p> 태그를 가져와 본문 내용을 합침
        paragraphs = driver.find_elements(By.TAG_NAME, "p")
        article_content = "\n".join([para.text for para in paragraphs])
        print(f"\n본문:\n{article_content}")

    except Exception as e:
        print(f"뉴스 크롤링 중 오류 발생: {e}")

# 3. 유튜브 자막 크롤링 함수
def crawl_youtube_transcript(video_id):
    try:
        # 유튜브 자막 언어 자동 판별 후 자막 추출
        transcript = None
        available_transcripts = YouTubeTranscriptApi.list_transcripts(video_id)
        # 사용할 수 있는 자막 중에서 한국어 자막을 우선적으로 찾음
        for transcript_data in available_transcripts:
            if transcript_data.language_code == 'ko':
                transcript = transcript_data.fetch()  # 한국어 자막을 가져옴
                break
        # 한국어 자막이 없으면 첫 번째 사용 가능한 자막을 가져옴
        if transcript is None:
            transcript = available_transcripts.find_manually_created_transcript([available_transcripts[0].language_code]).fetch()
        # 자막 텍스트만 추출하여 출력
        script_text = "\n".join([entry['text'] for entry in transcript])  # 타임스탬프 제거
        print("\n 자막 내용:")
        print(script_text)
    except Exception as e:
        print(f"ERR: {e}")

# 4. 메인 함수
def main():
    url = input("크롤링할 페이지의 URL을 입력하세요: ")  # 사용자로부터 URL 입력 받기

    page_type = is_news_page(url)
    if page_type is True:
        # 뉴스 기사 크롤링
        options = webdriver.ChromeOptions()
        options.add_argument("--headless") 
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get(url)
        time.sleep(3)  # 페이지 로딩 대기
        crawl_news(driver)
        driver.quit()

    elif page_type is False:
        # 유튜브 영상 ID 추출 (유튜브 URL에서 video_id를 추출하는 간단한 방법)
        if "watch?v=" in url:
            video_id = url.split("watch?v=")[-1]
        elif "youtu.be" in url:
            video_id = url.split("youtu.be/")[-1]
        else:
            print("유효한 유튜브 URL이 아닙니다.")
            return

        crawl_youtube_transcript(video_id)
    else:
        print("지원하지 않는 페이지입니다. 뉴스 기사나 유튜브 영상만 크롤링할 수 있습니다.")


if __name__ == "__main__":
    main()