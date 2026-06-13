import pandas as pd
import networkx as nx
from pyvis.network import Network
import os


def generate_network_graph():

    log_file = "../outputs/live_monitor_log.csv"

    if not os.path.exists(log_file):
        return None

    df = pd.read_csv(log_file)

    if len(df) == 0:
        return None

    graph = nx.DiGraph()

    threat_df = df[df["status"] == "THREAT"]

    if len(threat_df) == 0:
        return None

    for _, row in threat_df.iterrows():

        src = str(row["src_ip"])
        dst = str(row["dst_ip"])

        graph.add_node(src)
        graph.add_node(dst)

        graph.add_edge(src, dst)

    net = Network(
        height="750px",
        width="100%",
        bgcolor="#111111",
        font_color="white",
        directed=True,
    )

    net.from_nx(graph)

    output_file = "../outputs/network_graph.html"

    net.save_graph(output_file)

    return output_file
