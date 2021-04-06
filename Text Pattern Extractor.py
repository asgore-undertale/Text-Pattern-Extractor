def find_pattern(file_content, text):
    fromfile_text, table = '', {}
    r = 0
    for char in file_content:
        if len(fromfile_text) == len(text):
            show_result(fromfile_text, text, table)
            file_content = file_content.replace(fromfile_text, '')
            r -= len(fromfile_text) +1
            fromfile_text, table = '', {}
            
        if char in table and table[char] != text[len(fromfile_text)]:
            r -= len(fromfile_text) +1
            fromfile_text, table = '', {}
        
        for k, v in table.items():
            if v == text[len(fromfile_text)] and k != char:
                r -= len(fromfile_text) +1
                fromfile_text, table = '', {}
            
        fromfile_text += char
        table[char] = text[len(fromfile_text)-1]
        r += 1

    if len(fromfile_text) == len(text): show_result(fromfile_text, text, table)

def show_result(fromfile_text, text, table):
    print(fromfile_text)
    print(text)
    print(table)

find_pattern(open(input()).read(), 'You will have to do better than that.')#

input('task completed')