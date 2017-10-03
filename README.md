# PosterMatch!

The app PosterMatch! hosted on www.moviematch.life was built in 3 weeks as an Insight Data Science project.
It is aimed to help designers during the creation process of movie posters by:
  1. Matching posters according to their image design, in order to help make comparable posters or differentiate them, and ensure posters satisfies genre/time period designs.
  2. Matching posters according to their written synopsis which helps visualizing existing posters of similar movies.

### Piece of codes used to create the app can be found in this repository:

  - CreateFillTableDB.ipynb: This code creates a PostgreSQL database and define a table, in which are stored movie information taken from themoviedb.org API, such as movie poster image link, synopsis, genre, production countries, etc...
  - ProcessImageAndSynopsis.ipynb: This code processes poster images from links in the database through the pretained VGG16 deep neural network. 4096 features are extracted from the second-to-last layer (fully connected "fc2") and stored in the database. Similarly, every words of each movie synopsis are processed through a pretrained Word2Vec Google News neural network. Words that occur in similar contexts have similar embeddings, and are represented in a 300 dimensional space. These 300 features are stored in the database.
  - tSNE_Visualization.ipynb: This code is used to qualitatively assess that similar images have similar embeddings. The visualization of movie posters in a 2-dimensional space, is performed by using a t-distributed stochastic neighbor embedding (t-SNE) algorithm. A k-means clustering algorithm is also used to show images with similar features. Finally, in this code, as an example is presented how to visualize the most important features from an image, which can be used to better understand why poster images are in similar clusters.
  - ClosestNeighboorSynopsisPlusPoster.ipynb: This code is used to find nearest neighbors from both the image and text inserted by a user. The code first reduces the 4096 image features to 300 using a truncated single value decomposition algorithm (t-SVD). Features of both the image poster and written synopsis are then normalized using standard deviations and the mean of their distributions, before being concatenated. Finally, the 600 resulting features are used to find the nearest neighbors with a k-nearest neighbors algorithm.
