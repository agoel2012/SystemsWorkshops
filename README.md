# SystemsWorkshops
Workshops for Cloud Systems Coursework

# Workshop 1
## Build a 2 stage data-pipeline that imports MovieLens rating dataset to produce list of worst rated movies of all time
### Pre-requisite
Download MovieLens DataSet `ml-latest-small.zip` from `https://grouplens.org/datasets/movielens`
```
wget https://grouplens.org/datasets/movielens/ml-latest-small.zip
unzip ml-latest-small.zip
```

### Stage 1
Input: `data/ratings.csv` via `stdin`
Output: Sequence of tuples `(movieId, rating)` for all users

### Stage 2
Input: Output of `Stage 1`
Output: Increasing order of sequence of inverse tuples `(rating, movieId)`

## Run with Hadoop Streaming App/YARN on Azure HDInsight Cluster
Steps to follow: https://github.com/MicrosoftDocs/azure-docs/blob/981f98cd0fd7ac267142f3d43836cbc275805f5e/articles/hdinsight/hdinsight-hadoop-streaming-python.md
Stage1: `STAGEID=1 yarn hadoop-streaming.jar -files mapper_stage$STAGEID.py,reducer_stage$STAGEID.py -mapper mapper_stage$STAGEID.py -reducer reducer_stage$STAGEID.py -input data/ratings.csv -output data/avg_rating`
Stage2: `STAGEID=2 yarn hadoop-streaming.jar -files mapper_stage$STAGEID.py,reducer_stage$STAGEID.py -mapper mapper_stage$STAGEID.py -reducer reducer_stage$STAGEID.py -input data/avg_rating -output data/sort_rating`
