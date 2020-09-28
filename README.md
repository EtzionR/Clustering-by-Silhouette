## Clustering-by-Silhouette
create the best clustering by the measure of Silhouette score automatically.

## introduction
We cannot know always which parameter value will give us the best clustering result. Many times we do not have enough previous knowledge on the data and the subject we are researching, so we do not know which parameter to choose. This situation causes a lot of time wasted in finding the optimal value for the parameter. In order to solve this difficulty, the code [**clustering_by_silhouette.py**](https://github.com/EtzionData/Clustering-by-Silhouette/blob/master/clustering_by_silhouette.py) created.

The code runs on a specific number range and each of them is entered into the clustering function. Then, the code compares the different results obtained using the **Silhouette Score**. as you can see in the example, different input values to the clustering function return different silhouette score:

![score](https://github.com/EtzionData/Clustering-by-Silhouette/blob/master/Pictures/silhouette_score_example.png)

This example (based on the **Kmeans** algorithm) shows the differences exist between the different results. Every result based on a different cluster number value. It can be seen that we get the best score when **k=5**. This is why we choose to return only the lable results only for k=5. Similarly, the code at the end of the process, returns only the clustering labels with the highest silhouette result. 

The code uses three different types of clustering algorithms (of course other types can be adapted to it):

- **KMeans**: This function enters the code at each step of loop other **n_clusters value**. According to this **K** value, determines the number of clusters to which the dataframe must be divided.

- **MeanShift**: For this function, the code enters different values for the **bandwidth** parameter. this parameter determines the area scale size for mean calculation.The values entered reach until 0.5 value.

- **HDBSCAN**: For this function, the code enters the values for the **min_cluster_size** parameter.This parameter determines the samples quantity that should considered as a cluster.

All these functions are stored in the **CLUSTERING** dictionary which returns the appropriate function according to input key.

The outputs of those clustering functions are inserted into a adjusted **silhouette** function. First, the data is filtered so that a silhouette value is not calculated based on rows that have not been defined as part of any cluster. Such entities are formed as part of the output from **HDBSCAN** algorithm and their label is marked as: **-1**.

In addition, the adjustments made to the silhouette function deal with the familiar silhouette **MemoryError**. This error is caused by an extensive amount of samples on which the algorithm is required to run. In order to deal with this error, the number of samples on them must be reduced using the **sample_size** parameter. However, reducing the samples number will result less-accurate results (since the results are not based on all the data). Therefore, when we get MemoryError, the code will reduce the sample_size by 5% of its previous quantity. this method continue in **loop**, until the appropriate value that allow the silhouette return answer. The new sample_size will be saved, so basically once the corresponding value is found, no further adjustments will be required.

The following graph shows the adjusted sample_size at each step of the loop:
![graph](https://github.com/EtzionData/Clustering-by-Silhouette/blob/master/Pictures/sample_size_.png)

Application of the code can be seen in the file **implementation_results.pdf**. The implementation performed **3D visualization** based on the results, using a code to create three-dimensional outputs **GIF**. The visualization code written as part of another project. Full details and documentation can be seen here: [**create-3d-graph-gif**](https://github.com/EtzionData/create-3d-graph-gif). Example of one of the outputs:

![gif](https://github.com/EtzionData/Clustering-by-Silhouette/blob/master/Pictures/example.gif)

## libraries
The code uses the following libraries in Python:

**sklearn**

**hdbscan**

**pandas**


## application
An application of the code is attached to this page under the name: 

[**implementation**](https://github.com/EtzionData/Clustering-by-Silhouette/blob/master/implementation_results.pdf)

the examples outputs are also attached here.


## example for using the code
To use this code, you just need to import it as follows:
``` sh
# import
from clustering_by_silhouette import silhouette_clustering
import pandas as pd

# define variables
data= pd.read_csv(r'path\data.csv')  
typ = 'hdbscan'
org = 4 
lim = 8 

# application
data['labels'] = silhouette_clustering(data, typ, org, lim)
```

When the variables displayed are:

**data:** pandas dataframe that you want to perform clustering on all its columns

**typ:** the clustering type (default: 'kmeans')

**org:** bottom value to input the clustering function (default: 2)

**lim:** upper value to input the clustering function (default: 20)


# License
MIT © [Etzion Harari](https://github.com/EtzionData)

