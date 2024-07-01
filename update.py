#!/usr/bin/env python 
import os
from urllib import parse
from itertools import zip_longest

# README 파일의 헤더
HEADER = """# 백준 & 프로그래머스 문제 풀이 목록
"""
# 제외할 디렉토리 목록
EXCLUDE_DIRS = {'', '.', '.git', '.github', 'logs', 'refs', 'remotes', 'objects'}

def main():
    print("스크립트 실행 시작")
    content = HEADER
    
    directories = set() # 처리한 디렉토리 집합
    problem_links = [] # 문제 번호와 링크를 저장할 리스트
    
    print(f"현재 작업 디렉토리: {os.getcwd()}")
    
    # 디렉토리 트리 순회
    for root, dirs, files in os.walk("."):
        # 제외할 디렉토리 필터링
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        print(f"Processing directory: {root}")
        
        category = os.path.basename(root) # 현재 디렉토리 이름
        directory = os.path.basename(os.path.dirname(root)) # 상위 디렉토리 이름
        
        # 불필요한 디렉토리 건너뛰기
        if category in EXCLUDE_DIRS or directory in EXCLUDE_DIRS:
            continue
        
        # 새로운 디렉토리 처리
        if directory not in directories:
            if directory in ["백준", "프로그래머스"]:
                content += f"## 📚 {directory}\n"
            else:
                content += f"### 🚀 {directory}\n"
            directories.add(directory)
        
        # 파일 처리
        for file in files:
            if file.endswith('.py'): # 파이썬 파일만 처리
                problem_number = category if directory != "프로그래머스" else category.split('.')[0]
                relative_path = os.path.relpath(os.path.join(root, file), ".")
                problem_links.append((problem_number, parse.quote(relative_path)))
                print(f"Added problem: {problem_number}")
    
    # 4열 테이블 생성
    content += "| 문제번호 | 링크 | 문제번호 | 링크 |\n"
    content += "| ----- | ----- | ----- | ----- |\n"
    for row in zip_longest(*[iter(problem_links)]*2, fillvalue=('', '')):
        content += f"|{row[0][0]}|[링크]({row[0][1]})|{row[1][0]}|[링크]({row[1][1]})|\n"
    
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
