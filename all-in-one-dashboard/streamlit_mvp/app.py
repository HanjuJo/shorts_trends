import os

# 프로젝트 루트 폴더
PROJECT_NAME = "all-in-one-dashboard"
BASE_DIR = os.path.join(os.getcwd(), PROJECT_NAME)

# 폴더 구조 정의
FOLDERS = [
    "streamlit_mvp/pages", "streamlit_mvp/assets", "streamlit_mvp/utils",
    "backend/api", "backend/utils",
    "frontend/components", "frontend/pages", "frontend/styles", "frontend/assets",
    "deploy/.github/workflows"
]

# 파일 구조 정의
FILES = {
    "streamlit_mvp/app.py": '''import streamlit as st

st.set_page_config(page_title="All-in-One 유틸리티 대시보드", layout="wide")

st.sidebar.title("🔧 기능 선택")
menu = st.sidebar.radio("메뉴", ["유튜브 분석", "SNS 분석", "SEO 분석", "AI 도구", "기타 유틸리티"])

st.title("🎯 올인원 분석 도구 대시보드")

if menu == "유튜브 분석":
    st.subheader("📊 유튜브 데이터 분석")
    youtube_url = st.text_input("유튜브 채널 또는 영상 URL 입력")
    if st.button("분석 시작"):
        st.success("유튜브 데이터 분석 중...")

elif menu == "SNS 분석":
    st.subheader("📱 SNS 트렌드 분석")
    platform = st.selectbox("플랫폼 선택", ["인스타그램", "틱톡", "트위터"])
    keyword = st.text_input("분석할 키워드 입력")
    if st.button("검색"):
        st.success(f"{platform}에서 '{keyword}' 관련 트렌드 분석 중...")

elif menu == "SEO 분석":
    st.subheader("🌍 SEO 및 웹사이트 분석")
    website_url = st.text_input("분석할 웹사이트 URL 입력")
    if st.button("분석"):
        st.success(f"'{website_url}' 웹사이트 SEO 분석 중...")

elif menu == "AI 도구":
    st.subheader("🤖 AI 기반 콘텐츠 생성 도구")
    ai_input = st.text_area("문장 또는 키워드 입력")
    if st.button("AI 생성"):
        st.write("AI가 생성한 문장 출력...")

elif menu == "기타 유틸리티":
    st.subheader("🛠 기타 유틸리티 도구")
    option = st.selectbox("사용할 도구", ["환율 변환기", "BMI 계산기", "JSON 포매터"])
    if st.button("실행"):
        st.success(f"{option} 실행 중...")
''',

    "streamlit_mvp/requirements.txt": "streamlit\ngoogle-auth\ngoogleapiclient\npandas\nrequests",
    "streamlit_mvp/README.md": "# Streamlit MVP",

    "backend/main.py": '''from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI 서버 실행 중"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
''',
    "backend/api/youtube.py": "# 유튜브 API 처리 코드 작성",
    "backend/api/seo.py": "# SEO 분석 API 코드 작성",
    "backend/api/sns.py": "# SNS 분석 API 코드 작성",
    "backend/requirements.txt": "fastapi\nuvicorn\nrequests\npandas\ngoogle-auth\ngoogleapiclient\ntweepy",

    "frontend/package.json": '''{
  "name": "frontend",
  "version": "1.0.0",
  "dependencies": {
    "next": "latest",
    "react": "latest",
    "react-dom": "latest",
    "axios": "latest",
    "tailwindcss": "latest"
  }
}''',

    "frontend/pages/index.js": '''import Head from "next/head";

export default function Home() {
  return (
    <div className="flex items-center justify-center h-screen">
      <Head>
        <title>All-in-One 유틸리티 대시보드</title>
      </Head>
      <h1 className="text-2xl font-bold">올인원 유틸리티 대시보드</h1>
    </div>
  );
}''',

    "frontend/styles/tailwind.config.js": '''module.exports = {
  content: ["./pages/**/*.{js,ts,jsx,tsx}", "./components/**/*.{js,ts,jsx,tsx}"],
  theme: { extend: {} },
  plugins: [],
};''',

    "deploy/.github/workflows/ci.yml": '''name: CI/CD
on: [push]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout repository
      uses: actions/checkout@v3
    - name: Set up Python
      uses: actions/setup-python@v3
      with:
        python-version: "3.9"
    - name: Install dependencies
      run: |
        pip install -r backend/requirements.txt
    - name: Run FastAPI
      run: uvicorn backend.main:app --host 0.0.0.0 --port 8000
''',

    "README.md": "# All-in-One Dashboard\n\nFastAPI + Streamlit + React 프로젝트",
}

# 폴더 생성
for folder in FOLDERS:
    os.makedirs(os.path.join(BASE_DIR, folder), exist_ok=True)

# 파일 생성
for file, content in FILES.items():
    file_path = os.path.join(BASE_DIR, file)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

print(f"✅ 프로젝트 구조가 생성되었습니다! 프로젝트 폴더: {BASE_DIR}")
