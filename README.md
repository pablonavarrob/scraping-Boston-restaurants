# Scraping agent of Boston Restaurants 

Web scraping agent using scraPy to find all the restaurants in Boston as given by the website TripAdvisor. Part of a larger project for the Hertfordshire Master. 

I add three extra files for the pre-processing of the data to, mainly, solve parsing issues:
- *scraped_preprocessing.py*: geolocates the restaurants given their scraped address for future plotting on a map.
- *data_cleaning.py* : parsing of the columns that might have incorrect names or missing/extra characters. 
- *geolocate.py* : contains the function used by *scraped_preprocessing.py* to geolocate the restaurants

Within the *review_restaurants/* directory there are four different agents, one that crawls in search of every restaurants and three that filter by class (can be used as a template for other classes). The agents utilize a mixture of XPATH and CSS selectors to find the information. Please bear in mind that TripAdvisor changes its tags frequently and the selectors may need to be rewritten. 

The *stettings.py* file is alread set-up to read and function according to the *robots.txt* file to avoid any problems.

### Data

I added some of the data I gathered in case the crawlers don't work anymore because of faulty selectors, feel free to use. I included polygon data as a *.geojson* file for the plotting of the restaurants with Python (density areas in the plot were obtained as a Gaussian Kernel Density Estimation)

<br>
<img src="https://github.com/pablonavarrob/scraping-Boston-restaurants/blob/main/geo_kde_plot.png" >
