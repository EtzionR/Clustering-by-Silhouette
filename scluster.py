# Create by Etzion Harari
# https://github.com/EtzionR

# import libraries
from sklearn.cluster import KMeans, MeanShift
from sklearn.metrics import silhouette_score
from hdbscan import HDBSCAN


# dictionary of clustering functions:
CLUSTERING = {'kmeans' : lambda df, k: KMeans(n_clusters = k).fit(df).labels_,
             'hdbscan' : lambda df, s: HDBSCAN(min_cluster_size = s).fit(df).labels_,
            'meanshift': lambda df, q: MeanShift(bandwidth=0.025*min(q,50)).fit(df).labels_}

# the clustering by silhouette object
class SCluster:
    """
    The object that calculate the clustering by silhouette.
    for each step, the object calculate the clustering labels,
    and then, calculate for each result the silhouette score.
    next, this code choose the labels with the best score.
    """
    def __init__(self,typ='kmeans', org=2, lim=20, stp=1, dup=0.95):
        """
        initialize the object
        :param typ: clustering type
        :param org: first value in the loop
        :param lim: last value in the loop
        :param stp: # values between each step
        :param dup: value for fix dataframe row length for silhouette
        """
        # initial parameters
        self.type= typ
        self.org = org
        self.lim = lim+1
        self.stp = stp
        self.dup = dup

        # clustering function
        self.function = CLUSTERING[self.type.lower()]

        # values for calculation
        self.max = -1
        self.scores = {}
        self.labels_= []

    def adapt_silhouette(self,labels):
        """
        calculate the silhouette value for the given dataframe
        :param labels: cluster labels
        :return: the dataframe silhouette score for the given labels
        """
        data, labels= self.df[labels > -1], labels[labels > -1]
        if data.shape[0] == 0: return -1
        while True:
            try:
                return silhouette_score(data, labels, sample_size=self.size)*(labels.shape[0]/self.n)
            except:
                self.size = int(self.size*self.duf)

    def fit(self,data):
        """
        fit the optimal cluster labels to the data
        :param data: input dataframe
        """
        self.n = data.shape[0]
        self.size = self.n
        self.df = data
        for i in range(self.org, self.lim , self.stp):
            label = self.function(self.df, i)
            silho = self.adapt_silhouette(label)
            self.scores[silho] = label
            self.max = silho if self.max<silho else self.max
            print(f'cluster kind: {self.type}, input value = {i}, silhouette = {round(silho,2)}')
        self.labels_ = self.scores[self.max]
        return self

      
  # MIT © Etzion Harari
