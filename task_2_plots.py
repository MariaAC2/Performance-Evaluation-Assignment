import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
df = pd.read_csv("tcp_stats.csv")

# Metrics chosen for plotting
metrics = {
    "rtt_us": "RTT (µs)",
    "rttvar_us": "RTT Variance (µs)",
    "cwnd": "Congestion Window (segments)",
    "snd_wnd": "Send Window (bytes)",
    "bytes_sent": "Bytes Sent",
    "delivery_rate_bps": "Delivery Rate (Bps)"
}

# Create 2x3 subplots
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(20, 8))
axes = axes.flatten()

# Plot each metric
for idx, (metric, label) in enumerate(metrics.items()):
    ax = axes[idx]
    ax.plot(df["second"].to_numpy(), df[metric].to_numpy(), marker='o')
    ax.set_title(label)
    ax.set_xlabel("Time (seconds)")
    ax.set_ylabel(label)
    ax.grid(True)

# Adjust layout
plt.tight_layout()
plt.show()
