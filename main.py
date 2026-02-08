import dask.dataframe as df
from config.dask_config import start_dask
from ingestion.loader import load_logs
from ingestion.parser import parse_log_line
from processing.pipeline import build_pipeline
import time
import dask.dataframe as df
from anamoly.detector import detect_anomaly
from config.email_config import send_email
user_email="pklakshmi894@gmail.com"
def main():
    client = start_dask()
    print(client)
    print(f"Dashboard link: {client.dashboard_link}")
    print("\n" + "-" * 50)

    start=time.time()
    log_df=build_pipeline(r"data/sample_log.log")
    print("start time:",start)

    total_logs=log_df.count().compute()
    end=time.time()
    print("running anomoly detection...")
    anamolies=detect_anamoly(log_df)
    anomalies =anamolies_df.compute()

    if anamolies.empty:
        print("no anamolies detected")
    else:
        print(f"{len(anamolies)}anamolies detected!")

    for _, anamoly in anamolies.iterrows():
        anamoly_data= {
            "timestamp":row["timestamp"],
            "error_count":row["error_count"],
            "z_score":row["z_score"]
        }
send_email ( 
    to_mail=user_mail,
    anamoly=anamoly_data
        

)

print("alert sent!")

print("total log parsed:")
print(total_logs)
print("time taken:",end_time-start_time)
input("press enter to exit..") 

if __name__ == "__main__":
    main()