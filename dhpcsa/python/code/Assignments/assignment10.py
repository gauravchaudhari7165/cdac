# Assignment 1: Replace a Keyword in a Text File
# Search for all occurrences of keyword 'after', replace it with 'before’. Save modified content back to file. 
# Create functions wherever appropriate.

def replace_keyword(file_name, keyword, replacement):
    with open(file_name, 'r') as file:
        content = file.read()
    content = content.replace(keyword, replacement)
    with open(file_name, 'w') as file:
        file.write(content)


file_name = 'sample.txt'
keyword = 'after'
replacement = 'before'
replace_keyword(file_name, keyword, replacement)

