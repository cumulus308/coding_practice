#!/usr/bin/env python 
import os
from urllib import parse
import sys
import traceback

HEADER = """# 백준 & 프로그래머스 문제 풀이 목록
"""

def main():
    try:
        print("스크립트 실행 시작")
        content = HEADER
        
        directories = []
        solveds = []
        
        print(f"현재 작업 디렉토리: {os.getcwd()}")
        print("디렉토리 내용:")
        print(os.listdir('.'))
        
        for root, dirs, files in os.walk("."):
            dirs.sort()
            print(f"Processing directory: {root}")
            
            category = os.path.basename(root)
            
            # 불필요한 디렉토리 건너뛰기
            if category in ['.', '.git', '.github']:
                continue
            
            directory = os.path.basename(os.path.dirname(root))
            
            if directory == '.':
                continue
                
            if directory not in directories:
                if directory in ["백준", "프로그래머스"]:
                    content += f"## 📚 {directory}\n"
                elif directory not in ['.', '.git', '.github']:  # 최상위 디렉토리와 Git 관련 디렉토리 제외
                    content += f"### 🚀 {directory}\n"
                    content += "| 문제번호 | 링크 |\n"
                    content += "| ----- | ----- |\n"
                directories.append(directory)
            
            for file in files:
                print(f"Found file: {file}")
                if file.endswith('.py'):
                    problem_number = category
                    if directory == "프로그래머스":
                        problem_number = category.split('.')[0]
                    if problem_number not in solveds:
                        relative_path = os.path.relpath(os.path.join(root, file), ".")
                        content += f"|{problem_number}|[링크]({parse.quote(relative_path)})|\n"
                        solveds.append(problem_number)
                        print(f"Added problem: {problem_number}")
        
        print("README.md 파일 작성 시작")
        with open("README.md", "w", encoding="utf-8") as fd:
            fd.write(content)
        print("README.md 업데이트 완료")
        
    except Exception as e:
        print(f"오류 발생: {e}", file=sys.stderr)
        print(f"오류 타입: {type(e).__name__}", file=sys.stderr)
        print("상세 오류 정보:", file=sys.stderr)
        print(traceback.format_exc(), file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
