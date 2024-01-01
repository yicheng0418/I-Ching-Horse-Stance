from docx import Document
import random
import datetime

# 定义六个爻位的阴阳符号
YIN = "阴"
YANG = "阳"

BAGUA_YAO_MAPPING = {
    "乾": ["阳", "阳", "阳"],
    "兑": ["阴", "阳", "阳"],
    "离": ["阳", "阴", "阳"],
    "震": ["阴", "阴", "阳"],
    "巽": ["阳", "阴", "阴"],
    "坎": ["阴", "阳", "阴"],
    "艮": ["阴", "阴", "阴"],
    "坤": ["阴", "阴", "阴"]
}

# 定义八卦与数字的对应关系
BAGUA_MAPPING = {
    1: "乾",
    2: "兑",
    3: "离",
    4: "震",
    5: "巽",
    6: "坎",
    7: "艮",
    8: "坤"
}

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

# 修改后的生成本卦函数（使用新的逻辑）
def generate_base_hexagram_new():
    upper_num = random.randint(100, 999)
    lower_num = random.randint(100, 999)

    upper_hexagram_num = upper_num % 8 or 8
    lower_hexagram_num = lower_num % 8 or 8

    upper_gua = BAGUA_MAPPING[upper_hexagram_num]
    lower_gua = BAGUA_MAPPING[lower_hexagram_num]

    # 组合上卦和下卦，确保爻位的顺序（第1爻在底部，第6爻在顶部）
    return BAGUA_YAO_MAPPING[lower_gua] + BAGUA_YAO_MAPPING[upper_gua]

# 修改后的生成变爻函数（使用新的逻辑）
def generate_changing_line_new(base_hexagram):
    changing_num = random.randint(100, 999)
    changing_line_index = changing_num % 6 

    # 确定变爻的阴阳性质（考虑易经的爻位顺序）
    changing_line = YIN if base_hexagram[5 - changing_line_index] == YANG else YANG
    return changing_line, changing_line_index

# 根据变爻位生成变卦的函数
def generate_changing_hexagram(base_hexagram, changing_line, changing_line_index):
    changing_hexagram = base_hexagram.copy()
    # 考虑易经的爻位顺序，第1爻在底部，第6爻在顶部
    # 变爻位的索引需要调整为 5 - changing_line_index
    adjusted_index = 5 - changing_line_index
    # 将变爻位的阴阳性质应用到本卦中的相应爻位
    changing_hexagram[adjusted_index] = changing_line
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

def generate_daily_hexagram(docx_path, gua_yao_mapping):
    # 使用当天的日期作为随机数生成器的种子
    today = datetime.datetime.now()
    random.seed(today.strftime("%Y%m%d"))

    # 生成本卦和变卦的逻辑
    base_hexagram = generate_base_hexagram_new()
    base_gua_name = get_gua_name_by_yao(gua_yao_mapping, base_hexagram)
    base_gua_content = extract_guaci_content(docx_path, base_gua_name)

    changing_line, changing_line_index = generate_changing_line_new(base_hexagram)
    changing_hexagram = generate_changing_hexagram(base_hexagram, changing_line, changing_line_index)
    changing_gua_name = get_gua_name_by_yao(gua_yao_mapping, changing_hexagram)
    changing_gua_content = extract_guaci_content(docx_path, changing_gua_name)

    return {
        "base_gua": base_gua_name,
        "base_gua_content": base_gua_content,
        "changing_gua": changing_gua_name,
        "changing_gua_content": changing_gua_content
    }



def main():
    # 指定卦爻的docx文件路径
    gua_yao_file_path = "卦爻.docx"  # 替换为实际的文件路径
    # 指定《易经卦辞.docx》的路径
    docx_path = "易经卦辞.docx"

    # 读取卦爻信息
    gua_yao_mapping = read_gua_yao_from_docx(gua_yao_file_path)


    # 询问用户想要的功能
    choice = input("请选择功能：1-生成每日一卦，2-随机卦占卜：")
 
    if choice == "1":
        # 生成每日一卦
        daily_gua = generate_daily_hexagram(docx_path, gua_yao_mapping)
        print("今日本卦：", daily_gua["base_gua"])
        print("本卦卦辞：", daily_gua["base_gua_content"])
        print("变卦：", daily_gua["changing_gua"])
        print("变卦卦辞：", daily_gua["changing_gua_content"])  
        
        with open("shared_gua_names.txt", "w", encoding="utf-8") as f:
            base_gua_name_simplified = daily_gua["base_gua"].rstrip('卦')
            changing_gua_name_simplified = daily_gua["changing_gua"].rstrip('卦')
            f.write(f"{base_gua_name_simplified}\n{changing_gua_name_simplified}\n")
    
    
    elif choice == "2":        
        # 询问用户想要了解的内容
        user_input = input("您想要问什么？")

        # 生成本卦
        base_hexagram = generate_base_hexagram_new()
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
        changing_line, changing_line_index = generate_changing_line_new(base_hexagram)
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
        
        with open("shared_gua_names.txt", "w", encoding="utf-8") as f:
            base_gua_name_simplified = base_gua_name.rstrip('卦')
            changing_gua_name_simplified = changing_gua_name.rstrip('卦')
            f.write(f"{base_gua_name_simplified}\n{changing_gua_name_simplified}\n")
    else:
        print("未生成卦名")
        
     

if __name__ == '__main__':
    main()
