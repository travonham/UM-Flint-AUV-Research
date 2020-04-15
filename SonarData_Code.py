import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import numpy

sonar = pd.read_csv("Sonar_Detection.csv")
sonar.dropna(how='all', inplace=True)

sonar = sonar.plot(kind='scatter', x='Species', fontsize=9, y='Count', marker = '+', color='Blue')

median = [42,38,30,36,37,25,27,22,14]


plt.title("Group of Fish to Utilize Sonar Detection On", fontsize=13, color='Black')
plt.xticks(rotation=21)


sonar.spines['right'].set_color('Blue')
sonar.spines['left'].set_color('Blue')
sonar.spines['top'].set_color('Blue')
sonar.spines['bottom'].set_color('Blue')

median = numpy.std(median)


#print('Standard Deviation - ', median)
#print(sonar)

plt.show()



