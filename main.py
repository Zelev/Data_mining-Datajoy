import numpy as np
import matplotlib as pyplot
import matplotlib.pyplot as plt
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.tools as tls

def main():
    data_file = open('detergente_modificado.txt', 'r')
    data_counters = {}
    related_counters = {}
    categories = []
    pref_users = {'M-user': {}}
    
    for line in data_file:
        if 'M-user' in line:
            categories = line.split()
            for category in categories:
                data_counters[category] = {}

        else:
            # Le cambie el orden porque cuando lo cambie a 
            # detergente_modificado quedo distinto
            # ^^Esta bien, esa era la idea^^
            results = line.split()
            previous_m_user = False
            if results[2] == 'X' and results[0] == 'No':
                if results[3] == 'Soft' and (results[3] not in pref_users['M-user']):
                    pref_users['M-user'][results[3]] = 1
                elif results[3] == 'Soft':
                    pref_users['M-user'][results[3]] += 1
                elif results[3] == 'Medium' and (results[3] not in pref_users['M-user']):
                    pref_users['M-user'][results[3]] = 1
                elif results[3] == 'Hard' and (results[3] not in pref_users['M-user']):
                    pref_users['M-user'][results[3]] = 1
                elif results[3] == 'Hard':
                    pref_users['M-user'][results[3]] += 2
                elif results[3] == 'Medium':
                    pref_users['M-user'][results[3]] += 1
                previous_m_user = True
            
            
        
            data_counters = counter(category='M-user', data=results[0],
                                    data_counters=data_counters, previous_m_user=False)
            data_counters = counter(category='Temperature', data=results[1],
                                    data_counters=data_counters, previous_m_user=False)
            data_counters = counter(category='Preference', data=results[2],
                                    data_counters=data_counters, previous_m_user=False)
            data_counters = counter(category='WaterSoftness', data=results[3],
                                    data_counters=data_counters, previous_m_user=False)
    
    #print pref_users
    print data_counters
    x = ['M','X']
    y = [data_counters['Preference']['M']['value'], data_counters['Preference']['X']['value']]
    # data_preference = [go.Bar(x = ['M','X'], y = [data_counters['Preference']['M'], data_counters['Preference']['X']])]
    # graph = plt.plot(data_preference, filename ='basic-bar')
    y_pos = np.arange(len(x))
    plt.bar(y_pos, y, align='center', alpha=0.25)
    plt.xticks(y_pos, x)
    plt.ylabel('Users')
    plt.title('Users M or X')
    #plt.yscale(0,1000)
    plt.show()
    
    index = 4
    
   
def counter(category, data, data_counters, previous_m_user):
    #total users
    if data not in data_counters[category]:
        data_counters[category][data] = {}
        data_counters[category][data]['value'] = 1
        data_counters[category][data]['previous_m_user'] = 0 
    else:
        data_counters[category][data]['value'] += 1
    #previous m users
    if previous_m_user and data not in data_counters[category]['previous_m_user']:
        data_counters[category][data]['previous_m_user'] = 1
    else:
        data_counters[category][data]['previous_m_user'] += 1
    return data_counters
    

    

main()


# x = np.linspace(0, 2 * np.pi, 100)

# plt.plot(x, np.sin(x))
# plt.show()


