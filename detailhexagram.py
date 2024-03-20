import re
import docx

def read_docx(file_path):
    """读取.docx文件并返回其内容"""
    doc = docx.Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])

def find_gua_info(doc_text, gua_name):
    """在文档中查找并返回指定卦的信息，直到遇到空白行为止"""
    regex_pattern = rf"{gua_name}：.*?(?=\n\s*\n|\Z)"
    matches = re.findall(regex_pattern, doc_text, re.DOTALL)
    return matches[0] if matches else None

def clear_file(filename):
    """清空文本文件的内容"""
    with open(filename, 'w', encoding='utf-8') as file:
        file.truncate(0)

def save_info_to_file(filename, gua_info):
    """将卦的信息保存到文本文件中"""
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(gua_info + "\n\n")

# 主程序

def second_main():
    file_path = '易经白话全文.docx'
    doc_text = read_docx(file_path)

    try:
        with open("shared_gua_names.txt", "r", encoding="utf-8") as f:
            gua_names = [line.strip() for line in f.readlines()]

        for gua_name in gua_names:
            gua_info = find_gua_info(doc_text, gua_name)
            if gua_info:
                print(gua_info)
                save_info_to_file("卦象信息.txt", gua_info)
            else:
                print(f"未找到关于'{gua_name}'的相关卦的信息。")
    except FileNotFoundError:
        print("未找到共享的卦名文件。请先运行第一个脚本生成卦名。")

if __name__ == "__main__":
    second_main()

