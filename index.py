import CSV
import matplotlib.pyplot as plt

csv = CSV.opencsv("./cars.csv")

weightedParams = []

x = CSV.num(CSV.getCollum(csv, "horsepower"))

y = CSV.num(CSV.getCollum(csv, "price"))


plt.figure()
plt.plot(x, y)
plt.show()