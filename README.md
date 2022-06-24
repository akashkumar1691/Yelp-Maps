# Yelp-Maps
a visualization of restaurant ratings using machine learning and the Yelp academic dataset
<div class="haiku">
  <p><img class="img-responsive center-block" src="voronoi.png" alt="voronoi"></p>
<h2 id="introduction">Introduction</h2>

<p> In this visualization, Berkeley is segmented into regions, where each region is shaded by the predicted rating of the closest restaurant (yellow is 5 stars, blue is 1 star). Specifically, the visualization is a <a href="https://en.wikipedia.org/wiki/Voronoi_diagram">Voronoi diagram</a>.</p>

<p>In the map above, each dot represents a restaurant. The color of the dot is
determined by the restaurant's location. For example, downtown restaurants are
colored green. The user that generated this map has a strong preference for
Southside restaurants, and so the southern regions are colored yellow.</p>

 <h2 id="running">Running the Code</h2>
  
  In terminal, run:
  ```
  python3 reccomend.py
  ```  
  ### Flags  
  ```
  python3 recommend.py -u likes_expensive -k 2 -p -q Sandwiches
 ```
  "-u" allows one to specify user  
  "-k" allows one to specify number of clusters    
  "-q" allows one to filter based on category  
  "-p" predicts user rating if user has not visited location  
