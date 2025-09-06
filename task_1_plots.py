import os
import matplotlib.pyplot as plt

# Time intervals
time_intervals = [i for i in range(1, 11)]

# TCP Bitrate values from first experiment
bitrates_tcp_old = [0.683, 7.88, 9.65, 9.56, 9.57, 9.58, 9.59, 9.57, 9.56, 9.54]

# TCP Bitrate values from second experiment
bitrates_tcp_new = [0.683, 7.88, 9.65, 9.57, 9.56, 9.58, 9.57, 9.57, 4.78, 2.75]

# UDP Bitrate values from second experiment
bitrates_udp = [1.19, 1.19, 1.68, 5.62, 9.35, 9.72, 9.72, 9.72, 9.72, 9.72]

# Create subplots
fig, axs = plt.subplots(1, 3, figsize=(12, 4))

# Subplot 1: TCP - First experiment
axs[0].plot(time_intervals, bitrates_tcp_old, marker='o', linestyle='-', color='green')
axs[0].set_title("TCP Bitrate Over Time - First Experiment")
axs[0].set_xlabel("Time (seconds)")
axs[0].set_ylabel("Bitrate (Mbits/sec)")
axs[0].grid(True)
axs[0].set_xticks(time_intervals)
axs[0].set_ylim(0, max(bitrates_tcp_old) + 2)

# Subplot 2: TCP and UDP - Second experiment
axs[1].plot(time_intervals, bitrates_tcp_new, marker='s', linestyle='--', label='TCP New (h3)', color='orange')
axs[1].plot(time_intervals, bitrates_udp, marker='^', linestyle='-.', label='UDP (h3)', color='blue')
axs[1].set_title("TCP and UDP Bitrate Over Time - Second Experiment")
axs[1].set_xlabel("Time (seconds)")
axs[1].set_ylabel("Bitrate (Mbits/sec)")
axs[1].grid(True)
axs[1].legend()
axs[1].set_xticks(time_intervals)
axs[1].set_ylim(0, max(bitrates_tcp_new + bitrates_udp) + 2)

# Subplot 3: Compare First experiment and Second experiment
axs[2].plot(time_intervals, bitrates_tcp_old, marker='o', linestyle='-', label='TCP Old (h3)', color='green')
axs[2].plot(time_intervals, bitrates_tcp_new, marker='s', linestyle='--', label='TCP New (h3)', color='orange')
axs[2].plot(time_intervals, bitrates_udp, marker='^', linestyle='-.', label='UDP (h3)', color='blue')
axs[2].set_title("TCP vs UDP Bitrate Over Time - Comparison")
axs[2].set_xlabel("Time (seconds)")
axs[2].set_ylabel("Bitrate (Mbits/sec)")
axs[2].grid(True)
axs[2].legend()
axs[2].set_xticks(time_intervals)
axs[2].set_ylim(0, max(bitrates_tcp_old + bitrates_tcp_new + bitrates_udp) + 2)

plt.tight_layout()
plt.show()
