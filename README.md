# PosterMatch!

The app PosterMatch! hosted on www.moviematch.life was built in 3 weeks as an Insight Data Science project.
It is aimed to help designers during the creation process of movie posters by:
  1. Matching posters according to their image design, in order to help make comparable posters or differentiate them, and ensure posters satisfies genre/time period designs.
  2. Matching posters according to their written synopsis which helps visualizing existing posters of similar movies.

### Piece of codes used to create the app are present on this github:

  - CreateFillTableDB.ipynb: This code creates a PostgreSQL database and define a table, in which are stored movie information taken from themoviedb.org API, such as movie poster image link, synopsis, genre, production countries, etc...
  - ProcessImageAndSynopsis.ipynb: This code processes poster images from links in the database through the pretained VGG16 deep neural network. 4096 features are extracted from the second-to-last layer (fully connected "fc2") and stored in the database. Similarly, every words of each movie synopsis are processed through a pretrained Word2Vec Google News neural network. Words that occur in similar contexts have similar embeddings, and are represented in a 300 dimensional space. The code stores these 300 features are stored in the database.
