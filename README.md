## Clustering-by-Silhouette
create the best clustering by the measure of Silhouette Score automatically.

## Overview
We cannot know always which parameter value will give us the best clustering result. Many times we do not have enough previous knowledge on the data and the subject we are researching, so we do not know which parameter to choose. Also, in the case of data with 2 or 3 dimensions, you can review the results and determine whether the clustering successful. But for a dataset with more dimensions, it become much more complex procedure. This situation causes a lot of time wasted in finding the optimal value for the parameter. In order to solve this difficulty, the code [**clustering_by_silhouette.py**](https://github.com/EtzionData/Clustering-by-Silhouette/blob/master/clustering_by_silhouette.py) created.

Entering different parameters into the clustering function probabliy result us get different outcomes. For example, we will use Kmeans on [**data_3.xlsx**](https://github.com/EtzionData/Clustering-by-Silhouette/blob/master/Example/data_3.xlsx) dataset, so each time we set a different K value. As you can see, we get different results for each input:

![nine](https://github.com/EtzionData/Clustering-by-Silhouette/blob/master/Pictures/nine_clusters.png)
By simply looking at the scatter plot, it can be seen that there are **six clusters** in the dataset. But how can we automatically determine that K = 6 gives the best outcome? To answer this question we can use **silhouette score**. silhouette method can gives us some assessment to the quality of the clustering output. As you can see, each subplot has a silhouette score: The closer the score is to 1, the better the clustering function performe the separation into clusters. We do see that for K = 6 calculated the highest silhouette-score: 0.662!

So, to determine the best input value, the code runs on a specific number range and each of them is entered into the clustering function. Then, the code compares the different results obtained using the Silhouette Score. as you can see in the example, different input values to the clustering function return different silhouette score:

![score](https://github.com/EtzionData/Clustering-by-Silhouette/blob/master/Pictures/silhouette_score_example.png)

This example (based on the **Kmeans** algorithm) shows the differences scores between different clustering results. Every result based on a different cluster number value. It can be seen that we get the best score when **k=6** for this specific example. This is why we choose to input k=6. Similarly, the code at the end of the process, returns only the clustering labels with the highest silhouette result. 

The code uses three different types of clustering algorithms (of course other types can be adapted to it):

- **KMeans**: This function enters the code at each step of loop other **n_clusters value**. According to this **K** value, determines the number of clusters to which the dataframe must be divided.

- **MeanShift**: For this function, the code enters different values for the **bandwidth** parameter. this parameter determines the area scale size for mean calculation.

- **HDBSCAN**: For this function, the code enters the values for the **min_cluster_size** parameter.This parameter determines the samples quantity that should considered as a cluster.

All these functions are stored in the **"CLUSTERING"** dictionary which returns the appropriate function according to input key. Each of the functions performs the clustering process differently, so the values that the code enters also result in different results from each other. An example can be seen from the outputs that the functions genereted, based on the optimal values found by [**clustering_by_silhouette.py**](https://github.com/EtzionData/Clustering-by-Silhouette/blob/master/clustering_by_silhouette.py):

![functions](https://github.com/EtzionData/Clustering-by-Silhouette/blob/master/Pictures/functions.png)

The outputs of each clustering functions are inserted into a **adjusted silhouette function**. First, the data is filtered so that a silhouette value is not calculated based on rows that have not been defined as part of any cluster. Such entities are formed as part of the output from **HDBSCAN** algorithm and their label is marked as: **-1**. Also, for such datasets, the silhouette score calculated relativity to rate of **label = -1** records. That is, if **N** is the number of records in the original dataset, and **M** is the number of records after filtering label = -1, then the silhouette score will be:
**silhouette ∙ (M/N)**

In addition, the adjustments made to the silhouette function deal with the familiar silhouette **MemoryError**. This error is caused by an extensive amount of samples on which the algorithm is required to run. In order to deal with this error, the number of samples on them must be reduced using the **sample_size** parameter. However, reducing the samples number will result less-accurate results (since the results are not based on all the data). Therefore, when we get MemoryError, the code will reduce the sample_size by 5% of its previous quantity. this method continue in **loop**, until the appropriate value that allow the silhouette return answer. The new sample_size will be saved, so basically once the corresponding value is found, no further adjustments will be required.

The following graph shows the adjusted sample_size at each step of the loop:

![graph](https://github.com/EtzionData/Clustering-by-Silhouette/blob/master/Pictures/sample_size.png)

Another option that exists in the code is to perform **steps** in the run over the defined number range. This simple option runs based on the "step" parameter of the "range" function. This option is significant when there small changes for a close number range. To define number of steps, you can use the **"stp"** parameter. Illustration for this option can be seen in the following example of **stp=2** (based on the dataset of [HDBSCAN documentation](https://hdbscan.readthedocs.io/en/latest/comparing_clustering_algorithms.html#hdbscan)):

![stp_gif](https://github.com/EtzionData/Clustering-by-Silhouette/blob/master/Pictures/set_bar_2.gif)

Application of the code can be seen in the file **implementation_results.pdf**. The implementation performed **3D visualization** based on the results, using a code to create three-dimensional outputs **GIF**. The visualization code written as part of another project. Full details and documentation can be seen here: [**create-3d-graph-gif**](https://github.com/EtzionData/create-3d-graph-gif). Example of one of the outputs:

![gif](https://github.com/EtzionData/Clustering-by-Silhouette/blob/master/Pictures/example.gif)

**NOTE:** Although all the graph examples in this documentation describe results for 2 or 3 dimensional cases, the code itself also **works for a multidimensional** dataset.

## Libraries
The code uses the following libraries in Python:

**sklearn**

**hdbscan**

**pandas**


## Application
An application of the code is attached to this page under the name: 

[**implementation**](https://github.com/EtzionData/Clustering-by-Silhouette/blob/master/implementation_results.pdf)

the examples outputs are also attached here.


## Example for using the code
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
stp = 2

# application
data['labels'] = silhouette_clustering(data, typ, org, lim, stp)
```

When the variables displayed are:

**data:** pandas dataframe that you want to perform clustering on all its columns

**typ:** the clustering type (default: 'kmeans')

**org:** bottom value to input the clustering function (default: 2)

**lim:** upper value to input the clustering function (default: 20)

**stp:** define the gap between each step between **"org"** to **"lim"** (default: 1)


## License
MIT © [Etzion Harari](https://github.com/EtzionData)

