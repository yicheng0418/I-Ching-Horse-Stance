from docx import Document
import random

# 定义六个爻位的阴阳符号
YIN = "阴"
YANG = "阳"

# 读取docx文件中的卦爻信息
def read_gua_yao_from_docx(file_path):
    doc = Document(file_path)
    gua_yao_mapping = {}
    table = doc.tables[0]  # 假设卦爻信息在第一个表格中
    for row in table.rows[1:]:  # 跳过表头行，从第二行开始读取数据
        cells = row.cells
        if len(cells) > 1:
            gua_name = cells[0].text.strip()
            gua_yao = [cell.text.strip() for cell in cells[1:]]  # 修改为列表形式
            gua_yao_mapping[gua_name] = gua_yao
    return gua_yao_mapping

# 根据阴阳爻位获取卦名
def get_gua_name_by_yao(gua_yao_mapping, hexagram):
    for gua_name, gua_yao in gua_yao_mapping.items():
        if gua_yao == list(hexagram):
            return gua_name
    return None

# 生成本卦的函数
def generate_base_hexagram():
    base_hexagram = []
    for _ in range(5, -1, -1):
        # 使用掷硬币的方式生成阴阳爻位
        line = random.choice([YIN, YANG])
        base_hexagram.append(line)
    return base_hexagram

# 生成变爻位的函数
def generate_changing_line(base_hexagram):
    # 选择一个随机的爻位作为变爻位
    changing_line_index = random.randint(0, 5)
    # 确定变爻位的阴阳性质
    if base_hexagram[changing_line_index] == YANG:
        changing_line = YIN
    else:
        changing_line = YANG
    return changing_line, changing_line_index

# 根据变爻位生成变卦的函数
def generate_changing_hexagram(base_hexagram, changing_line, changing_line_index):
    changing_hexagram = base_hexagram.copy()
    # 将变爻位的阴阳性质应用到本卦中的变爻位
    changing_hexagram[changing_line_index] = changing_line
    return changing_hexagram

# 提取卦辞内容
def extract_guaci_content(docx_path, gua_name):
    doc = Document(docx_path)
    guaci_content = ""

    for paragraph in doc.paragraphs:
        text = paragraph.text.strip()
        if gua_name in text:
            guaci_content = text
            break

    return guaci_content

def main():
    # 指定卦爻的docx文件路径
    gua_yao_file_path = r"E:\code\易经自动算命\卦爻.docx"  # 替换为实际的文件路径
    # 指定《易经卦辞.docx》的路径
    docx_path = r"E:\code\易经自动算命\易经卦辞.docx"

    # 读取卦爻信息
    gua_yao_mapping = read_gua_yao_from_docx(gua_yao_file_path)

    # 询问用户想要了解的内容
    user_input = input("您想要问什么？")

    # 生成本卦
    base_hexagram = generate_base_hexagram()
    base_gua_name = get_gua_name_by_yao(gua_yao_mapping, base_hexagram)
    print("本卦：", base_hexagram)
    print("本卦卦名：", base_gua_name)
    # 提取本卦卦辞内容
    base_gua_content = extract_guaci_content(docx_path, base_gua_name)
    if base_gua_content:
        print(f"本卦卦辞：{base_gua_content}")
        print("--------------------")
    else:
        print(f"未找到名为'{base_gua_name}'的卦辞")
    
    # 生成变爻位
    changing_line, changing_line_index = generate_changing_line(base_hexagram)
    print("变爻位：第", changing_line_index+1, "爻")

    # 生成变卦
    changing_hexagram = generate_changing_hexagram(base_hexagram, changing_line, changing_line_index)
    changing_gua_name = get_gua_name_by_yao(gua_yao_mapping, changing_hexagram)
    print("变卦：", changing_hexagram)
    print("变卦卦名：", changing_gua_name)

    # 提取变卦卦辞内容
    changing_gua_content = extract_guaci_content(docx_path, changing_gua_name)
    if changing_gua_content:
        print(f"变卦卦辞：{changing_gua_content}")
        print("--------------------")
    else:
        print(f"未找到名为'{changing_gua_name}'的卦辞")

    # 写入卦名到文本文件
    with open("签文.txt", "w", encoding="utf-8") as f:
        f.write(f"本卦卦名：{base_gua_name}\n")
        f.write(f"本卦卦辞：{base_gua_content}\n")
        f.write(f"变卦卦名：{changing_gua_name}\n")
        f.write(f"变卦卦辞：{changing_gua_content}")
        

if __name__ == '__main__':
    main()

