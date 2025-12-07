import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from EDAsettup import read_games, year_bar

#Set up page and write intro
st.set_page_config(page_title="INSY6500 Steam Games Streamlit")
st.title("Steam Games EDA")
st.write("This streamlit contains analysis of scrapped data from steam during 1997 to 2024")
st.write("""
""")

#get data frame
games = read_games()

#create dropdown boxes
x_col = st.selectbox("Select Desired X Axis", options=["Years", "Operating System", "Languages", "Developers Are Publishers"])
y_col = st.selectbox("Select Desired Y Axis", options=["Count", "Price", "Peak CCU", "Percent Positive"])

#create year graphs
if x_col == "Years":
    fig, axes = plt.subplots()
    if y_col == "Count":
        release_year_freq = (games['release_date']
                        .dt.year
                        .value_counts())
        # Plot the release year frequency using Pandas
        release_year_freq.sort_index().plot(kind='bar', 
                                            title="Release Year Frequency", 
                                            logy=True, xlabel='Release Year', 
                                            ylabel='Number of Games Released')
        plt.show()
    if y_col == "Price":
        # Group by year, aggregate price average
        avg_price_by_year = (games.groupby('release_year', observed=False)['price']
                            .mean()
                            .sort_index())
        # Plot the results using a bar graph
        avg_price_by_year.plot(kind='bar', 
                            title="Average Yearly Game Price", 
                            xlabel='Release Year', 
                            ylabel='Average Game Price (USD)',
                            rot=90.0)
    if y_col == "Peak CCU":
        avg_peak_ccu_by_year = (games.groupby('release_year', observed=False)['peak_ccu']
                            .mean()
                            .sort_index())

        # Plot the results using a bar graph
        avg_peak_ccu_by_year.plot(kind='bar', 
                            title="Average Yearly Game Peak CCU", 
                            xlabel='Release Year', 
                            ylabel='Average Game Peak CCU',
                            logy=True,
                            rot=90.0)
    if y_col == "Percent Positive":
        #get yearly avg percent positive
        avg_percent_positive_by_year = (games.groupby('release_year', observed=False)['percent_positive']
                            .mean()
                            .sort_index())

        # Plot the results using a bar graph
        avg_percent_positive_by_year.plot(kind='bar', 
                            title="Average Yearly Game Percent Positive", 
                            xlabel='Release Year', 
                            ylabel='Average Game Percentage Positive',
                            rot=90.0)
    st.write(fig)

#create operating system graphs
if x_col == "Operating System":
    fig, axes = plt.subplots()
    # Plot game counts by Operating System
    op_sys = ["windows", "mac", "linux"]
    op_counts = games[op_sys].sum()
    if y_col == "Count":
        axes.bar(x=op_sys, height=op_counts)
        axes.set_xticks(range(len(op_sys)))
        axes.set_xticklabels(labels=op_sys)
        axes.set_title("Numb of Game for each Operating System")
        axes.set_xlabel("Operating Systems")
        axes.set_ylabel("Number of Games")
    if y_col == "Price":
        # Plot average price by Operating System
        average_prices = [games["price"].loc[games[x] == True].mean() for x in op_sys]
        axes.bar(x=op_sys, height=average_prices)
        axes.set_xticks(range(len(op_sys)))
        axes.set_xticklabels(labels=op_sys)
        axes.set_title("Average Price For Games Per Operating System")
        axes.set_xlabel("Operating Systems")
        axes.set_ylabel("Price (USD)")
    if y_col == "Peak CCU":
        # Plot average peak_ccu by Operating System
        average_ccu = [games["peak_ccu"].loc[games[x] == True].mean() for x in op_sys]
        axes.bar(x=op_sys, height=average_ccu)
        axes.set_xticks(range(len(op_sys)))
        axes.set_xticklabels(labels=op_sys)
        axes.set_title("Average Peak CCU Per Operating System")
        axes.set_xlabel("Operating Systems")
        axes.set_ylabel("Peak CCU")
    if y_col == "Percent Positive":
        # Plot average percent positive review by Operating System
        average_pospct = [games["percent_positive"].loc[games[x] == True].mean() for x in op_sys]
        axes.bar(x=op_sys, height=average_pospct)
        axes.set_xticks(range(len(op_sys)))
        axes.set_xticklabels(labels=op_sys)
        axes.set_title("Average % Positive Review Per Operating System")
        axes.set_xlabel("Operating Systems")
        axes.set_ylabel("Percent Positive")
    st.write(fig)

#create language graphs
if x_col == "Languages":
    fig, axes = plt.subplots()
    # Plot game counts by language
    lang = ["English","Chinese", "Japanese", "Spanish", "German", "French", "Russian"]
    lang_counts = games[lang].sum()
    if y_col == "Count":
        axes.bar(x=lang, height=lang_counts)
        axes.set_xticks(range(len(lang)))
        axes.set_xticklabels(labels=lang, rotation=90.0)
        axes.set_title("Number of Games Supported")
        axes.set_xlabel("Languages")
        axes.set_ylabel("Number of Games")
    if y_col == "Price":
        # Plot average price by language
        average_prices = [games["price"].loc[games[x] == True].mean() for x in lang]
        axes.bar(x=lang, height=average_prices)
        axes.set_xticks(range(len(lang)))
        axes.set_xticklabels(labels=lang, rotation=90.0)
        axes.set_title("Average Price Per Language")
        axes.set_xlabel("Languages")
        axes.set_ylabel("Price (USD)")
    if y_col == "Peak CCU":
        # Plot average peak_ccu by language
        average_ccu = [games["peak_ccu"].loc[games[x] == True].mean() for x in lang]
        axes.bar(x=lang, height=average_ccu)
        axes.set_xticks(range(len(lang)))
        axes.set_xticklabels(labels=lang, rotation=90.0)
        axes.set_title("Average Peak CCU Per Language")
        axes.set_xlabel("Languages")
        axes.set_ylabel("Peak CCU")
    if y_col == "Percent Positive":
        # Plot average percent positive review by language
        average_pospct = [games["percent_positive"].loc[games[x] == True].mean() for x in lang]
        axes.bar(x=lang, height=average_pospct)
        axes.set_xticks(range(len(lang)))
        axes.set_xticklabels(labels=lang, rotation=90.0)
        axes.set_title("Average % Positive Review Per Language")
        axes.set_xlabel("Languages")
        axes.set_ylabel("Percent Positive")
    st.write(fig)

#create developers are publishers graphs
if x_col == "Developers Are Publishers":
    fig, axes = plt.subplots()
    if y_col == "Count":
        release_dev_pub_freq = (games['dev_pub'].value_counts().sort_index())
        # Plot the count
        release_dev_pub_freq.plot(kind='bar',
                               title="Release Frequency of Games", 
                               logy=True, xlabel='If Developers are Publishers',
                               ylabel='Number of Games Released')
        plt.show()
    if y_col == "Price":
        # Group by year, aggregate price average
        avg_price_by_dev_pub = (games.groupby('dev_pub', observed=False)['price']
                            .mean()
                            .sort_index())
        # Plot the results using a bar graph
        avg_price_by_dev_pub.plot(kind='bar', 
                            title="Average Game Price If Developers are Publishers", 
                            xlabel='If Developers are Publishers', 
                            ylabel='Average Game Price (USD)')
    if y_col == "Peak CCU":
        avg_peak_ccu_by_dev_pub = (games.groupby('dev_pub', observed=False)['peak_ccu']
                            .mean()
                            .sort_index())

        # Plot the results using a bar graph
        avg_peak_ccu_by_dev_pub.plot(kind='bar', 
                            title="Average Game Peak CCU If Developers are Publishers", 
                            xlabel='If Developers are Publishers', 
                            ylabel='Average Game Peak CCU',
                            logy=True)
    if y_col == "Percent Positive":
        avg_percent_positive_by_dev_pub = (games.groupby('dev_pub', observed=False)['percent_positive']
                            .mean()
                            .sort_index())

        # Plot the results using a bar graph
        avg_percent_positive_by_dev_pub.plot(kind='bar', 
                            title="Average Game Percent Positive If Developers are Publishers", 
                            xlabel='If Developers are Publishers', 
                            ylabel='Average Game Percentage Positive')
    st.write(fig)



