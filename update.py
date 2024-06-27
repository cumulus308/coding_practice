#!/usr/bin/env python 
import os
from urllib import parse
import sys

HEADER = """# 
# 백준 & 프로그래머스 문제 풀이 목록
"""

def main():
    try:
        content = HEADER
        
        directories = []
        solveds = []
        
        # 현재 스크립트의 위치를 기준으로 상위 디렉토리로 이동
        os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        
        for root, dirs, files in os.walk("coding_practice"):
            dirs.sort()
            print(f"Processing directory: {root}")  # 디버깅을 위한 로그 추가
            
            category = os.path.basename(root)
            
            if category in ['.git', '.github', 'images']:
                continue
            
            directory = os.path.basename(os.path.dirname(root))
            
            if directory == 'coding_practice':
                continue
                
            if directory not in directories:
                if directory in ["백준", "프로그래머스"]:
                    content += f"## 📚 {directory}\n"
                    content += "| 문제번호 | 링크 |\n"
                    content += "| ----- | ----- |\n"
                else:
                    content += f"### 🚀 {directory}\n"
                    content += "| 문제번호 | 링크 |\n"
                    content += "| ----- | ----- |\n"
                directories.append(directory)
            
            for file in files:
                print(f"Found file: {file}")  # 디버깅을 위한 로그 추가
                if file.endswith('.py'):  # Python 파일만 처리
                    problem_number = category
                    if directory == "프로그래머스":
                        # 프로그래머스 문제 번호 추출 (예: "120807. 숫자 비교하기" -> "120807")
                        problem_number = category.split('.')[0]
                    if problem_number not in solveds:
                        relative_path = os.path.relpath(os.path.join(root, file), "coding_practice")
                        content += f"|{problem_number}|[링크]({parse.quote(relative_path)})|\n"
                        solveds.append(problem_number)
                        print(f"Added problem: {problem_number}")  # 디버깅을 위한 로그 추가
        
        readme_path = os.path.join("coding_practice", "README.md")
        with open(readme_path, "w", encoding="utf-8") as fd:
            fd.write(content)
        print(f"README.md 업데이트 완료: {readme_path}")
    except Exception as e:
        print(f"오류 발생: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
