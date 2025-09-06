import pandas as pd
import matplotlib.pyplot as plt
import os

# Base directory containing cleaned subfolders
base_dir = "cleaned"

# Metrics chosen for plotting
metrics = {
    "rtt_us": "RTT (µs)",
    "rttvar_us": "RTT Variance (µs)",
    "cwnd": "Congestion Window (segments)",
    "snd_wnd": "Send Window (bytes)",
    "bytes_sent": "Bytes Sent",
    "delivery_rate_bps": "Delivery Rate (Bps)"
}

# Load tcp_stats.csv
baseline_df = pd.read_csv("tcp_stats.csv")

# Go through each subdirectory in 'cleaned'
for subdir in sorted(os.listdir(base_dir)):
    input_dir = os.path.join(base_dir, subdir)
    if not os.path.isdir(input_dir):
        continue  # skip files

    print(f"\n Plotting for: {subdir}")

    # Load all CSVs from the subdir
    dataframes = {"tcp_stats": baseline_df}
    csv_files = sorted([
        f for f in os.listdir(input_dir) if f.endswith(".csv")
    ])

    for file in csv_files:
        df = pd.read_csv(os.path.join(input_dir, file))
        label = os.path.splitext(file)[0]
        dataframes[label] = df

    # Create subplots for this subdir
    fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(20, 8))
    axes = axes.flatten()

    for idx, (metric, label) in enumerate(metrics.items()):
        ax = axes[idx]
        for name, df in dataframes.items():
            color = 'black' if name == "tcp_stats" else None
            ax.plot(df["second"].to_numpy(), df[metric].to_numpy(), marker='o', label=name, color=color)
        ax.set_title(f"{label} over Time")
        ax.set_xlabel("Time (seconds)")
        ax.set_ylabel(label)
        ax.grid(True)
        ax.legend(title="Experiment")

    plt.suptitle(f"Comparison for {subdir}", fontsize=16)
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()
