import matplotlib.pyplot as plt

#Histogram
def plot_histogram(data,column, bins=30, color='blue',edgecolor="black"):
    plt.figure(figsize=(10,6))
    plt.hist(data[column],bins=bins, color=color,edgecolor=edgecolor)
    plt.title(f'Distrubtion of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show

#Box Plot
def plot_box(data, column):
    plt.figure(figsize=(10, 6))
    plt.boxplot(data[column])
    plt.title(f'Box Plot of {column}')
    plt.ylabel(column)
    plt.show()

#Bar Plot
def plot_bar(data, column):
    counts = data[column].value_counts()
    plt.figure(figsize=(12, 8))
    counts.plot(kind='bar', color='green')
    plt.title(f'Frequency of {column}')
    plt.xlabel(column)
    plt.ylabel('Count')
    plt.show()
#Scatter Plot
def plot_scatter(data, column_x, column_y, color='red'):
    plt.figure(figsize=(10, 6))
    plt.scatter(data[column_x], data[column_y], color=color)
    plt.title(f'Scatter Plot of {column_x} vs. {column_y}')
    plt.xlabel(column_x)
    plt.ylabel(column_y)
    plt.show()

#Pie Chart
def plot_pie(data, column):
    counts = data[column].value_counts()
    plt.figure(figsize=(10, 10))
    counts.plot(kind='pie', autopct='%1.1f%%', startangle=140)
    plt.title(f'Distribution of {column}')
    plt.ylabel('')
    plt.show()


