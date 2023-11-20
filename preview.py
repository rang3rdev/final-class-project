
# Final Class Project 
# Author: Gavin Schnowske 

import csv
import matplotlib.pyplot as p
import numpy as n

gavin = 'gavin.txt'
bryan = 'bryan.txt'
adam = 'adam.txt'
mujeeb = 'mujeeb.txt'
tyler = 'tyler.txt'
arnold = 'arnold.txt'

x1 = []
y1 = []

x2 = []
y2 = []

x3 = []
y3 = []

x4 = []
y4 = []

x5 = []
y5 = []

x6 = []
y6 = []

with open(gavin, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        x1.append(float(row[0]))  
        y1.append(float(row[1]))  

with open(bryan, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        x2.append(float(row[0]))  
        y2.append(float(row[1]))  

with open(adam, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        x3.append(float(row[0]))  
        y3.append(float(row[1]))  

with open(mujeeb, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        x4.append(float(row[0]))  
        y4.append(float(row[1])) 

with open(tyler, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        x5.append(float(row[0]))  
        y5.append(float(row[1])) 

with open(arnold, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        x6.append(float(row[0]))  
        y6.append(float(row[1])) 

p.plot(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, marker = 'o')
p.title('Fantasy Football Scoring: Weeks 1-10')
p.xlabel('Total Points Scored')
p.ylabel('Points Scored by Week')
p.legend()
p.show()