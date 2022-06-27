#Price Pridication Using Linear Regression
#Author: Vaibhav Nalawade
#GitHUb: https://github.com/vaibhavnalawade7/
#Instagram: https://www.instagram.com/vaibhavnalawade7/

from pyexpat import model
import pandas
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = pandas.read_csv('Price.csv')
 
print("\nWelcome To Predict US Dollar In Indian Rupees\n\n")
model = LinearRegression()
model.fit(data[['year']], data[['price']])

p_year = int(input("Enter Year To Predict\n"))
print("The Price Will Be In: ", p_year, model.predict([[p_year]]))

plt.scatter(data['year'], data['price'])
plt.show()
# print('''
#     Predict USD To INR Price\n''')


# y = input("Enter Y To Start\n")
# n = 1
# if y == "y" or "Y":
#     while n == 1:
#         data = pandas.read_csv('Price.csv')

#         print("\nWelcome To Predict US Dollar In Indian Rupees\n\n")
#         model = LinearRegression()
#         model.fit(data[['year']], data[['price']])

#         p_year = int(input("Enter Year To Predict\n"))
#         print(model.predict([[p_year]]))

#         plt.scatter(data['year'], data['price'])
#         plt.show()
# else:
#     print("Enter Valid Choice")
