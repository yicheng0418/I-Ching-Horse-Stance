import datetime
from lunarDateBaziCal import get_ganzhi, get_zodiac, get_day_ganzhi, get_hour_ganzhi, gan , zhi

# 计算骨量的方法（根据天干地支来计算骨量）
year_weight_dict = {
    "甲子": 1.2, "乙丑": 0.9, "丙寅": 0.6, "丁卯": 0.7, "戊辰": 1.2, "己巳": 0.5,
    "庚午": 0.9, "辛未": 0.8, "壬申": 0.5, "癸酉": 0.8, "甲戌": 1.5, "乙亥": 0.9,
    "丙子": 1.6, "丁丑": 0.8, "戊寅": 0.8, "己卯": 1.9, "庚辰": 1.2, "辛巳": 0.6,
    "壬午": 0.8, "癸未": 0.7, "甲申": 0.5, "乙酉": 1.5, "丙戌": 0.6, "丁亥": 1.6,
    "戊子": 1.5, "己丑": 0.6, "庚寅": 0.9, "辛卯": 1.2, "壬辰": 0.5, "癸巳": 0.7,
    "甲午": 1.5, "乙未": 0.6, "丙申": 0.5, "丁酉": 1.6, "戊戌": 1.4, "己亥": 0.9,
    "庚子": 0.7, "辛丑": 0.7, "壬寅": 0.9, "癸卯": 1.2, "甲辰": 0.8, "乙巳": 0.7,
    "丙午": 1.3, "丁未": 0.5, "戊申": 1.4, "己酉": 0.5, "庚戌": 0.9, "辛亥": 1.7,
    "壬子": 0.5, "癸丑": 0.7, "甲寅": 1.2, "乙卯": 0.8, "丙辰": 0.8, "丁巳": 0.6,
    "戊午": 0.8, "己未": 1.5, "庚申": 0.8, "辛酉": 0.6, "壬戌": 1.0, "癸亥": 0.6
}

month_weight_dict = {
    1: 0.6, 2: 0.7, 3: 1.8, 4: 0.9, 5: 0.5, 6: 1.6,
    7: 0.9, 8: 1.5, 9: 1.8, 10: 0.8, 11: 0.9, 12: 0.5
}

day_weight_dict = {
    1: 0.5, 2: 1.0, 3: 0.8, 4: 1.5, 5: 1.6, 6: 1.5, 7: 0.8, 8: 1.6, 
    9: 0.8, 10: 1.6, 11: 0.9, 12: 1.7, 13: 0.8, 14: 1.7, 15: 1.0,
    16: 0.8, 17: 0.9, 18: 1.8, 19: 0.5, 20: 1.5, 21: 1.0, 22: 0.9,
    23: 0.8, 24: 0.9, 25: 1.5, 26: 1.8, 27: 0.7, 28: 0.8, 29: 1.6, 30: 0.6
}

time_weight_dict = {
    '子': 1.6, '丑': 0.6, '寅': 0.7, '卯': 1.0, '辰': 0.9, '巳': 1.6,
    '午': 1.0, '未': 0.8, '申': 0.8, '酉': 0.9, '戌': 0.6, '亥': 0.6
}

def convert_to_date(input_str):
    """
    转换输入的日期字符串（阳历/农历）
    :param input_str: 用户输入的日期
    :return: 转换后的日期对象
    """
    # 判断是否为阳历，如果有/g，则为阳历，否则是农历
    if '/g' in input_str:
        date_str = input_str.replace('/g', '').strip()  # 去掉/g
        date_format = "%Y %m %d %H"  # 阳历格式
    else:
        date_str = input_str.strip()  # 假设输入的格式为农历
        date_format = "%Y %m %d %H"  # 处理农历时也可以加入转换逻辑
    
    # 将输入的字符串转换为日期
    try:
        date_obj = datetime.datetime.strptime(date_str, date_format)
        return date_obj
    except ValueError:
        raise ValueError("日期格式不正确，请使用：年年年年 月月 日日 时时")



def calculate_bone_weight(year, month, day, time):
    """
    计算出生日期和时辰的骨量
    :param year: 出生年份
    :param month: 出生月份
    :param day: 出生日
    :param time: 出生时辰
    :return: 总骨量
    """
    # 获取年份的天干地支
    year_ganzhi = get_ganzhi(year)
    print(f"Year Ganzhi for {year}: {year_ganzhi}")  # 打印年柱，查看是否正确
    
    year_stem = year_ganzhi[0]  # 天干
    year_branch = year_ganzhi[1]  # 地支

    # 获取年份对应的骨量
    year_key = year_stem + year_branch
    weight_sum = year_weight_dict.get(year_key, None)

    # 验证是否成功获取年份骨量
    if weight_sum is None:
        print(f"无法计算年份 {year_key} 对应的骨量。")
        return None

    # 获取月份、日期、时辰对应的骨量
    weight_sum += month_weight_dict.get(month, 0)
    weight_sum += day_weight_dict.get(day, 0)
    weight_sum += time_weight_dict.get(time, 0)

    return weight_sum


def third_main():
    """
    主程序，负责接收用户输入并计算骨量
    """
    input_date = input('请输入出生年份-阴历（四位数字），月份（1-12），日期（1-31），时辰（中文字符，如“子”）：')

    # 解析输入日期（阳历或农历）
    try:
        date_obj = convert_to_date(input_date)
        year = date_obj.year
        month = date_obj.month
        day = date_obj.day
        hour = date_obj.hour
    except ValueError as e:
        print(e)
        return

    # 获取年柱、月柱、日柱、时柱
    year_ganzhi = get_ganzhi(year)
    month_ganzhi = get_ganzhi(year)[0] + zhi[(month + 1) % 12]  # 月柱是根据年柱推算的
    day_ganzhi = get_day_ganzhi(date_obj)
    hour_ganzhi = get_hour_ganzhi(hour, day_ganzhi[0])

    print(f"生辰八字：")
    print(f"年柱：{year_ganzhi}")
    print(f"月柱：{month_ganzhi}")
    print(f"日柱：{day_ganzhi[0]}{day_ganzhi[1]}")
    print(f"时柱：{hour_ganzhi[0]}{hour_ganzhi[1]}")

    # 让用户输入时辰
    time = input('请输入出生时辰（中文字符，如“子”）：')

    # 计算骨量
    weight_sum = calculate_bone_weight(year, month, day, time)

    # 验证是否计算成功
    if weight_sum is None:
        print("发生错误，无法计算称骨重量。")
    else:
        print(f"计算得到的骨量为：{weight_sum}两")
        # 根据骨量输出命运解释
        if weight_sum == 2.1:
            print('终身行乞孤苦之命。\n短命非业谓大空，平生灾难事重重，凶祸频临陷逆境，终世困苦事不成。')
        elif weight_sum == 2.2:
            print('一生劳碌之命。\n此命劳碌一生穷，每逢困难事重重，凶祸频临陷苦境，终身大事谋不成。\n身寒骨冷苦伶仃，此命推来行乞人，劳劳碌碌无度日，终年打拱过平生。')
        elif weight_sum == 2.3:
            print('终身困苦之命。\n此命推来骨肉轻，求谋做事事难成，妻儿兄弟实难靠，外出他乡做散人。')
        elif weight_sum == 2.4:
            print('一生薄福之命。\n此命推来福禄无，门庭困苦总难荣，六亲骨肉皆无靠，流浪他乡作老翁。')
        elif weight_sum == 2.5:
            print('六亲无靠，自力更生之命。\n此命推来祖业微，门庭营度似稀奇，六亲骨肉如冰炭，一世勤劳自把持。')
        elif weight_sum == 2.6:
            print('平生衣禄苦中求，独自营谋事不休，离祖出门宜早计，晚来衣禄自无休。\n此命为人刚强，劳心劳力，移祖居住，有能自力得安然，知轻识重，坏事不做，老来贪心口无毒，但一 生不足，子息难靠。初限之中小发达，早年家计得安康，四十七八岁，交来末运渐渐谋事而成，事业而就，财源 茂盛，老来荣华。妻宫有克，两妻无刑，子息四个只一子送终，寿元七十九，过此七十九岁，死于十二月中。')
        elif weight_sum == 2.7:
            print('一生多谋少成之命。\n一生作事少商量，难靠祖宗作主张，独马单枪空做去，早年晚岁总无长。\n此命为人性纯不刚不柔，心中无毒，做事有始有终，池塘鸳鸯寻食吃，易聚易散，骨肉六亲不得力，财 物风云，操心劳力，极早恨奋寒窗，原来破尽，重新白手起家，且过三十五六，方可成家立业，四十外行船顺 风，五十安稳，末限滔滔事业兴，妻宫硬配，子女送终，寿元七十，死于五月中。')
        elif weight_sum == 2.8:
            print('一生行事似飘蓬，祖宗产业在梦中，若不过房改名姓，也当移徒二三通。\n此命为人多才能，心机灵巧，祖业飘零，离乡别井可成事业，兄弟多力，驳杂多端，为静处安然，出外 有人敬重，可进四方之财，有贵人扶持，逢凶化吉，勤俭一生，无大难，只是救人无功，恩中招怨，重义轻才，易聚易散，早年不能聚财，三十三岁方知劳苦，凡事顺意，三十而立，四十岁称心如意，末限福如东海，寿比 南山。只是妻宫有克，三子送终，寿元六十九，闯过八十一，死于三月中。')
        elif weight_sum == 2.9:
            print('初年运限未曾亨，纵有功名在后成，须过四旬才可立，移居改姓始为良。\n此命为人性爆，心直口快，有才能，见善不欺，逢恶不怕，事有始终，量能宽大，但不能聚财，兄弟六亲无力，自立家计，出外方好，初限二十三四五不遂，二十七八有好运到，犹如枯木逢春，中限四十九之命有险，四十多来古镜重磨，明月再圆。五十六七八末限明月又被云侵，交七十方走大运，妻小配怕刑，克子，寿元七十七，死于春光中。')
        elif weight_sum == 3.0:
            print('劳劳碌碌苦中求，东奔西走何日休，若使终身勤与俭，老来稍可免忧愁。\n此命为人多才多能，心机为巧，祖业凋零，离乡别井可成家业，兄弟少力，驳杂多端，出外有贵人扶持，一生无刑克，无大难，只是救人无功，恩中招怨，重义轻才，易聚易散，早年不能聚财，三十三岁方知劳苦，凡事顺意，三十而立，四十岁称心如意，三子送终，寿元六十九，死于三月中。')
        elif weight_sum == 3.1:
            print('忙忙碌碌苦中求，何日云开见日头，难得祖基家可立，中年衣食渐无忧。\n交友谨慎，老年衣食足用之命。\n此命推来敬重双亲，有福有禄，六亲和睦，义气高强，少年勤学有功名，忠孝双全，心中无毒，不贵则福，出外受人钦佩，四海闻名，老来荣华，限上无忧，一生安康，年轻欠利，末限安享福禄，白鹤先生云：此命三限，有子孙旺相局，初限早成家计，辛勤劳苦，中限渐渐生财重奔江山，夫妻少配无刑，末限荣华富贵，寿元八十三岁，死于冬月之中。')
        elif weight_sum == 3.2:
            print('初年运蹇事难谋，渐有财源如水流，到得中年衣食旺，那时名利一齐收。\n中限交来渐渐称心，求谋顺利，出外有人恭敬，一生受贵，若要问其消息，事业兴，家业旺，其年运到滔滔财源至，滚滚利丰盈，春光花自发，微风细雨生，四十六七八交末运，移花接子桂花香，夫妻偕老，寿元八十之外，子孙福禄荣昌，死于腊月中。')
        elif weight_sum == 3.3:
            print('性直多情，交友带劫之命，\n早年作事事难成，百计徒劳枉费心，半世自如流水去，后来运到得黄金。\n此命生人性巧心灵，弄假成真，口快无心，恩中招怨，君子敬佩，小人气恨，骨肉无援，志在四方，身心健康，前运乘阴少种树，中限轻财，大运交来，声名可望，万事更新，名利振建，此后小事宜注意，才有子息，寿元八十三，死于三月中。')
        elif weight_sum == 3.4:
            print('此命福气果如何，僧道门中衣禄多，离祖出家方为妙，朝晚拜佛念弥陀。\n此命推来为人性躁，与人做事反为不美，离祖成家，三翻四次自成自立安享福，直自三十六至四十六，财不谋而自至，福不求而自得，有贵人助，家庭安宁，妻宫若要无刑，猴、猪、羊、蛇不可配，龙、虎、马、牛方得安，虽有二子，终生带暗方可。兄弟六亲如冰碳，在家不得安然，初限驳杂多端，劳碌奔波不能聚钱，常有忧愁，寿元七十八岁，死于三月中。')
        elif weight_sum == 3.5:
            print('生平福量不周全，祖业根基觉少传，营事生涯宜守旧，时来衣食胜从前。\n此命为人品性纯和，做事忠直，志气高傲，与人做事恩中招怨，六亲兄弟不得力，祖业全无，早年驳杂多端，独马单枪，初限命运甚来，二十而立三十来岁末曾交运都说好，三十五六到四十犹如金秋菊迎秋放，心机用尽方逢春，末限交来始称怀，祖业有破后重兴，犹如枯木逢春再开花，妻宫忧虚无刑，寿元五十七，限至六十九，三子送终，寿元八十一，死于十月中。')
        elif weight_sum == 3.6:
            print('少年多波折，老来安逸之命。\n不须劳碌过平生，独自成家福不轻，早有福星常照命，任君行去百般成。\n此命为人灵机性巧，胸襟通达，志气高，少年勤学有功名之格，青年欠利，腹中多谋，有礼有义，有才能，做事勤俭，一生福禄无缺，与人干事，反为不美，六亲骨肉可靠，交朋友，四海春风，中限光耀门庭，见善不欺，逢恶不怕，事有始终，量能宽大，义利分明，吉人天相，四海闻名，末限成家立业，安然到老，高楼大厦，妻宫无刑，子息三人，只一子送终，寿元七十七，卒于春光中。')
        elif weight_sum == 3.7:
            print('此命般般事不成，弟兄少力自孤行。虽然祖业须微有，来得明时去不明。\n一生财来复去，难得大富之命。\n此命为人品性刚直，做事公开有才能，不肯休息，六亲兄弟不得力，祖业无靠，白手成家立业，末运多驳杂，不能聚财，不欺负人，有义气，心神不定，易成喜怒，初限奔波劳苦，离别他境可成家计，改换门庭，中限未得如意，末限环环妻宫，方可刑克，子息虽有不得力，只好真假送终，寿元七十七，死于七月中。')
        elif weight_sum == 3.8:
            print('一身骨肉最清高，早入簧门姓氏标。待到年将三十六，蓝衫脱去换红袍。\n此命为人品性刚直，做事公开有才能，不肯休息，六亲兄弟不得力，祖业无靠，白手成家立业，末运多驳杂，不能聚财，好一双抓钱手，没有一个赚钱斗，此命蜘蛛结网，朝圆夜不圆，做几番败几番，只能稳步成家计，谁知又被狂风吹，初限二十三四，犹如明月被云侵，三十外来恰是日头又重开，终交末运方为贵，渐渐荣昌盛。')
        elif weight_sum == 3.9:
            print('少年命运不通，老享清福之命。\n此命终身运不通，劳劳作事尽皆空，苦心竭力成家计，到得那时在梦中。\n此命为人品性刚直，做事公开有才能，有机变不肯休息，六亲兄弟不得力，祖业无靠，白手成家立业，末运多驳杂，不能聚财，好一双抓钱手，没有一个赚钱斗，此命蜘蛛结网，朝圆夜不圆，做几番败几番，只能稳步成家计，谁知又被狂风吹，初限二十三四，犹如明月被云侵，三十外来恰是日头又重开，二子送终，寿元五十七岁，过此八十八，死于秋天中。')
        elif weight_sum == 4.0:
            print('平生衣禄是绵长，件件心中自主张。前面风霜多受过，后来必定享安康。\n此命为人性躁，心直口快，有才能，逢善不欺，逢恶不怕，事有始终，量能宽大，不能聚财，祖业破败，兄弟六亲不得力，自立家计出外方好，初限二十五六连年不遂，二十七岁有好运，犹如枯木逢春，中限四十九岁有灾，铁镜重磨，明月正圆，五十六七交大运，寿元七十七，卒于春光中。')
        elif weight_sum == 4.1:
            print('聪明超群，老来逍遥享福之命。\n此命推来事不同，为人能干异凡庸，中年还有逍遥福，不比前时运未通。\n此命性重气高，有口无心，祖业未交，离别他境，事事可成，六亲骨肉不得力，自成家计，学习经营，四方闻名，当把外方之时，丰隆初限奔波驳杂，不能聚财，交过三十八九方可成家，四十五六方能顺意，末限犹如三月杨柳，枝枝生细叶，晚景处处红，妻宫无克破，子息假送老，寿元四十七，闯过可到六十六，卒于九月中。')
        elif weight_sum == 4.2:
            print('自力更生，老运名利双收之命。\n得宽怀处且宽怀，何用双眉皱不开，若使中年命运济，那时名利一齐来。\n此命为人操劳，自成自立，与人出力事不成，离祖之命，成家三番四次，用尽心机不得开怀，若要安乐享福，要到三十六到四十六时不谋自待，福不求自至，有贵人助力，家庭安然，妻宫若要无刑，猴、猪、羊、蛇不可配，龙、虎、马、牛方得安，兄弟六亲如冰碳，在家不得安然，初限驳杂多端，不能聚钱，常有忧愁，寿元七十八岁，死于三月中。')
        elif weight_sum == 4.3:
            print('福禄厚重，白手成家之命。\n为人心性最聪明，作事轩昂近贵人，衣禄一生天数定，不须劳碌过平生。\n此命为人性躁刚强，平生不受亏，多技多能，祖业冰碳，能聚财，交过三十开外，方得开怀，中限之命能进四方之财，出外逢贵人之力，艺术精，善经营，方能兴旺，上业迟，有一疾相侵，直至末限方得享福，妻宫匹配，龙虎马牛可配，二子送终，寿元八十，卒于四月之中。')
        elif weight_sum == 4.4:
            print('初年无财，老年自得享福之命。\n万事由天莫苦求，须知福禄命里收，少壮名利难如意，晚景欣然更不忧。\n此命为人忠直敬重，心慈性躁，深谋远虑，心中多劳，贵人钦敬，六亲冰碳，初限行运，美中不足，中限渐入佳境，名利可佳，刚柔有济，二十九交佳运，可通花甲，天赐麒麟送老，寿元八十五岁，卒于冬月之中。')
        elif weight_sum == 4.5:
            print('少年辛苦，老来福禄双全之命。\n名利推来竟若何，前番辛苦后奔波。命中难养男与女，骨肉扶持也不多。\n此命为人品性不刚不柔，心中无毒，自当自担，离祖之命，做事有始有终，池塘鸳鸯觅食，或聚或散，骨肉六亲不得力，如嗥如风，劳心费力多成败，初限运寒多驳杂，祖业破败，重新白手成家，至三十五六方能成家立业，四十开外，如船遇顺风，五十多岁安稳，末限滔滔事业兴，妻宫硬配，子息伴架送终，寿元七十五岁，卒于五月之中。')
        elif weight_sum == 4.6:
            print('改姓移居，自得福寿双全之命。\n东西南北尽皆通，出姓移居更觉隆，衣禄无亏天数定，中年晚景一般同。\n此命为人心慈性躁，有口无心，有粗有细，一生奔波，六亲无靠，无大难，妻宫无刑，祖业凋零，自立家计，早业如同败落萍，劳心用下一半生，交三十五六七八岁，又平平度过几春秋，六十前后花开日，花开又招雨来淋，必定小人加暗害，平日之中要小心，早子招维，只一子送终，寿元七十三，卒于冬月之中')
        elif weight_sum == 4.7:
            print('早年多波折，晚年享福之命。\n此命推为旺末年，妻荣子贵自怡然，平生原有滔滔福，财源滚滚似水流。\n此命为人品性纯和，做事公道，忠心待人气质高，与人干事恩仇报，兄弟不力祖业微，早年驳杂多端，时来骨肉精，财源是归命，匹马单枪，初限运来二十至三十岁，末限交运都好，反到交时苦衰，三十六至四十来岁，犹如金秋菊遇秋开放，心机用尽方为贵，末运交来怡称怀，祖业有破，家业重注，好似枯木逢春再开花，孤子送老，五十九岁有一限到六十九岁，寿元八十二卒于冬月之中。')
        elif weight_sum == 4.8:
            print('初年大志难伸，晚年发展之命。\n初年运道未曾亨，若是蹉跎再不兴，兄弟六亲皆无靠，一身事业晚年成。\n此命为人性躁，能随机应变，常近贵人，祖业无成，骨肉六亲少义，一个自立家计，初限交来财运如霜雪，中限略可成家，大运突来能立家业，妻有克，小配无刑，子息三人，寿元七十七岁，卒于七月之中。')
        elif weight_sum == 4.9:
            print('交友多情有损，小心防之再发之命。\n此命推来福不轻，自成自立显门庭，从来富贵人钦敬，使婢差奴过一生。\n此命为人品性纯和，做事勤俭，恩中招怨，兄弟有克，亲朋相援，赔酒赔饭，反说不美，初限贫愁，交过二十六七岁，如逆水行舟，不能聚财，中限驳杂多端，刑妻克子，交过四十岁，方可成家立业，般般遂意，件件称心，至四十七八岁有一灾，宁可损财交过，后有十年好运来，家中钱财聚，三子送老，寿元七十三岁，卒于九月之中。')
        elif weight_sum == 5.0:
            print('衣食无亏，一生富贵之命。\n为利为名终日劳，中年福禄也多遭，老来是有财星照，不比前番目下高。\n此命为人正直，伶俐灵巧，有机变，平生无大难，祖业无靠，自成自立，白手成家，亲朋冷落，兄弟少力，可得四方之财，好一双挣钱手，没有一个聚钱斗，满面春风人道好，一生不足自爱知，妻迟子晚，初限奔波，中限四十岁方交大运，犹如枯木逢春，四十九岁有一灾，其年福星高照，有十年大运，财禄丰盈大吉昌，妻宫铁硬同偕老，子息一双可送终，寿元六十九岁，卒于冬月之中。')
        elif weight_sum == 5.1:
            print('勤俭成家，老年自得福禄之命。\n一世荣华事事通，不须劳碌自亨通，弟兄叔侄皆如意，家业成时福禄宏。\n此命为人做事有能力，且能随机应变，性燥能知其轻重，交朋结友如兄弟，气量宽宏，见善不欺，逢恶不怕，平生正直，无大难刑险，只是少招祖业，初限衣禄无亏，子息晚招可实得，四十至五十，末限通达昌吉，福禄无亏，财源稳定，丰衣足食，高堂大厦，妻宫友好，二子两女送终，寿元八十岁，卒于九月中。')
        elif weight_sum == 5.2:
            print('聪明能干，老来财禄丰足之命。\n一世荣华事事能，不须劳思自然宁，宗族欣然心皆好，家业丰亨自称心。\n此命为人多才多能，心机灵变，祖业飘零，离乡可成家计，兄弟少力，驳杂多端，为人只是救人无功，重义轻财，财禄易聚易散，早年聚财凡事顺意，三十至四十岁如意称心，末限福如东海，寿比南山，只是妻克两硬无刑，有三子二女送终，寿元八十三，卒于冬月之中。')
        elif weight_sum == 5.3:
            print('自己兴家立业之命。\n此格推为气量真，兴家发达在其中，一生福禄安排定，却是人间一富翁。\n此命推来敬重双亲，有福有禄，气质高昂，少年勤学功名不就，忠孝两全，心善无毒，非富则贵，出外有人钦佩，四海名扬，到老荣华，限上无忧，一世健康，青年欠利，末限安享福禄，白鹤先生云：此骨三限之骨，子孙王相之局，初限早成家计，辛勤劳苦，中限渐渐生财，重整门庭，末限荣华富贵，妻宫小配无刑，有三子二女送终，寿元八十二，卒于冬月之中。')
        elif weight_sum == 5.4:
            print('一生清闲之命。\n此命推来厚且清，诗书满腹看功成，丰衣足食自然稳，正是人间有福人。\n此命为人灵巧，胸襟通达，志气高强，少年勤学有功名，年轻欠利，腹中多谋，有礼有义，有才有能，做事勤俭，一生福禄无亏，与人干事反为不美，亲朋戚友，四海春风。中限光辉门庭，逢善不欺，逢恶不怕，事有始终，吉人天相，四海扬名，成家立业，安然到老，高楼大厦，妻宫硬无刑，子息三人，只一子送终，寿元七十七，卒于春光中。')
        elif weight_sum == 5.5:
            print('少年奋斗，晚年富贵之命。\n走马扬鞭争利名，少年作事费筹论，一朝福禄源源至，富贵荣华显六亲。\n此命为人灵巧机巧，初限尚不聚财，只是虚名虚利，财来财去，一生勤于学，自有功名，有衣禄，福星照命，中限交来可称心，求谋如意，出外有人恭敬，一生受贵，要问其他消息，事后兴家发达，壮年滔滔财源旺，滚滚利顺来，迎春花正发，微风细雨生，四十九交来末运，移花接木桂花香，夫妻百年同偕老，寿元八十之外，福禄荣昌，卒于春光之中。')
        elif weight_sum == 5.6:
            print('仁义之人，老来富贵之命。\n此格推来礼义通，一身福禄用无穷，甜酸苦辣皆尝过，滚滚财源稳且丰。\n此命为人性巧心灵，有口无心，事不保密，少年劳碌难免，志在四方，身心健康，前运乘阴少种树，怀才不遇，中限轻财，大举随行，移动得安然终日成，名声可望，旧业换新，名利享通，五人盆石皆白发，倾自心田此后昆，此命小事宜放松，方有子息，寿元八十二岁，卒于冬月之中。')
        elif weight_sum == 5.7:
            print('人人钦敬，离祖成家之命。\n福禄丰盈万事全，一身荣耀乐天年。名扬威震人争羡，此世逍遥宛似仙。\n此命为人心灵性巧，做事细致，足智多谋，志气高昂，少年勤学，名利成就，逍遥快乐，气量宽宏，财禄有余，犹如锦上添花，中限以来，自成自立，渐渐荣昌，招人进财，妻子晚配为美，四十至四十五六岁，看子成名，末限多得意，家中财产甚丰隆，妻宫无克，二子送终，寿元七十三岁，卒于正月中。')
        elif weight_sum == 5.8:
            print('独创名利，晚年享福之命。\n平生福禄自然来，名利兼全福寿偕，雁塔题名为贵客，紫袍金带走金阶。\n此命为人忠直，做事有头有尾，身清气高，六亲有旺，兄弟少帮，妻宫并重，子息二三，他乡创业，官臣之命，只是与人干事，恩中招怨，反为不美，早限财来财去，中限兴旺，一子送终，寿元八十三岁，卒于四月之中。')
        elif weight_sum == 5.9:
            print('宜安分守己，福禄自足之命。\n细推此格妙且清，必定才高礼义通，甲第之中应有分，扬鞭走马显威荣。\n此命为人性情暴躁，刚强，平生不受亏，所谓量大多智多能，受人尊敬，祖业凋零，兄弟只可画饼充饥，亲戚则是望梅止渴，劳心见早，发福见迟，独立成家，只是早聚财，逢凶化吉，驳杂交过二十开外，方得顺利开怀，中限之命可进四方之财，出外有贵人助力，可精手艺营业，方能兴家立业，此间或有小疾相侵，再交限方得安然，坐享福禄，妻宫之配龙虎马牛，一子送老，寿元八十岁，卒于六月之中。')
        elif weight_sum == 6.0:
            print('鹤立鸡群，显祖扬宗之命。\n一朝金榜快题名，显祖荣宗立大功，衣禄定然原裕足，田园财帛更丰盈。\n此命为人灵机性巧，胸襟发达，志气高强，少年勤学，有功名之格，青年欠利，腹中多谋，有礼有仪，有才能，做事勤俭，一生福禄无亏，与人做事，有力无功，兄弟骨肉中多谋，交朋友，四海名扬，中限光辉门户，早能发达，义利分明，末限成家立业安然到老，高楼大厦，妻宫两硬无刑，子息三人，只有一人送终，寿元七十七岁，卒于春光之中。')
        elif weight_sum == 6.1:
            print('名利双收，一生富贵之命。\n不作朝中金榜客，定为世上大财翁，聪明天赋经书熟，名显高科自是荣。\n此命为人心秉直，聪明利达，心善口快，有才能。见善不欺，逢恶不怕，刚柔有济，事有始终，早能宽大，而能聚财，祖业如旧，六亲兄弟有靠，自立家计出外更好，二十至二十五六七八岁有险，三十开外古镜重磨，明月再圆，六十六至七十方交大运妻宫小配，寿元七十七岁，卒于春光之中。')
        elif weight_sum == 6.2:
            print('读书聪明，特任高官，大振家风之命。\n此命生来福不穷，读书必定显亲宗，紫衣金带为卿相，富贵荣华皆可同。\n此命为人忠直敦厚，心无所毒，性巧灵敏，深谋远虑，吉人天相，心中多劳，受人钦叹，美中不足，中限渐入佳境，名利可佳，刚济有情，二十九交来阳春暖，东北佳音，天津四通，花甲一二岁大顺，天赐麒麟送老，寿元八十五岁，卒于冬月之中。')
        elif weight_sum == 6.3:
            print('长寿，高官显耀，上格之命。\n命主为官福禄长，得来富贵实丰常，名题金塔传金榜，定中高科天下扬。\n此命为人聪明利达，近知识，远小人，自觉性强，改悔及时，君子量大，福禄寿三星拱照，富贵名扬天下，荣宗显祖之格，可是美中欠佳，妻宫有硬，操劳心重，先天下之忧而忧，后天下之乐而乐，寿元七十有八，享于荣绵归期，二子二女送终。')
        elif weight_sum == 6.4:
            print('此格威权不可当，紫袍金带尘高堂。荣华富贵谁能及？万古留名姓氏扬。\n权威大官，万古留名之富贵命')
        elif weight_sum == 6.5:
            print('细推此命福非轻，富贵荣华孰与争？定国安邦人极品，威声显赫震寰瀛。')
        elif weight_sum == 6.6:
            print('大富大贵，堆金积玉之福命。\n此格人间一福人，堆金积玉满堂春，从来富贵由天定，正笏垂绅谒圣君。')
        elif weight_sum == 6.7:
            print('一世荣华，享福无边之命。\n此命生来福自宏，田园家业最高隆，平生衣禄盈丰足，一世荣华万事通。')
        elif weight_sum == 6.8:
            print('享受天赐之福，近贵显达之命。\n富贵由天莫苦求，万金家计不须谋，如今不比前翻事，祖业根基飞古留。')
        elif weight_sum == 6.9:
            print('祖业虽多，若不紧守也会落空。\n君是人间衣禄星，一生富贵众人钦，纵然福禄由天定，安享荣华过一生。')
        elif weight_sum == 7.0:
            print('一生清荣，富贵双全之命荣华富贵已天定，正笏垂绅拜紫宸。\n此命推来福禄宏，不须愁虑苦劳心，一生天定衣与禄，富贵荣华主一生。')
        elif weight_sum == 7.1:
            print('此命生成大不同，公侯卿相在其中。一生自有逍遥福，富贵荣华极品隆。')
        elif weight_sum == 7.2:
            print('此格世界罕有生，十代积善产此人。天上紫微来照命，统治万民乐太平。')


# 启动主程序
if __name__ == "__main__":
    third_main()

