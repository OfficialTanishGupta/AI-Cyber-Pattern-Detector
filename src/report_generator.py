from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak

from reportlab.lib.styles import getSampleStyleSheet

import pandas as pd
import os


def generate_report():

    log_file = "../outputs/live_monitor_log.csv"

    if not os.path.exists(log_file):

        return None

    df = pd.read_csv(log_file)

    if len(df) == 0:

        return None

    report_path = "../outputs/threat_report.pdf"

    doc = SimpleDocTemplate(report_path)

    styles = getSampleStyleSheet()

    elements = []

    elements.append(Paragraph("AI Cyber Threat Intelligence Report", styles["Title"]))

    elements.append(Spacer(1, 20))

    total_packets = len(df)

    threats = df["status"].astype(str).str.contains("THREAT").sum()

    normal = total_packets - threats

    threat_percentage = (threats / max(total_packets, 1)) * 100

    stats_text = f"""
    <b>Total Packets:</b> {total_packets}<br/>
    <b>Threats:</b> {threats}<br/>
    <b>Normal Traffic:</b> {normal}<br/>
    <b>Threat Percentage:</b> {threat_percentage:.2f}%<br/>
    """

    elements.append(Paragraph(stats_text, styles["BodyText"]))

    elements.append(Spacer(1, 20))

    elements.append(Paragraph("Top Source IPs", styles["Heading2"]))

    top_sources = df["src_ip"].value_counts().head(10)

    for ip, count in top_sources.items():

        elements.append(Paragraph(f"{ip} : {count}", styles["BodyText"]))

    elements.append(Spacer(1, 20))

    elements.append(Paragraph("Top Destination IPs", styles["Heading2"]))

    top_targets = df["dst_ip"].value_counts().head(10)

    for ip, count in top_targets.items():

        elements.append(Paragraph(f"{ip} : {count}", styles["BodyText"]))

    elements.append(PageBreak())

    elements.append(Paragraph("Recent Threat Activity", styles["Heading1"]))

    threat_df = df[df["status"] == "THREAT"]

    recent = threat_df.tail(25)

    for _, row in recent.iterrows():

        text = (
            f"{row['timestamp']} | "
            f"{row['src_ip']} -> "
            f"{row['dst_ip']} | "
            f"Score={row['error']}"
        )

        elements.append(Paragraph(text, styles["BodyText"]))

    doc.build(elements)

    return report_path
