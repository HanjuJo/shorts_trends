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
st.title("All-in-One 유틸리티 대시보드")
st.sidebar.title("🔧 기능 선택")
menu = st.sidebar.radio("메뉴", ["유튜브 분석", "SNS 분석", "SEO 분석", "AI 도구", "기타 유틸리티"])
st.write(f"현재 선택한 메뉴: {menu}")
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
    "frontend/pages/index.js": '''export default function Home() {
  return (
    <div className="flex items-center justify-center h-screen">
      <h1 className="text-2xl font-bold">All-in-One 유틸리티 대시보드</h1>
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
