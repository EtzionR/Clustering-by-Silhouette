from sklearn.cluster import KMeans, MeanShift
from sklearn.metrics import silhouette_score
from hdbscan import HDBSCAN


# dictionary of clustering functions:
CLUSTERING = {'kmeans' : lambda df, k: KMeans(n_clusters = k).fit(df).labels_,
             'hdbscan' : lambda df, s: HDBSCAN(min_cluster_size = s).fit(df).labels_,
            'meanshift': lambda df, q: MeanShift(bandwidth=0.025*min(q,50)).fit(df).labels_}


def adapt_silhouette(data, labels, memory):
    """
    calculate the silhouette value for the given dataframe
    :param data: input dataframe
    :param labels: cluster labels
    :param memory: sample_size to run the silhouette score
    :return: the dataframe silhouette score for the given labels
    """

    data, labels, length = data[labels>-1], labels[labels>-1], len(labels)
    if data.shape[0]==0: return-1
    while True:
        try:
            return silhouette_score(data, labels, sample_size=memory['size'])*(len(labels)/length)
        except:
            memory['size'] = int(memory['size']*0.95)


def silhouette_clustering(data, typ='kmeans', org=2, lim=20, stp=1):
    """
    calculate the best clustering labels, by silhouette score
    :param data: given dataframe
    :param typ:  clustering type (default: kmeans)
    :param org:  bottom value to input the clustering function (default: 2)
    :param lim:  upper value to input the clustering function (default: 20)
    :return: the best clustering label by silhouette score
    """

    memory = {'size': data.shape[0]}
    scores = {}
    cluster= CLUSTERING[typ.lower()]
    for i in range(org, lim+1,stp):
        lable = cluster(data, i)
        silho = adapt_silhouette(data, lable, memory)
        scores[silho] = lable
        print(f'cluster kind: {typ},   input value = {i},   silhouette = {round(100*silho,1)}%')
    return scores[max(scores.keys())]
