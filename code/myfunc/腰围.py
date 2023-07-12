#根据腰围和臀围计算腰臀比，并判断身体肥胖程度是否超标。
def check_waist_hip_ratio(waist, hip, gender):
    ratio = waist / hip
    if gender == "male":
        if ratio > 0.9:
            return "您的腰臀比超标了，可能存在腹部脂肪堆积，建议注意饮食和加强锻炼。"
        else:
            return "您的腰臀比正常，继续保持健康的生活方式。"
    else:
        if ratio > 0.85:
            return "您的腰臀比超标了，可能存在腹部脂肪堆积，建议注意饮食和加强锻炼。"
        else:
            return "您的腰臀比正常，继续保持健康的生活方式。"


waist = float(input("请输入您的腰围（单位：厘米）："))
hip = float(input("请输入您的臀围（单位：厘米）："))
gender = input("请输入您的性别(male或female):")
result = check_waist_hip_ratio(waist, hip, gender)
print(result)

# 建议
# 你的腰围比你的IQ还要高。
# 你的肚子比我大