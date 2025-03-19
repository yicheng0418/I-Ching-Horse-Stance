import datetime
from lunardate import LunarDate
import math

# 天干地支表
gan = "甲乙丙丁戊己庚辛壬癸"
zhi = "子丑寅卯辰巳午未申酉戌亥"
lunar_months = ["正", "二", "三", "四", "五", "六", "七", "八", "九", "十", "十一", "腊"]
lunar_days = ["初", "十", "廿", "卅"]

# 日上起时表（根据日干和时支，直接查表）
hour_table = {
    "甲己": ["甲子", "乙丑", "丙寅", "丁卯", "戊辰", "己巳", "庚午", "辛未", "壬申", "甲酉", "丙戌", "戊亥"],
    "乙庚": ["丙子", "丁丑", "戊寅", "庚卯", "壬辰", "甲巳", "丙午", "戊未", "庚申", "壬酉", "甲戌", "丙亥"],
    "丙辛": ["戊子", "己丑", "庚寅", "壬卯", "甲辰", "丙巳", "戊午", "庚未", "壬申", "甲酉", "丙戌", "戊亥"],
    "丁壬": ["庚子", "壬丑", "甲寅", "丙卯", "戊辰", "庚巳", "壬午", "甲未", "丙申", "戊酉", "庚戌", "壬亥"],
    "戊癸": ["壬子", "甲丑", "丙寅", "戊卯", "庚辰", "壬巳", "甲午", "丙未", "戊申", "庚酉", "壬戌", "甲亥"]
}

# 基准时间：2000年1月1日，已知的日柱为戊午
base_date = datetime.datetime(2025, 1, 1)
base_day_gan = "庚"
base_day_zhi = "午"

# 计算天干地支（年柱）
def get_ganzhi(year):
    base_year = 1900  # 基准年为1900年，庚子年
    year_diff = year - base_year
    
    # 1900年为庚子年，所以天干和地支的偏移应该是庚子（庚为7，子为0）
    gan_index = (year_diff + 6) % 10  # 计算天干位置，+6是因为庚子年从庚开始
    zhi_index = (year_diff) % 12  # 计算地支位置，+0是因为庚子年从子开始
    
    return gan[gan_index] + zhi[zhi_index]

# 计算生肖（根据地支）
def get_zodiac(year):
    zodiac = "鼠牛虎兔龙蛇马羊猴鸡狗猪"
    zhi_index = (year - 4) % 12  # 1900年是鼠年
    return zodiac[zhi_index]

# 计算月柱（根据年柱和农历月份）
def get_month_ganzhi(year_ganzhi, lunar_month):
    year_stem = year_ganzhi[0]
    stem_index = gan.index(year_stem)
    
    # 月支：正月=寅(2), 二月=卯(3)...腊月=丑(1)
    month_zhi_index = (lunar_month + 1) % 12  # 农历1月→索引2
    month_zhi = zhi[month_zhi_index]
    
    # 月干：使用传统推算法
    if stem_index in [0, 5]:  # 甲己年
        month_gan_index = (2 + lunar_month - 1) % 10
    elif stem_index in [1, 6]:  # 乙庚年
        month_gan_index = (4 + lunar_month - 1) % 10
    elif stem_index in [2, 3]:  # 丙丁年
        month_gan_index = (7 + lunar_month - 1) % 10
    else:  # 辛癸年
        month_gan_index = (0 + lunar_month - 1) % 10
    
    return gan[month_gan_index] + month_zhi
# 
# 使用基准时间（2025年1月1日）进行日柱推算
def get_day_ganzhi(date):
    # 计算从基准时间到目标日期的天数差
    day_count = (date - base_date).days  # 从2025年1月1日到目标日期的天数差
    
    # 基准日柱：戊午
    base_day_gan_index = gan.index(base_day_gan)
    base_day_zhi_index = zhi.index(base_day_zhi)
    
    # 推算目标日期的日干和日支
    day_gan_index = (base_day_gan_index + day_count) % 10  # 天干循环
    day_zhi_index = (base_day_zhi_index + day_count) % 12  # 地支循环
    
    return gan[day_gan_index], zhi[day_zhi_index]

# 计算时柱的干支
def get_hour_ganzhi(hour, day_gan):
    time_stems = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
    time_gans = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]

    # 根据小时确定时支
    if 23 <= hour < 1:
        time_stem = time_stems[0]  # 子时
    elif 1 <= hour < 3:
        time_stem = time_stems[1]  # 丑时
    elif 3 <= hour < 5:
        time_stem = time_stems[2]  # 寅时
    elif 5 <= hour < 7:
        time_stem = time_stems[3]  # 卯时
    elif 7 <= hour < 9:
        time_stem = time_stems[4]  # 辰时
    elif 9 <= hour < 11:
        time_stem = time_stems[5]  # 巳时
    elif 11 <= hour < 13:
        time_stem = time_stems[6]  # 午时
    elif 13 <= hour < 15:
        time_stem = time_stems[7]  # 未时
    elif 15 <= hour < 17:
        time_stem = time_stems[8]  # 申时
    elif 17 <= hour < 19:
        time_stem = time_stems[9]  # 酉时
    elif 19 <= hour < 21:
        time_stem = time_stems[10]  # 戌时
    elif 21 <= hour < 23:
        time_stem = time_stems[11]  # 亥时

    # 使用公式计算时干：日干索引 * 2 + 时支数
    day_gan_index = gan.index(day_gan)  # 获取日干的索引
    time_zhi_index = zhi.index(time_stem)  # 获取时支的索引
    hour_gan_index = (day_gan_index * 2 + time_zhi_index) % 10  # 使用公式计算时干
    hour_gan = gan[hour_gan_index]  # 获取时干
    
    return hour_gan, time_stem

# 计算农历的节气和闰月（示例公式，简化版）
def get_lunar_info(year, month):
    # 这里简单假设通过某些已知规则来计算节气等信息
    # 例如，使用公式来计算朔望月和节气等
    m = month - 1  # 农历月从1开始
    M = 1.6 + 29.5306 * m + 0.4 * math.sin(1 - 0.45058 * m)
    # 节气计算公式
    F = 365.242 * year + 6.18799 + 15.22567 * m - 1.9 * math.sin(0.2618 * m)
    # 可以根据实际的计算规则确定是否有闰月
    # 返回农历的节气和是否闰月的信息
    return M, F

# 获取当前时辰并转换为农历
current_time = datetime.datetime.now()
year, month, day, hour = current_time.year, current_time.month, current_time.day, current_time.hour

# 将阳历日期转换为农历日期
lunar_date = LunarDate.fromSolarDate(year, month, day)
lunar_month = lunar_date.month

# 获取农历信息（简化的节气和闰月计算）
M, F = get_lunar_info(year, lunar_month)

# 计算年柱、月柱、日柱、时柱
year_ganzhi = get_ganzhi(year)
month_ganzhi = get_month_ganzhi(year_ganzhi, lunar_month)  # 月柱是根据年柱推算的
day_ganzhi = get_day_ganzhi(current_time)
hour_ganzhi = get_hour_ganzhi(hour, day_ganzhi[0])

# 输出结果
print(f"生辰八字：")
print(f"年柱：{year_ganzhi}")
print(f"月柱：{month_ganzhi}")
print(f"日柱：{day_ganzhi[0]}{day_ganzhi[1]}")
print(f"时柱：{hour_ganzhi[0]}{hour_ganzhi[1]}")
