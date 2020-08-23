# ISTEAM [![Build Status](https://travis-ci.com/5d-jh/isteam.svg?token=3WQchpJY137XqN7bpXmB&branch=master)](https://travis-ci.com/5d-jh/isteam)
<img src="https://user-images.githubusercontent.com/24839897/90855719-383af980-e3bb-11ea-82e3-b28afa9e1531.png" alt="고로_숭실" width="auto" height="50px">

## 모듈 설명
### main_page
메인 페이지

### user
 * 회원 모델 저장
 * 로그인 프로세스, 회원가입 프로세스 등 사용자 관련된 것

### groupware
 * 진행한 활동 기록, 팀 프로젝트 생성 등
 
## 실행방법
 * 에디터: Visual Studio Code
 * Python 버전: => 3.7
 * 프레임워크: Django
 
```sh
python3 -m venv venv
```

에디터 좌측 하단에 `Python 3.7.x (venv:venv)`로 바뀌었는지 확인

```sh
pip install -r requirements.txt
```

프로젝트 최상단에 `.env`파일 생성 후 다음과 같이 작성 (예시)
```
DATABASE_NAME=isteam
DATABASE_USER=root
DATABASE_PASS=1234
DATABASE_HOST=localhost
```

```sh
cd isteam

./manage.py migrate

npm i

npm run bundle
```

좌측 디버거 탭(벌레모양+플레이버튼) 클릭 후 상단의 플레이버튼 클릭시 실행 가능
