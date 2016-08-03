import csv
import matplotlib.pyplot as plt
import numpy as np


CATEGORIES = ['Unknown', 'Action', 'Adventure',
        'Animation', 'Children','Comedy', 'Crime', 'Documentary',
        'Drama', 'Fantasy', 'FilmNoir', 'Horror',
        'Musical','Mystery','Romance', 'SciFi',
        'Thriller', 'War', 'Werstern\r\n']


def get_category(items):
    items_list = list(unique_everseen(items))
    return items_list
    

def data_per_category(data_set, category_list, category_index):
    return_dict = {}
    for category in category_list:
        return_dict[category] = [x for x in data_set if x[category_index] == category]
    return return_dict
    

def get_sum(data_set, categories):
    average = {}
    for category in categories:
        average[category] = sum([x[categories.index(category)] for x in data_set])
    return average


def read_file(file_name, separator):
    raw_data = [line.split(separator) for line in open(file_name, 'r')]
    return raw_data


review_data = read_file('Proyecto/dataUser.csv', ',') 
labels = review_data[0]
data = review_data[1:]

item_raw = read_file('Proyecto/items.tsv', '|')
item_data = [line[5:] for line in item_raw]
item_proc = []
for item in item_data:
    data_aux = [int(flag) for flag in item]
    item_proc.append(data_aux)


movies_proc ={'totals':{}}
for category in CATEGORIES:
    movies_proc[category] = [x for x in item_proc if x[CATEGORIES.index(category)] == 1]
    movies_proc['totals'][category] = get_sum(movies_proc[category], CATEGORIES)

def show_bars_chart(totals, category):
    chart_labels = CATEGORIES
    chart_labels.remove(category)
    sizes = [ totals[lbl]  for lbl in chart_labels]
    colors = ['darkgoldenrod','blue','yellow','firebrick','white','purple','green','magenta','cyan'] 
    y_pos = np.arange(len(chart_labels))
    plt.barh(y_pos, sizes, align='center', alpha=0.4)
    plt.yticks(y_pos, chart_labels)
    plt.xlabel('# Movies')
    plt.title(category + ' Movies Genres')
    plt.show()
    
#def show_blox_plot
    
def show_genres_charts():
    for category in CATEGORIES:
        show_bars_chart(movies_proc['totals'][category], category)