from  more_itertools import unique_everseen
from sklearn.cluster import KMeans, DBSCAN, AffinityPropagation
from scipy.cluster.vq import kmeans,vq
import matplotlib.pyplot as plt

class Wholesale:
    # region 3 buys more Fresh
    # region 3 buys more Milk
    # region 3 buys more Delicassen
    # region 2 buys more Detergents_Paper
    # region 2 buys more Frozen
    # region 2 buys more Grocery
    
    def __init__(self):
        self.data_file = open('Taller_Cluster/wholesale_dataset.txt', 'r')
        data_set_pre = [x.split(',') for x in self.data_file]
        self.data_file.close()
        
        self.labels = data_set_pre[0]
        self.labels[-1] = self.labels[-1][:-1]
        data_set_pre = data_set_pre[1:]
        data_set = []
        for data_line in data_set_pre:
            data_line[-1] = data_line[-1][:-1]
            data_line = [int(data) for data in data_line]
            data_set.append(data_line)
        
        # Separate the channels and regions for use as categories
        channels, regions = zip(*[(x[self.labels.index('Channel')], x[self.labels.index('Region')]) for x in data_set])
        channels = self.get_category(channels)
        regions = self.get_category(regions)
        
        data_per_region = self.data_per_category(data_set, regions, self.labels.index('Region'))
        data_per_channel = self.data_per_category(data_set, channels, self.labels.index('Channel'))
        
        region1_average = self.get_average(data_per_region[1], self.labels)
        region2_average = self.get_average(data_per_region[2], self.labels)
        region3_average = self.get_average(data_per_region[3], self.labels)
        
        fresh, milk, deli, detergent, frozen, grocery = zip(*[(x[self.labels.index('Fresh')],
                                                               x[self.labels.index('Milk')],
                                                               x[self.labels.index('Delicassen')],
                                                               x[self.labels.index('Detergents_Paper')],
                                                               x[self.labels.index('Frozen')],
                                                               x[self.labels.index('Grocery')],) for x in data_set])
        
        self.plot_cluster(deli, fresh, ['Delicatessen','Fresh'])
    
    def get_category(self, items):
        items_list = list(unique_everseen(items))
        return items_list
    
    def data_per_category(self, data_set, category_list, category_index):
        return_dict = {}
        for category in category_list:
            return_dict[category] = [x for x in data_set if x[category_index] == category]
        return return_dict

    def get_average(self, data_set, categories):
        average = {}
        for category in categories[2:]:
            average[category] = sum([x[categories.index(category)] for x in data_set])/len(data_set)
        return average
    
    def plot_cluster(self, xaxis, yaxis, labels):
        '''Given that the lenghts of xaxis and yaxis are the same'''
    
        if len(xaxis) == len(yaxis):
            data_show = [[xaxis[i], yaxis[i]] for i in xrange(len(xaxis))]
            cluster_plot = KMeans(n_clusters=4).fit_predict(data_show)
            # cluster_plot = DBSCAN(eps=0.1).fit_predict(data_show)
            # cluster_plot = AffinityPropagation(damping=0.9).fit_predict(data_show)
            plt.scatter(xaxis, yaxis, c=cluster_plot)
            plt.xlabel(labels[0])
            plt.ylabel(labels[1])
            plt.show()
        else:
            return 'data not related lenght-wise'
