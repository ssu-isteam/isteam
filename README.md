[![Build Status](https://travis-ci.com/ssu-isteam/isteam.svg?branch=master)](https://travis-ci.com/ssu-isteam/isteam)

<p align="center">
 <img src="https://user-images.githubusercontent.com/24839897/90855719-383af980-e3bb-11ea-82e3-b28afa9e1531.png" alt="고로_숭실" width="auto" height="50px">
</p>

## 모듈 설명
### main_page
* 메인 페이지

### user
* 회원 모델 저장
* 로그인 프로세스, 회원가입 프로세스 등 사용자 관련된 것

### groupware
* 진행한 활동 기록, 팀 프로젝트 생성 등
 
### recruit
* 부원 모집 관련(비활성화 시에도 애플리케이션 실행 가능)
 
## 실행방법
 * 패키지 관리자: [Poetry](https://python-poetry.org)
 * Python 버전: 3.7 이상
 * 데이터베이스: MySQL 5
 
 ---

### 단순 실행방법
- linux
    ```shell
    chmod 711 ./scripts/local-init.sh ./scripts/run-local.sh
    ./scripts/local-init.sh
    ./scripts/run-local.sh
    ```

### 1. Poetry 설치
Linux, macOS, Git bash on Windows 등등:
```shell
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

Windows PowerShell:
```shell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -
```

### 2. Poetry가 가상 환경을 생성하도록 설정
```sh
poetry config virtualenvs.in-project true
```

### 3. 패키지 설치
```sh
poetry install
```

### 4. 프로젝트 최상단에 `.env`파일 생성 후 아래와 같이 작성
예시:
```
DATABASE_NAME=isteam
DATABASE_USER=root
DATABASE_PASS=1234
DATABASE_HOST=localhost

EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=foo@gmail.com
EMAIL_HOST_PASSWORD=foobar
EMAIL_USE_TLS=True
SERVER_EMAIL=foo@gmail.com
DEFAULT_FROM_EMAIL=EMAIL_HOST_USER

RECAPTCHA_SECRET=foobar

STATIC_PATH=static
MEDIA_PATH=media
```

데이터베이스, 이메일, 캡챠는 직접 세팅해야 합니다.

### 5. 모델 마이그레이션
```sh
cd isteam
./manage.py migrate
```

### 6. CSS 파일 빌드
```
npm i
npm run bundle
```

### 7. (선택사항) PyCharm을 사용하는 경우 [Poetry 플러그인](https://plugins.jetbrains.com/plugin/14307-poetry) 설치

