
import matplotlib.pyplot as plt
import csv
x=[]
y=[]
with open('pgm1.csv','r')as csvfile:
    lines=csv.reader(csvfile,delimiter=',')
    for row in lines:
        x.append(row[0])
        y.append(string(row[1]))
    print(x,y)
plt.plot(x,y,color='blue',linestyle='-',marker='*',ms=7,mfc='red',label='CLOSING PRICE')
plt.xticks(rotation=45,fontsize=8)
plt.xlabel('DATES')
plt.ylabel('CLOSING PRICE')
plt.title('STOCK MARKET TREND ANALYSIS',fontsize=16)
plt.grid()
plt.legend()
plt.tight_layout()
plt.show()