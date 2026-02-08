import dask.dataframe as dd

def detect_anomaly(log_df, z_threshold=3):
    """
    Detects anomalies in log data based on Z-score method.

    Parameters:
    - log_df: Dask DataFrame with log data containing
              'timestamp' and 'level' columns.
    - z_threshold: Z-score threshold to flag anomalies.

    Returns:
    - Dask DataFrame with anomalies flagged.
    """

    # Filter ERROR logs
    error_logs = log_df[log_df["level"] == "ERROR"]

    # Count errors per minute
    error_counts = (
        error_logs
        .set_index("timestamp")
        .resample("1T")            # 1-minute intervals
        .size()
        .rename("error_count")
        .reset_index()
    )

    # Calculate mean and standard deviation
    mean = error_counts["error_count"].mean().compute()
    std_dev = error_counts["error_count"].std().compute()

    # Calculate Z-score
    error_counts["z_score"] = (
        (error_counts["error_count"] - mean) / std_dev
    )

    # Flag anomalies
    error_counts["is_anomaly"] = (
        error_counts["z_score"].abs() > z_threshold
    )

    # Return only anomalous rows
    return error_counts[error_counts["is_anomaly"]]


# Example log columns:
# log_df = ["timestamp", "level", "service", "message"]

# Example note:
# service = auth
# time = 19:17:45 pm
# error count = 10