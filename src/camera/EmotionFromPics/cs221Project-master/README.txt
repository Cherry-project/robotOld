Extracting Emotions from Faces:
Chelsea Lewis, Katie Redmond, Rohisha Adke

---------- Submitted Files ----------
1. baseline.py
    - All code used to run various classifiers with various feature extractors
2. fer.csv
    -Kaggle pixel data
3. jaffePixelData.txt
    -JAFFE pixel data

---------- How to run baseline.py from command line ----------

python baseline.py <data file name> <data type> <linear classifier> <feature extractor>

-- Data arguments ---
a) On Kaggle data
    <data file name> = fer.csv
    <data type> = kaggle
b) On Jaffe data
    <data file name> = jaffePixelData.txt
    <data type> = jaffe

--- linear classifier and feature extractor arguments ---
a) SGD and pixel list:
    <linear classifier> = sgd
    <feature extractor> = pl 
b) SGD and grid:
    <linear classifier> = sgd
    <feature extractor> = grid
c) K-Means and pixel list:
    <linear classifier> = kmeans
    <feature extractor> = pl
d) K-Means and grid:
    <linear classifier> = kmeans
    <feature extractor> = grid
e) K-Means and surf:
    <linear classifier> = kmeans
    <feature extractor> = surf
f) K-Means and sift:
    <linear classifier> = kmeans
    <feature extractor> = sift
g) K-Means and fast:
    <linear classifier> = kmeans
    <feature extractor> = fast
h) KNN and surf:
    <linear classifier> = knn
    <feature extractor> = surf
i) KNN and sift:
    <linear classifier> = knn
    <feature extractor> = sift
j) KNN and fast:
    <linear classifier> = knn
    <feature extractor> = fast


---- example ----
python baseline.py jaffePixelData.txt jaffe sgd grid
