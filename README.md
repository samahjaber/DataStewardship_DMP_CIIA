# DataStewardship_DMP
Country Innovation Index Analysis


The purpose of this project is to gain insights with regard to the following research questions:

1-	What common drivers behind countries improving or deteriorating substantially with regard to their innovation levels may be identified?

2-	 In what manner are the innovation indices as well as their underlying drivers correlated? 

3-	Are innovation indices published by an official EU organization biased in a way that they rather favor European countries?


The data of interest is a collection of data from four different sources (all datasets are useable free of charge for non-commercial purposes):


•	Global Innovation Index (GII):  2013 – 2021 (Main Source)

•	Bloomberg Innovation Index (BII):  2016 – 2021 (Alternative Source for comparison)

•	European Innovation Scoreboard (EIS):  2014 – 2021 (Alternative Source for comparison)

•	OECD Business Innovation Statistics:  2013 – 2019 (Alternative Source for comparison)


The data mainly includes information about the factors that determine innovation; such as political environment, business environment, education and research, Information and communication technologies.

Then, all datasets have been merged and preprocessed. Initially standardized for consistency with regard to data types, indexes, naming conventions as well as column groups before merging them altogether in one dataset for coherent querying later on.
The original datasets are saved as csv files in folders (./data/gii), (./data/oecd), (./data/bii) and (./data/eis), where the merged and preprocessed dataset is saved in (./OUTPUT.csv). 

Interactive plots will be produced for Exploratory Data Analysis, radar plot for average innovation leaders and laggards and other visual representations will be showing drivers behind top 10 innovation “Leaders” and factors contributing to bottom 10 innovation “Laggards”.

