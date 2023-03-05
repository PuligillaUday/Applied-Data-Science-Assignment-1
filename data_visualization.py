# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 15:44:32 2023

@author: udayp
"""

import matplotlib.pyplot as plt
import pandas as pd

"""
   Define a function to read the data from a CSV file and clean it up
"""
def read_data():
    # Read the data from a CSV file
    data = pd.read_csv(r'C:\Users\udayp\Desktop\Uday Puligilla\TaxsOnGoodsAndServices.csv')
    
    # Remove unnecessary columns
    data = data.drop(columns=['Series Name','Series Code','Country Code','2021 [YR2021]'])
    
    # Drop rows with missing values
    data = data.dropna()
    
    # Return the cleaned up data
    return data

"""
   Define a function to create a line plot
""" 
def line_plot_visualization(data):
    # Set the x-axis labels
    years = ['2012', '2013', '2014', '2015', '2016', '2017', '2018']

    # Create the plot
    plt.figure(figsize=(10,8))
    for i in range(0, 8):
        # Plot each line
        plt.plot(years, data.iloc[i, 1:8], label=data.iloc[i, 0])
        
    # Set the x-axis and y-axis labels
    plt.xlabel('Year')
    plt.ylabel('Taxes on goods and services (% of revenue)')
    
    # Set the legend position and font size
    plt.legend(loc='upper left', bbox_to_anchor=(1.0, 1.0), fontsize=12)

    # Set the plot title
    plt.title('Taxes on goods and services over time for select countries')
    
    # Add a description
    plt.figtext(0.5, -0.1, "This line plot shows how taxes on goods and services (% of revenue) \n have changed over time (2012-2018) for select countries. \n Each line represents a different country, and the legend identifies which line corresponds to each country. \n The plot shows that while taxes have generally increased over time for most countries,\n there is a lot of variation in the magnitude of the increase between countries.\n For example, the taxes in the United Kingdom increased at a slower rate compared to\n other countries such as France and China.", ha="center", fontsize=12)
    
    # Display the plot
    plt.show()
"""
   Define a function to create a pie chart
"""
def pie_plot_visualization(data, year):
    # Create the plot
    plt.figure(figsize=(10,10))
    plt.pie(data[f'{year} [YR{year}]'], labels=data['Country Name'], autopct='%1.1f%%')
    
    # Set the plot title
    plt.title(f'Taxes on goods and services in {year}')
    
    # Set the legend position and font size
    plt.legend(loc='upper left', bbox_to_anchor=(1.0, 1.0), fontsize=12)

    # Display the plot
    plt.show()
"""
   Define a function to create a bar chart
"""
def bar_plot_visualization(data):
    # extract the country names from the data
    x = data['Country Name']
    # extract the tax data for 2012 from the data
    y = data['2012 [YR2012]']
    
    # set the size of the figure
    plt.figure(figsize=(14,8)) 

    # create a bar chart using the data for 2012
    plt.bar(x, y, label="TOGAS", color='steelblue')

    # set the x-axis label
    plt.xlabel('Country Name', fontsize=14) 
    # set the y-axis label
    plt.ylabel('Taxes on goods and services (% of revenue)', fontsize=14)
    
    # set the tick size
    plt.tick_params(axis='both', which='major', labelsize=12)
    
    # rotate the x-axis labels for better visibility
    plt.xticks(rotation=90) 

    # add a legend to the plot
    plt.legend(loc='upper left', bbox_to_anchor=(1.0, 1.0), fontsize=12)
    
    # set the title of the plot
    plt.title('Taxes on goods and services in 2012', fontsize=16) 
    
    # display the plot
    plt.show() 

def main():
    data = read_data()
    line_plot_visualization(data)
    pie_plot_visualization(data, '2014')
    pie_plot_visualization(data, '2018')
    bar_plot_visualization(data)


if __name__ == '__main__':
    main()