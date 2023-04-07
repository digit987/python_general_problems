import csv, math, matplotlib.pyplot as plt

with open("student.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    row_count = 0
    name = []
    marks = []
    for row in csv_reader:
        if row_count > 0:
            name.append(row[0])
            marks.append(int(row[1]))
        row_count += 1

num_of_obv = len(marks)

mean = sum(marks)/num_of_obv

variance_numerator = 0

for i in marks:
    variance_numerator += math.pow(i-mean, 2)

variance = variance_numerator/num_of_obv

std_dev = math.pow(variance, 0.5)

print("Mean is:", mean)
print("Variance is:", variance)
print("Standard Deviation is:", std_dev) 

var_plot = [variance for _ in range(len(marks))]
std_dev_plot = [std_dev for _ in range(len(marks))]
plt.plot(name, marks)
plt.xlabel("Name")
plt.ylabel("Marks")
#plt.show()
plt.plot(variance, label="Variance")
#plt.show()
plt.plot(std_dev_plot, label="Standard Deviation")
plt.show()
