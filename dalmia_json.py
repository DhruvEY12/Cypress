#!/usr/bin/env python3
import sys
from pathlib import Path

file_string = Path('myfile.json').read_text()
stdin_reader = input()
for s in sys.stdin:
    file_string+=s

start_brace_search_result=file_string.find("]{")+1

end_search_result=file_string.find("32m",start_brace_search_result)
result_string=file_string[start_brace_search_result:end_search_result]
print(result_string)