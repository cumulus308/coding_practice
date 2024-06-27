#!/usr/bin/env python 
import os
from urllib import parse
import sys

HEADER = """# 
# 백준 & 프로그래머스 문제 풀이 목록
프로그래머스의 경우, 푼 문제 목록에 대한 마이그레이션이 필요합니다.
"""

def main():
    try:
        content = HEADER
        
        directories = []
        solveds = []
        for root, dirs, files in os.walk("."):
            dirs.sort()
            if root == '.':
                for dir in ('.git', '.github'):
                    try:
                        dirs.remove(dir)
                    except ValueError:
                        pass
                continue
            category = os.path.basename(root)
            
            if category == 'images':
                continue
            
            directory = os.path.basename(os.path.dirname(root))
            
            if directory == '.':
                continue
                
            if directory not in directories:
                if directory in ["백준", "프로그래머스"]:
                    content += "## 📚 {}\n".format(directory)
                else:
                    content += "### 🚀 {}\n".format(directory)
                    content += "| 문제번호 | 링크 |\n"
                    content += "| ----- | ----- |\n"
                directories.append(directory)
            for file in files:
                if category not in solveds:
                    content += "|{}|[링크]({})|\n".format(category, parse.quote(os.path.join(root, file)))
                    solveds.append(category)
                    print("category : " + category)
                    print("file : " + file)
        
        with open("README.md", "w") as fd:
            fd.write(content)
        print("README.md 업데이트 완료")
    except Exception as e:
        print(f"오류 발생: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()