#直接根据两个压判断
def check_blood_pressure(systolic, diastolic):
    if systolic > 130 and diastolic > 90:
        return "高血压"
    elif systolic < 90 and diastolic < 60:
        return "低血压"
    else:
        return "正常血压"

# 测试高血压情况
print(check_blood_pressure(140, 95))  # 预期输出: 高血压

# 测试低血压情况
print(check_blood_pressure(80, 50))  # 预期输出: 低血压

# 测试正常血压情况
print(check_blood_pressure(120, 80))  # 预期输出: 正常血压


#根据血压指数判断
def check_blood_pressure(systolic, diastolic):
    result = ""
    blood_pressure_index = (systolic - diastolic) / diastolic
    if blood_pressure_index > 0.5:
        result += "您的血压指数较高，需要注意血压管理。\n"
    elif blood_pressure_index < 0.2:
        result += "您的血压指数较低，需要关注是否存在低血压的症状。\n"
    else:
        result += "您的血压指数正常。\n"
    
    return result

systolic = float(input("请输入您的收缩压(mmHg):"))
diastolic = float(input("请输入您的舒张压(mmHg):"))
result  = check_blood_pressure(systolic, diastolic)
print( result )


#高
#main:减轻并控制体重
#①减轻并控制体重。②减少钠盐摄入。③补充钙和钾盐。④减少脂肪摄入。⑤增加运动。⑥戒烟、限制饮酒。⑦减轻精神压力，保持心理平衡

#低
#main:"XXX这边建议您"每日清晨可饮些淡盐开水

# 1．病因治疗
# 对体质虚弱者要加强营养；对患有肺结核等消耗性疾病者要加紧治疗；因药物引起者可停用或调整用药剂量。如高血压患者服降压药后血压下降过快而感到不适时，应在医生指导下调整给药方法和剂量；对体位性低血压患者，由卧位站立时注意不要过猛，或以手扶物，以防因低血压引起摔跤等。
# 2．适当加强锻炼
# 生活要有规律，防止过度疲劳，因为极度疲劳会使血压降得更低。要保持良好的精神状态，适当加强锻炼，提高身体素质，改善神经、血管的调节功能，加速血液循环，减少直立性低血压的发作，老年人锻炼应根据环境条件和自己的身体情况选择运动项目，如太极拳、散步、健身操等。
# 3．调整饮食
# 每餐不宜吃得过饱，因为太饱会使回流心脏的血液相对减少；低血压的老人每日清晨可饮些淡盐开水，或吃稍咸的饮食以增加饮水量，较多的水分进入血液可增加血容量，从而可提高血压。