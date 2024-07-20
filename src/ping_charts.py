import pandas as pd
import os
import plotly.express as px

outputfile_base = "ping_output"
outputfile = os.path.join(os.curdir, f"{outputfile_base}.csv")
outputfile_df = os.path.join(os.curdir, f"{outputfile_base}_df.csv")

def charts():

    ping_df = pd.read_csv(outputfile)
    ping_df.to_csv(outputfile_df)
    ping_df.reset_index(inplace = True, drop = True)
    
    
    chart = px.histogram(
        ping_df,
        x = "time",
        color = 'hostname',
        facet_row='return_status',
        title='Distribution of Pings'
    )
    chart.write_html( os.path.join(os.curdir, f"{outputfile_base}_hist.html"))

    chart = px.line(
        ping_df,
        x = "time",
        y = 'return_status',
        color = 'hostname',
        title='Scatter of Pings'
    )
    chart.write_html( os.path.join(os.curdir, f"{outputfile_base}_scatter.html"))


    ping_df.index = pd.to_datetime(ping_df['time'])
    # = 100 * (ping_df.groupby('return_status').resample('60min').count() / ping_df.resample('60min').count())
    ping_df_summarized = ping_df.groupby('return_status')[['return_status']].resample('60min').count()
    ping_df_summarized['pct'] = 100 * (ping_df.groupby('return_status')[['return_status']].resample('60min').count() / ping_df[['return_status']].resample('60min').count())
    #print(ping_df_summarized.columns)
    #print(ping_df_summarized.head())
    #ping_df_summarized['pct_sum'] = 100*ping_df_summarized['count']
    ping_df_summarized = ping_df_summarized.reset_index(level=[1])
    
    chart = px.bar(
        ping_df_summarized,
        x = 'time' ,
        y = 'pct',
        color = ping_df_summarized.index,
        title='Scatter of Pings'
    )
    chart.write_html( os.path.join(os.curdir, f"{outputfile_base}_bar.html"))


if __name__ == "__main__":
    charts()