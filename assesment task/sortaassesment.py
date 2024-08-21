# importing pandas and matplotlib and setting up the dataset
import pandas as pd
import matplotlib.pyplot as plt
dataset = pd.read_csv('assesment task/world_population.csv', on_bad_lines = 'skip')

# defining all of the functions and variables
true = True
columns = (dataset.columns).to_list
number1 = 0
def saveanquit():
    global columns
    global number1
    global dataset
    newdataset = dataset
    n = input('Do you want to save anything? type 1 if yes press enter or type anything else if no: ')
    if n == '1': 
        t = input('''what do you want to save?
                  1: Table/Spreadsheet
                  2: Chart
                  Type 1 for table and 2 for chart: ''')
        if t == '1':
            print('Which coloums do you want to delete?: ')
            print(columns)
            h = str(input( '''Please type it out as you see it and space out the colunms with a comma and not a space: '''))
            h = h.split(",")
            p = len(h)
            for x in range(p):
                newdataset = newdataset.drop(h[number1], axis = 1)
                number1 = number1 +1
            newdataset.to_csv('world_population_update.csv')
            print('A new csv has been created')
        if t == '2':
                hor = ''
                ver = ''

                p = input('''
                1 for abreviation
                2 for country
                ''')
                l = input('''
                1 for rank
                2 for growth rate
                3 for world population percantage
                4 for population 2022
                ''')
   

                if p == '1':
                    hor = 'Abreviation'
                if p == '2':
                    hor = 'Country/Territory'

                if l == '1':
                    ver = 'Rank'
                    dataset = dataset.sort_values(by='Rank')
                if l == '2':
                    ver = 'Growth Rate'
                    dataset = dataset.sort_values(by='Growth Rate')
                if l == '3':
                    ver = 'Population Percentage'
                    dataset = dataset.sort_values(by='Population Percentage')
                if l == '4':
                    ver = '2022 Population'
                    dataset = dataset.sort_values(by='2022 Population')
                plt.rcParams["figure.figsize"] = [7.50, 3.50]
                plt.rcParams["figure.autolayout"] = True
                dataset.plot(
                     kind = 'bar',
                      x = hor,
                      y = ver,
                      color = 'green',
                      alpha = 0.3,
                      fontsize=3,
                      style='plain',
                     title = ver + ' of countrys'
                    )
                
                plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
                plt.savefig(ver + ' of countrys.png',dpi = 800)
   

def anylizedataset():
    global dataset


    i = input('''What do you want to Calculate?
              1: Mean
              2: Median  
              3: range
              4: total population
              (please type 1 2 3 or 4): ''')
    

    if i == '1':
        y = input("""What do you want to find the mean of
                  1: 2022 population
                  2: 2020 population
                  3: 2015 population
                  4: 2010 population
                  5: 2000 population
                  6: 1990 population
                 (please type 1 2 3 4 5 or 6: """)
        if y == '1':
            mean = dataset['2022 Population'].mean()
        if y == '2':
            mean = dataset['2020 Population'].mean()
        if y == '3':
            mean = dataset['2015 Population'].mean()
        if y == '4':
            mean = dataset['2010 Population'].mean()
        if y == '5':
            mean = dataset['2000 Population'].mean()
        if y == '6':
            mean = dataset['1990 Population'].mean()
        print('the mean is ',mean)


    if i == '2':
        t = input("""What do you want to find the median of
                  1: 2022 population
                  2: 2020 population
                  3: 2015 population
                  4: 2010 population
                  5: 2000 population
                  6: 1990 population
                  (please type 1 2 3 4 5 or 6: """)
        if t == '1':
            median = dataset['2022 Population'].median()
        if t == '2':
            median = dataset['2020 Population'].median()
        if t == '3':
            median = dataset['2015 Population'].median()
        if t == '4':
            median = dataset['2010 Population'].median()
        if t == '5':
            median = dataset['2000 Population'].median()
        if t == '6':
            median = dataset['1990 Population'].median()
        print('the median is ',median)


    if i == '3':
        t = input("""What do you want to find the range of
                  1: 2022 population
                  2: 2020 population
                  3: 2015 population
                  4: 2010 population
                  5: 2000 population
                  6: 1990 population
                  (please type 1 2 3 4 5 or 6: """)
        if t == '1':
            max = dataset['2022 Population'].max()
            min = dataset['2022 Population'].min()
        if t == '2':
            max = dataset['2020 Population'].max() 
            min = dataset['2020 Population'].min()
        if t == '3':
            max = dataset['2015 Population'].max() 
            min = dataset['2015 Population'].min()
        if t == '4':
            max = dataset['2010 Population'].max() 
            min = dataset['2010 Population'].min()
        if t == '5':
            max = dataset['2000 Population'].max() 
            min = dataset['2000 Population'].min()
        if t == '6':
            max = dataset['1990 Population'].max() 
            min = dataset['1990 Population'].min()
        
        print('The max is ',max,'The min is ',min)

    if i == '4':
        t = input("""What do you want to find the total of
                  1: 2022 population
                  2: 2020 population
                  3: 2015 population
                  4: 2010 population
                  5: 2000 population
                  6: 1990 population
                  (please type 1 2 3 4 5 or 6: """)
        if t == '1':
            sum = dataset['2022 Population'].sum()
        if t == '2':
            sum = dataset['2020 Population'].sum()
        if t == '3':
            sum = dataset['2015 Population'].sum()
        if t == '4':
            sum = dataset['2010 Population'].sum()
        if t == '5':
            sum = dataset['2000 Population'].sum()
        if t == '6':
            sum = dataset['1990 Population'].sum()
        print('the sum is ',sum)

def showdataset():
    global dataset
    n = dataset
    n = n.drop('2020 Population',axis = 1)
    n = n.drop('2015 Population',axis = 1)
    n = n.drop('2010 Population',axis = 1)
    n = n.drop('2000 Population',axis = 1)
    n = n.drop('1990 Population',axis = 1)
    n = n.drop('1980 Population',axis = 1)
    n = n.drop('1970 Population',axis = 1)
    n = n.drop('Density (per km²)',axis = 1)
    n = n.drop('Area (km²)',axis = 1)
    n = n.drop('Abreviation',axis = 1)
    n = n.drop('Capital',axis = 1)
    i = input("""What do you want to sort the table by?
    1: Rank
    2: Country
    3: Continent
    4: 2022 Population
    5: Growth rate
    6: Population percent of the world""")
    if i == '1':
        n = n.sort_values(by='Rank')
    if i == '2':
        n = n.sort_values(by='Country/Territory')
    if i == '3':
        n = n.sort_values(by='Continent')
    if i == '4':
        n = n.sort_values(by='2022 Population')
    if i == '5':
        n = n.sort_values(by='Growth Rate')
    if i == '6':
        n = n.sort_values(by='Population Percentage')
    n = n.to_markdown()
    print(n)

def showtable():

    global dataset
    hor = ''
    ver = ''

    p = input('''
    1 for abreviation
    2 for country
    ''')
    l = input('''
    1 for rank
    2 for growth rate
    3 for world population percantage
    4 for population 2022
    ''')
   

    if p == '1':
        hor = 'Abreviation'
    if p == '2':
        hor = 'Country/Territory'

    if l == '1':
        ver = 'Rank'
        dataset = dataset.sort_values(by='Rank')
    if l == '2':
        ver = 'Growth Rate'
        dataset = dataset.sort_values(by='Growth Rate')
    if l == '3':
        ver = 'Population Percentage'
        dataset = dataset.sort_values(by='Population Percentage')
    if l == '4':
        ver = '2022 Population'
        dataset = dataset.sort_values(by='2022 Population')

    dataset.plot(
         kind = 'bar',
          x = hor,
          y = ver,
          color = 'green',
          alpha = 0.3,
          fontsize=8,
         title = ver + ' of countrys'
        )
    plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
    plt.show()


# running all of the functions

while true == True:
    i = input("do you want a table or a spreadsheet?(1 for table 2 for spreadsheet 3 for anylizing and type q to quit and save): ")
    if i == '1':
        showtable()
    if i == '2':
        showdataset()
    if i == '3':
        anylizedataset()
    if i == 'q':
        saveanquit()
        break
    else:
        print('')
