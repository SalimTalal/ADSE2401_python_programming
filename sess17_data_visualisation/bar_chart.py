# Python file to demonstrate visualizing students scores on a line plot

# Import the required modules
import matplotlib.pyplot as plt

names = ["Adam","Richard","William","Emy","Linda"]
scores = [86,90,79,78,96]
plt.bar(names,scores)
plt.xlabel("Student Names")
plt.ylabel("Student Scores")
plt.title("Test Scores by Student")
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
#plt.plot(x_pt,y_pt,'o:r',marker='x',linestyle='-',color='red')
plt.show()