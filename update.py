#!/usr/bin/env python 
import os
from urllib import parse
from collections import defaultdict

# README 파일의 헤더
HEADER = """# 백준 & 프로그래머스 문제 풀이 목록
"""
# 제외할 디렉토리 목록
EXCLUDE_DIRS = {'', '.', '.git', '.github', 'logs', 'refs', 'remotes', 'objects'}

def create_table(problem_links):
    table = "| 문제이름 | 링크 | 문제이름 | 링크 |\n"
    table += "| ----- | ----- | ----- | ----- |\n"
    for i in range(0, len(problem_links), 2):
        row = problem_links[i:i+2]
        table += f"|{row[0][0]}|[링크]({row[0][1]})|"
        if len(row) > 1:
            table += f"{row[1][0]}|[링크]({row[1][1]})|\n"
        else:
            table += "|||\n"
    return table

def main():
    print("스크립트 실행 시작")
    content = HEADER
    
    baekjoon_links = defaultdict(list)
    programmers_links = defaultdict(list)
    
    print(f"현재 작업 디렉토리: {os.getcwd()}")
    
    # 디렉토리 트리 순회
    for root, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        print(f"Processing directory: {root}")
        
        parts = root.split(os.sep)
        if len(parts) < 3:
            continue
        
        platform = parts[1]  # '백준' 또는 '프로그래머스'
        sub_category = parts[2]  # 'Bronze' 또는 '0', '1' 등
        
        for file in files:
            if file.endswith('.py'):
                problem_number = os.path.splitext(file)[0].split('.')[0]
                relative_path = os.path.relpath(os.path.join(root, file), ".")
                if platform == "프로그래머스":
                    programmers_links[sub_category].append((problem_number, parse.quote(relative_path)))
                elif platform == "백준":
                    baekjoon_links[sub_category].append((problem_number, parse.quote(relative_path)))
                print(f"Added problem: {problem_number} in {platform}/{sub_category}")
    
    # 프로그래머스 테이블 생성
    content += "## 📚 프로그래머스\n"
    for level, problems in sorted(programmers_links.items()):
        content += f"### 🚀 레벨 {level}\n"
        content += create_table(sorted(problems))
        content += "\n"
    
    # 백준 테이블 생성
    content += "## 📚 백준\n"
    for difficulty, problems in sorted(baekjoon_links.items()):
        content += f"### 🚀 {difficulty}\n"
        content += create_table(sorted(problems))
        content += "\n"
    
    print("README.md 파일 작성 시작")
    
    # 기존 README.md 파일 읽기
    with open("README.md", "r", encoding="utf-8") as f:
        old_content = f.readlines()
    
    # 처음 두 줄은 유지하고 나머지는 새로운 내용으로 대체
    new_content = old_content[:2] + content.split('\n')[1:]
    
    # 수정된 내용을 README.md 파일에 쓰기
    with open("README.md", "w", encoding="utf-8") as f:
        f.write('\n'.join(new_content))
    
    print("README.md 업데이트 완료")

if __name__ == "__main__":
    main()
