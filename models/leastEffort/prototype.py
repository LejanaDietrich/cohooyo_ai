#as specified by Alessandro
#https://cohooyo-angular.s3.amazonaws.com/NLP+Cold+Recommender+System.html

#parameters - name of graphs being created change with these too
# "de_core_news_", "sm", 4 in example from cohooyo/Alessandro
modelLang = "de_core_news_"
modelSize = "md"
#abhaengig machen von Anzahl der Datensaetze:
clusterSize = 7

#see mapped_jobs for changing the mapping parameters

#imports for nlp
import requests
import json
from functools import reduce
import numpy as np
import string
from sklearn.feature_extraction import text as text_feature_extraction
from sklearn.feature_extraction import stop_words
import spacy
#change to compare 
modelString = modelLang + modelSize
nlp = spacy.load(modelString)

#imports for ml algorithm
from sklearn.cluster import KMeans #current



#DATA
#own user list with hashtags and evaluation score
#e.g. [hashtags, yes-swipes, no-swipes, locations]
users = [
    [['Ausbildung', 'Elektrotechnik', 'Volt'], ['5f3b78a4809ba900124873fa', '5f3b770d809ba900124873ee'], ['5f914b8a759f730012afba96'],[]],
    [['Brot backen'], ['5f914b8a759f730012afba96'], [], [[{'latitude': 49.4874592, 'longitude': 8.466039499999999}]] ],
    [['Holzverarbeitung'], ['5f3b7a10809ba9001248740c'], ['5f3b78a4809ba900124873fa'], [[]]],
    [[],[],[], []],
    [['Informatik'],[],[], []],
]

#e.g. userid, jobid, rating-score (e.g. 0-5) 
evaluations = [
    [0,'5f914b8a759f730012afba96', 1],
    [0,'5f914a19759f730012afba91', 5],
    [0,'5f8eb46de4d7f00012ea81b7', 0],
    [0,'5f46cb7c0b4ceb0012577524', 2],
    [0,'5f46c88b0b4ceb001257751e', 0],
    [0,'5f46c4020b4ceb0012577514', 2],
    [0,'5f3ba0d0809ba90012487452', 5],
    [0,'5f3ba0ae809ba9001248744e', 4],
    [0,'5f3b9ee1809ba90012487449', 2],
    [0,'5f3b9d1b809ba9001248743e', 4],
    [0,'5f3b7a10809ba9001248740c', 5],
    [0,'5f3b78a4809ba900124873fa', 5],
    [0,'5f3b770d809ba900124873ee', 5],
    [0,'5f2fdf6c15633f0012d6dbed', 5],
    [0,'5f2fddac15633f0012d6dbe8', 0],
    [0,'5f2eb49615633f0012d6dbc7', 0],
    [1,'5f914b8a759f730012afba96', 5],
    [1,'5f914a19759f730012afba91', 4],
    [1,'5f8eb46de4d7f00012ea81b7', 0],
    [1,'5f46cb7c0b4ceb0012577524', 4],
    [1,'5f46c88b0b4ceb001257751e', 4],
    [1,'5f46c4020b4ceb0012577514', 0],
    [1,'5f3ba0d0809ba90012487452', 3],
    [1,'5f3ba0ae809ba9001248744e', 1],
    [1,'5f3b9ee1809ba90012487449', 4],
    [1,'5f3b9d1b809ba9001248743e', 2],
    [1,'5f3b7a10809ba9001248740c', 0],
    [1,'5f3b78a4809ba900124873fa', 4],
    [1,'5f3b770d809ba900124873ee', 4],
    [1,'5f2fdf6c15633f0012d6dbed', 1],
    [1,'5f2fddac15633f0012d6dbe8', 5],
    [1,'5f2eb49615633f0012d6dbc7', 3],
    [2,'5f914b8a759f730012afba96', 5],
    [2,'5f914a19759f730012afba91', 5],
    [2,'5f8eb46de4d7f00012ea81b7', 2],
    [2,'5f46cb7c0b4ceb0012577524', 5],
    [2,'5f46c88b0b4ceb001257751e', 1],
    [2,'5f46c4020b4ceb0012577514', 3],
    [2,'5f3ba0d0809ba90012487452', 4],
    [2,'5f3ba0ae809ba9001248744e', 2],
    [2,'5f3b9ee1809ba90012487449', 1],
    [2,'5f3b9d1b809ba9001248743e', 0],
    [2,'5f3b7a10809ba9001248740c', 4],
    [2,'5f3b78a4809ba900124873fa', 1],
    [2,'5f3b770d809ba900124873ee', 1],
    [2,'5f2fdf6c15633f0012d6dbed', 1],
    [2,'5f2fddac15633f0012d6dbe8', 3],
    [2,'5f2eb49615633f0012d6dbc7', 5],
    [3,'5f914b8a759f730012afba96', 1],
    [3,'5f914a19759f730012afba91', 1],
    [3,'5f8eb46de4d7f00012ea81b7', 4],
    [3,'5f46cb7c0b4ceb0012577524', 0],
    [3,'5f46c88b0b4ceb001257751e', 2],
    [3,'5f46c4020b4ceb0012577514', 5],
    [3,'5f3ba0d0809ba90012487452', 4],
    [3,'5f3ba0ae809ba9001248744e', 5],
    [3,'5f3b9ee1809ba90012487449', 4],
    [3,'5f3b9d1b809ba9001248743e', 1],
    [3,'5f3b7a10809ba9001248740c', 3],
    [3,'5f3b78a4809ba900124873fa', 1],
    [3,'5f3b770d809ba900124873ee', 2],
    [3,'5f2fdf6c15633f0012d6dbed', 2],
    [3,'5f2fddac15633f0012d6dbe8', 1],
    [3,'5f2eb49615633f0012d6dbc7', 5],
    [4,'5f914b8a759f730012afba96', 4],
    [4,'5f914a19759f730012afba91', 3],
    [4,'5f8eb46de4d7f00012ea81b7', 0],
    [4,'5f46cb7c0b4ceb0012577524', 4],
    [4,'5f46c88b0b4ceb001257751e', 1],
    [4,'5f46c4020b4ceb0012577514', 2],
    [4,'5f3ba0d0809ba90012487452', 2],
    [4,'5f3ba0ae809ba9001248744e', 5],
    [4,'5f3b9ee1809ba90012487449', 1],
    [4,'5f3b9d1b809ba9001248743e', 0],
    [4,'5f3b7a10809ba9001248740c', 0],
    [4,'5f3b78a4809ba900124873fa', 5],
    [4,'5f3b770d809ba900124873ee', 1],
    [4,'5f2fdf6c15633f0012d6dbed', 1],
    [4,'5f2fddac15633f0012d6dbe8', 1],
    [4,'5f2eb49615633f0012d6dbc7', 0]
]

#access API
r = requests.get('https://api.cohooyo.com/jobs')
jobs = json.loads(r.text)
print(len(jobs))
#print(jobs)
print(jobs[22])


#IMPLEMENTATION
#pca = principal component analysis, project data to a lower dimensional space
def pca(data):
    from sklearn.decomposition import PCA
    pca = PCA(n_components=2)
    pca.fit(data)
    return pca.transform(data)


#TODO: Find best simple mapping for internal model
#Feature Selection + mapping with spacy vectors
mapped_jobs = list(map(lambda job: np.concatenate((nlp(job['jobTitle']).vector,[job['latitude'],job['longitude']])), jobs))


#Visualization of Data
from matplotlib import pyplot as plt
data=pca(mapped_jobs)

plt.scatter(data[:,0],data[:,1])

for index,xy in enumerate(zip(data[:,0], data[:,1])):   
    plt.annotate(jobs[index]['_id'][0:7], xy=xy, textcoords='data')

#in AI root directory, shows unclustered but mapped data
#plt.savefig("models\leastEffort\visualization\mappingLarge.png")


# Clustering
kmeans = KMeans(n_clusters=clusterSize)
# fit kmeans object to data
kmeans.fit(mapped_jobs)
mapped_clusters = kmeans.fit_predict(mapped_jobs)

plt.scatter(data[:,0],data[:,1], c=mapped_clusters)

#in AI root directory, shows clustered data
saveString = 'models\leastEffort\\visualization\clustering' + modelSize + str(clusterSize) + '.png'
plt.savefig(saveString)




'EVALUATE'
from functools import reduce

#TODO: Find out how to get exact distance between the mapped points
def closest_cluster(jobid):
    indices_only=list(map(lambda job: job["_id"], jobs))    
    _=indices_only.index(jobid)
    clusternr = mapped_clusters[_]
    return mapped_clusters[_]


def get_jobs_by_cluster(clusterid):
    jobs_indices = np.where(mapped_clusters==clusterid)[0]
   
    return_jobs = []
    for index, job in enumerate(jobs):
        if index in jobs_indices:
            return_jobs.append(job['_id'])
    
    return return_jobs
    
likes_per_users = list(map(lambda user: user[1], users))
list_of_clusters_per_user=list(map(lambda likes_per_user: list( map(lambda user_like: closest_cluster(user_like), likes_per_user)) , likes_per_users))
recommended_jobs=list(map(lambda list_per_user: list(map(lambda cluster:get_jobs_by_cluster(cluster),list_per_user)), list_of_clusters_per_user))
recommendations = list(map(lambda user_recommendations:reduce(lambda x,y: x+y,user_recommendations,[]),recommended_jobs))
print('\n', recommendations) 


#Set threshold for boolean decision
thresholded_evaluations=list(map(lambda evaluation: [evaluation[0],evaluation[1], 1 if evaluation[2]>2 else 0] , evaluations ))

#Add Prediction Score
def find_prediction(userid, jobid):
    if jobid in recommendations[userid]:
        return 1
    else:
        return 0

results_for_confusion_matrix=[]

y_true=[]
y_pred=[]
for evaluation in thresholded_evaluations:
    prediction=find_prediction(evaluation[0], evaluation[1])
    evaluation.append(prediction)
    results_for_confusion_matrix.append(evaluation)
    y_true.append(evaluation[2])
    y_pred.append(prediction)


from sklearn.metrics import confusion_matrix

_=confusion_matrix(y_true, y_pred)
import seaborn as sns
sns.heatmap(_/np.sum(_), annot=True, fmt='.2%', cmap='Blues')

saveString = 'models\leastEffort\\visualization\confusionMatrix' + modelSize + str(clusterSize) + '.png'
plt.savefig(saveString)
