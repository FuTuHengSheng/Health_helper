import matplotlib.pyplot as plt

##填入数据
x_data = ["6/7","6/20","6/29","7/12","7/22","7/30","8/1","8/9","9/9","12/12"]
y_data = [9,31.5,32 ,33 , 31,28.9 ,27.5,26.6,27.5,25]

 
plt.rcParams["font.sans-serif"]=['SimHei']
plt.rcParams["axes.unicode_minus"]=False

#*BMI*#
for i in range(len(x_data)):
    if y_data[i]<18.5:
        plt.bar(x_data[i],y_data[i],color='c')
    elif 18.5<=y_data[i]<=25:      
        plt.bar(x_data[i],y_data[i],color='g')
    else:
        plt.bar(x_data[i],y_data[i],color='r')

plt.title("健康分析")
plt.xlabel("时间")
plt.ylabel("BMI指数")

plt.show()


#####血压指数
x_data = ["6/7","6/20","6/29","7/12","7/22","7/30","8/1","8/9","9/9","12/12"]
y_data = [0.1,0.2,0.3,0.4,0.5,0.9,0.4,0.2,0.3,0.1]

 
plt.rcParams["font.sans-serif"]=['SimHei']
plt.rcParams["axes.unicode_minus"]=False

#*血压指数*#
for i in range(len(x_data)):
    if y_data[i]<0.2:
        plt.bar(x_data[i],y_data[i],color='c')
    elif 0.2<=y_data[i]<=0.5:      
        plt.bar(x_data[i],y_data[i],color='g')
    else:
        plt.bar(x_data[i],y_data[i],color='r')

plt.title("健康分析")
plt.xlabel("时间")
plt.ylabel("血压指数")

plt.show()

####血糖

x_data = ["6/7","6/20","6/29","7/12","7/22","7/30","8/1","8/9","9/9","12/12"]
y_data = [3.1,4.2,5.3,6.4,7.5,8.9,5.4,9.2,2.3,1.1]

plt.rcParams["font.sans-serif"]=['SimHei']
plt.rcParams["axes.unicode_minus"]=False

#*血糖*#
for i in range(len(x_data)):
    if y_data[i]<3.9:
        plt.bar(x_data[i],y_data[i],color='c')
    elif 3.9<=y_data[i]<=6.1:      
        plt.bar(x_data[i],y_data[i],color='g')
    else:
        plt.bar(x_data[i],y_data[i],color='r')

plt.title("健康分析")
plt.xlabel("时间")
plt.ylabel("空腹血糖")

plt.show()



