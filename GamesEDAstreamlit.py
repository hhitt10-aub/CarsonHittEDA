import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

#Set up page and write intro
st.set_page_config(page_title="INSY6500 Steam Games Streamlit")
st.title("Steam Games EDA")
st.write("This streamlit contains analysis of scrapped data from Steam from 1997 to 2024")


#get data frame
games = pd.read_pickle("export/games_cleaned_added_features.pkl")

st.write(f"There are {games.index.value_counts().sum()} unique game IDs")
st.write(f"The dates Range from {games['release_date'].min()} to {games['release_date'].max()}")

st.write(f'The data contains the follow columns:')
st.write(games.columns)


# creat selection box for either graphs or tables
graphic = st.selectbox("Select Desired Graphic", options=["Graphs", "Tables"])

# make graphs
if graphic == "Graphs":
    #create dropdown boxes for graphs
    x_col = st.selectbox("Select Desired X Axis", options=["Years", "Operating System", "Languages", "Developers Are Publishers"])
    y_col = st.selectbox("Select Desired Y Axis", options=["Count", "Price", "Peak CCU", "Percent Positive"])
    #create year graphs
    if x_col == "Years":
        fig, axes = plt.subplots()
        if y_col == "Count":
            release_year_freq = (games['release_date']
                            .dt.year
                            .value_counts().sort_index())
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

# create tables
if graphic == "Tables":
    #create dropdown boxes
    x_col = st.selectbox("Select Desired Index", options=["Years", "Operating System", "Languages", "Developers Are Publishers"])
    y_col = st.selectbox("Select Desired Columns", options=[ "Price", "Peak CCU", "Percent Positive"])

    #create year tables for years
    if x_col == "Years":
        if y_col == "Count":
            release_year_freq = (games['release_date']
                            .dt.year
                            .value_counts().sort_index())
            st.write(release_year_freq)
        if y_col == "Price":
            # Group by year, aggregate price average
            avg_price_by_year = (games.groupby('release_year', observed=False)[['price']]
                                .agg({"price":["describe"]})
                                .sort_index())
            st.write(avg_price_by_year)
        if y_col == "Peak CCU":
            avg_peak_ccu_by_year = (games.groupby('release_year', observed=False)[['peak_ccu']]
            .agg({"peak_ccu":["describe"]}).sort_index())
            st.write(avg_peak_ccu_by_year)

        if y_col == "Percent Positive":
            #get yearly avg percent positive
            avg_percent_positive_by_year = (games.groupby('release_year', observed=False)[['percent_positive']]
                                .agg({"percent_positive":["describe"]})
                                .sort_index())
            st.write(avg_percent_positive_by_year)


    #create operating system tables
    if x_col == "Operating System":
        
        
        op_sys = ["windows", "mac", "linux"]
        if y_col == "Count":
            op_count = games[op_sys].sum().sort_index()
            st.write(op_count)
                  
        if y_col == "Price":
            # Plot average price by Operating System
            op_prices = (games.groupby(op_sys, observed=False)[['price']]
                                .agg({"price":["describe"]}))
            st.write(op_prices)


        if y_col == "Peak CCU":
            # Plot average peak_ccu by Operating System
            op_ccu = (games.groupby(op_sys, observed=False)[['peak_ccu']]
                                .agg({"peak_ccu":["describe"]}))
            st.write(op_ccu)
            
        if y_col == "Percent Positive":
            # Plot average percent positive review by Operating System
            op_pospct = (games.groupby(op_sys, observed=False)[['percent_positive']]
                                .agg({"percent_positive":["describe"]}))
            st.write(op_pospct)
            
    #create language tables
    if x_col == "Languages":
        
        lang = ["English","Chinese", "Japanese", "Spanish", "German", "French", "Russian"]

        if y_col == "Count":
            lang_count = games[lang].sum().sort_index()
            st.write(lang_count)
        
        if y_col == "Price":
            # Plot average price by language
            lang_prices = (games.groupby(lang, observed=False)[['price']]
                                .agg({"price":["describe"]}))
            st.write(lang_prices)
            
        if y_col == "Peak CCU":
            # Plot average peak_ccu by language
            lang_ccu = (games.groupby(lang, observed=False)[['peak_ccu']]
                                .agg({"peak_ccu":["describe"]}))
            st.write(lang_ccu)
            
        if y_col == "Percent Positive":
            # Plot average percent positive review by language
            lang_pospct = (games.groupby(lang, observed=False)[['percent_positive']]
                                .agg({"percent_positive":["describe"]}))
            st.write(lang_pospct)
            

    #create developers are publishers tables
    if x_col == "Developers Are Publishers":
        if y_col == "Count":
            release_dev_pub_freq = (games['dev_pub'].value_counts().sort_index())
            # generated table
            st.write(release_dev_pub_freq)

        if y_col == "Price":
            # Group by year, aggregate price average
            avg_price_by_dev_pub = (games.groupby('dev_pub', observed=False)[['price']]
                                .agg({"price": "describe"})
                                .sort_index())
            st.write(avg_price_by_dev_pub)

        if y_col == "Peak CCU":
            avg_peak_ccu_by_dev_pub = (games.groupby('dev_pub', observed=False)[['peak_ccu']]
                                .agg({"peak_ccu": "describe"})
                                .sort_index())
            st.write(avg_peak_ccu_by_dev_pub)
    
        if y_col == "Percent Positive":    
            avg_percent_positive_by_dev_pub = (games.groupby('dev_pub', observed=False)[['percent_positive']]
                                .agg({"percent_positive": "describe"})
                                .sort_index())
            st.write(avg_percent_positive_by_dev_pub)


