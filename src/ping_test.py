from typing import List
import pandas as pd
import plotly.express as px
from typing import Optional
import os 
import time
import datetime

outputfile_base = "ping_output"
outputfile = os.path.join(os.curdir, f"{outputfile_base}.csv")
outputfile_df = os.path.join(os.curdir, f"{outputfile_base}_df.csv")

def main():
    if os.path.exists(path=outputfile):
        os.remove(outputfile)


    print(f"Testing Ping: ")
    with open(outputfile, "a") as f:
        cols = "time,hostname,return_status\n"
        f.write(cols)
        while(True):
            time.sleep(7)
            cur_time = datetime.datetime.now()
            cur_time = pd.to_datetime(cur_time)
            google_ret_status = check_ping("google.com")
            
            cur_values = f"{cur_time},google.com,{google_ret_status}\n"
            f.write(cur_values)
            time.sleep(3)
            f.flush()

    

def check_ping(hostname: str):
    hostname = hostname
    response = os.system("ping -n 1 " + hostname)
    # and then check the response...
    if response == 0:
        pingstatus = "Network Active"
    else:
        pingstatus = "Network Error"
    
    print(f"Checking Ping of {hostname}: result: {pingstatus}")
    return pingstatus


if __name__ == "__main__":
    main()