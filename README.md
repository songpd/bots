# bots

Python으로 만드는 디스코드 봇 저장소입니다.

## 요구 사항

- Python 3.10 이상
- 디스코드 봇 토큰 ([Discord Developer Portal](https://discord.com/developers/applications)에서 발급)

## 시작하기

```powershell
git clone https://github.com/songpd/bots.git
cd bots
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## 설정

봇 토큰은 코드에 넣지 않고 `.env` 파일에 저장합니다. `.env`는 `.gitignore`에 포함되어 커밋되지 않습니다.

```powershell
Copy-Item .env.example .env
```

`.env`를 열어 `DISCORD_TOKEN` 값을 발급받은 토큰으로 바꿉니다.

## 실행

```powershell
python bot.py
```

슬래시 명령어는 디스코드에 반영되기까지 시간이 걸릴 수 있습니다.

| 명령어 | 설명 |
|---|---|
| `/ping` | 봇의 응답 속도를 확인합니다. |

## 테스트

```powershell
python -m pytest
```

## 구조

| 경로 | 설명 |
|---|---|
| `bot.py` | 봇 실행 파일과 명령어 정의 |
| `tests/` | 테스트 코드 |
| `requirements.txt` | 필요한 패키지 목록 |
| `.env.example` | `.env` 작성 양식 |
