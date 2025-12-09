# Steam Games EDA

## Data

The data is scrapped data from Steam's API sourced from Keggle and uses the 2024 dataset that has dupiclates and playtest versions of games removed.

Source: https://www.kaggle.com/datasets/artermiloff/steam-games-dataset

## Questions

1. How does the number of games added to Steam, average price, average peak concurrent users, and average percent positive varies by year?
2. How many games support different operating systems and how does each operating system impact average price of games, average peak concurrent users, and average percent positive?
3. How many games support the following languages: English, Chinese, Japanese, Spanish, German, French, and Russian. What is the average price, average peak concurrent users, and average percent positive for each supported language.
4. How many games are made developers that are also the publishers and does that cause a difference in average price, average peak concurrent users, and average percent positive? 

## Files and Folders

1. SteamGamesEDA: Most of our analysis is performed in this file
2. GamesEDAstreamlit.py: Code used to create the streamlit
3. EDAsettup.py: Legacy code that was used for the streamlit
4. datasets Folder: Contains the zip files for the original data
5. exports Folder: Contains the exported CSV and pickle files of the altered data
6. profiles Folder: Contains the environment yaml file and the ruff toml file
