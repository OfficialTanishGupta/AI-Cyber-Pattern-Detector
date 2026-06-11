import pandas as pd
import os

LOG_FILE = "../outputs/live_monitor_log.csv"


def get_threat_intelligence():

    if not os.path.exists(LOG_FILE):
        return pd.DataFrame()

    df = pd.read_csv(LOG_FILE)

    if len(df) == 0:
        return pd.DataFrame()

    threats = (
        df[df["status"] == "THREAT"]
        .groupby("src_ip")
        .size()
        .reset_index(name="threat_count")
    )

    def risk_level(count):

        if count >= 500:
            return "HIGH"

        elif count >= 100:
            return "MEDIUM"

        else:
            return "LOW"

    threats["risk_level"] = threats["threat_count"].apply(risk_level)

    threats = threats.sort_values(by="threat_count", ascending=False)

    return threats
