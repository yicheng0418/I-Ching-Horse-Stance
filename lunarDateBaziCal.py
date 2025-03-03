import datetime
import math

# 干支纪年、生肖和月份名称
gan = "甲乙丙丁戊己庚辛壬癸"
zhi = "子丑寅卯辰巳午未申酉戌亥"
lunar_months = ["正", "二", "三", "四", "五", "六", "七", "八", "九", "十", "十一", "腊"]
lunar_days = ["初", "十", "廿", "卅"]

# 五行属性对应表
gan_wuxing = {"甲": "木", "乙": "木", "丙": "火", "丁": "火", "戊": "土", "己": "土", "庚": "金", "辛": "金", "壬": "水", "癸": "水"}
zhi_wuxing = {"子": "水", "丑": "土", "寅": "木", "卯": "木", "辰": "土", "巳": "火", "午": "火", "未": "土", "申": "金", "酉": "金", "戌": "土", "亥": "水"}

# 计算天干地支
def get_ganzhi(year):
    base_year = 1900
    year_diff = year - base_year
    gan_index = (year_diff + 6) % 10  # 天干
    zhi_index = (year_diff + 8) % 12  # 地支
    return gan[gan_index] + zhi[zhi_index]

# 计算生肖（根据地支）
def get_zodiac(year):
    zodiac = "鼠牛虎兔龙蛇马羊猴鸡狗猪"
    zhi_index = (year - 4) % 12  # 1900年是鼠年
    return zodiac[zhi_index]

# 计算日柱的干支
def get_day_ganzhi(date):
    C = (date.year - 1) // 100
    y = date.year % 100
    M = date.month
    d = date.day
    i = 0 if M % 2 == 1 else 6  # 奇数月i=0，偶数月i=6

    G = 4 * C + (C // 4) + 5 * y + (y // 4) + (3 * (M + 1) // 5) + d - 3
    Z = 8 * C + (C // 4) + 5 * y + (y // 4) + (3 * (M + 1) // 5) + d + 7 + i

    tian_gan = gan[G % 10]  # 天干
    di_zhi = zhi[Z % 12]  # 地支
    return tian_gan, di_zhi

# 计算时柱的干支
def get_hour_ganzhi(hour, day_gan):
    # 时柱对应的时支
    time_stems = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
    time_gans = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]

    # 判断时支
    if 23 <= hour < 1:
        time_stem = time_stems[0]
    elif 1 <= hour < 3:
        time_stem = time_stems[1]
    elif 3 <= hour < 5:
        time_stem = time_stems[2]
    elif 5 <= hour < 7:
        time_stem = time_stems[3]
    elif 7 <= hour < 9:
        time_stem = time_stems[4]
    elif 9 <= hour < 11:
        time_stem = time_stems[5]
    elif 11 <= hour < 13:
        time_stem = time_stems[6]
    elif 13 <= hour < 15:
        time_stem = time_stems[7]
    elif 15 <= hour < 17:
        time_stem = time_stems[8]
    elif 17 <= hour < 19:
        time_stem = time_stems[9]
    elif 19 <= hour < 21:
        time_stem = time_stems[10]
    elif 21 <= hour < 23:
        time_stem = time_stems[11]

    # 天干对应推算方法
    stem_index = (time_gans.index(day_gan) + (hour // 2)) % 10
    return time_gans[stem_index], time_stem

# 获取当前时辰
current_time = datetime.datetime.now()
year, month, day, hour = current_time.year, current_time.month, current_time.day, current_time.hour

# 计算年柱、月柱、日柱、时柱
year_ganzhi = get_ganzhi(year)
month_ganzhi = get_ganzhi(year)[0] + zhi[(month + 1) % 12]  # 月柱是根据年柱推算的
day_ganzhi = get_day_ganzhi(current_time)
hour_ganzhi = get_hour_ganzhi(hour, day_ganzhi[0])

print(f"生辰八字：")
print(f"年柱：{year_ganzhi}")
print(f"月柱：{month_ganzhi}")
print(f"日柱：{day_ganzhi[0]}{day_ganzhi[1]}")
print(f"时柱：{hour_ganzhi[0]}{hour_ganzhi[1]}")
