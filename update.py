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
        
        for root, dirs, files in os.walk("."):
            dirs.sort()
            print(f"Processing directory: {root}")
            
            category = os.path.basename(root)
            
            if category in ['.git', '.github', 'images']:
                continue
            
            directory = os.path.basename(os.path.dirname(root))
            
            if directory == '.':
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
        
        with open("README.md", "w", encoding="utf-8") as fd:
            fd.write(content)
        print("README.md 업데이트 완료")
    except Exception as e:
        print(f"오류 발생: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
