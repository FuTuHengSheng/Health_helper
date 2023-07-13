def check_bmi(bmi, gender):
    ideal_bmi = 22 if gender == 'male' else 19
    result = ""
    if bmi < 18.5:
        result = "BMI值过低,建议适当增加饮食和运动。"
    elif bmi < 25:
        result = "BMI值正常,继续保持良好的生活习惯。"
    elif bmi < 30:
        result = "BMI值偏高,建议适当控制饮食并增加运动量。"
    elif bmi < 35:
        result = "BMI值较高,建议寻求医生的帮助并进行相应的减重治疗。"
    elif bmi < 40:
        result = "BMI值很高,存在较高的健康风险,建议立即寻求医生的帮助。"
    else:
        result = "BMI值过高,属于三类肥胖,存在极高的健康风险,建议立即寻求医生的帮助。"
    if abs(bmi - ideal_bmi) > 8:
        result += "您的BMI值与理想值相差较大,建议咨询医生进行评估。\n"
    
    return result


gender = input("请输入您的性别(male或female):")
print("请注意:BMI值不适用于以下人群:正在做重量训练、怀孕或哺乳中、做过手术、身上有其他材料的患者、身体虚弱或久坐不动的老人。")
bmi = float(input("请输入您的BMI值:"))
result = check_bmi(bmi, gender)
print(result)

##找到的挑衅的建议

#太胖
# 你的肚子已经比你的大脑重了，你需要开始减肥了。
# 你的身体需要锻炼，否则你的脂肪将会像一个世界地图一样。
# 如果你继续这样下去，你的体重将会比你的薪水还要高。
# 你的体重快达到我能够计算的最大值了。
# 你的脂肪比你的肌肉还要多。

#正常
#你简直太完美了，叫你一声健身达人不为过吧。


#太瘦
#您的骨架可能比较轻，如果您不是运动员，建议多吃点好的，增肥一点点也无妨。


