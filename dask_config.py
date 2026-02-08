# To separate configuation from bussiness logice
# code is clean and easy for resuable

from dask.distributed import LocalCluster, Client

def start_dask():
    cluster = LocalCluster (
        n_workers=2,
        threads_per_worker= 1,
        memory_limit= "2gb",
        dashboard_address=":8787"
    )
    client= Client(cluster)
    return client
       # LocalCluster is a mini distributed cluser in your system, helps to run dask, as were running on mutiple systems.
    # n_workers = 2
    # threads_per_worker = 2

    # schedule
    # |
    # |
    # --- worker 1 (2 threads)
    # |
    # |
    # --- worker 2 ( 2 threads)
    #  memory limit="1GB"

    # client() is methods how python connects with dask cluster(connection between code and dask cluster)
    # send tasks to worker with the help of client and process easily.

    # LocalCluster -> create workers + schedule it
    # Client -> connect code with dask

    # LocalCluster -> Infrastructure
    # client -> Interface







    