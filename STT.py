import whisper
import time
from win10toast import ToastNotifier

start_time = time.time()

# 모델 크기 : tiny, base, small, medium, large
model = whisper.load_model("medium")

# 음성 파일 경로
audio_path = "file_path"

# 음성 파일을 텍스트로 변환 
current_time = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", current_time)
print("STT start!, 현재 시간:", formatted_time)
result = model.transcribe(audio_path, task="transcribe")

# 변환된 텍스트출력
for segment in result['segments']:
    start = segment['start']
    end = segment['end']
    text = segment['text']
    print(f"[{start:.0f}s - {end:.0f}s]: {text}")

# 텍스트를 파일로 저장
with open("10-28.txt", "w", encoding="utf-8") as file:
    for segment in result['segments']:
        start = segment['start']
        end = segment['end']
        text = segment['text']
        file.write(f"[{start:.0f}s - {end:.0f}s]: {text}\n")

end_time = time.time()

elapsed_time = end_time - start_time
print(f"프로그램이 완료되는 데 걸린 시간: {elapsed_time:.2f}초")
toaster = ToastNotifier()
toaster.show_toast("Alert", "Alert",duration=10)