import matplotlib.pyplot as plt

# Data extracted manually from images provided

# TCP Bitrate from second experiment in Task 1
tcp_task1_times = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tcp_task1_bitrate = [1.05, 8.40, 9.45, 5.04, 4.95, 0.00, 0.00, 0.00, 5.82, 7.28]

# TCP Bitrate from experiment in Task 4
tcp_task4_times = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tcp_task4_bitrate = [4.58, 17.3, 14.1, 10.8, 9.89, 10.5, 10.5, 10.5, 10.5, 10.5]

# UDP Bitrate from second experiment in Task 1
udp_task1_bitrate = [1.03, 9.38, 9.80, 9.40, 10.1, 10.0, 9.82, 9.58, 9.38, 9.35]

# UDP Bitrate from experiment in Task 4
udp_task4_bitrate = [6.83, 7.88, 8.63, 9.57, 9.57, 9.57, 9.57, 9.57, 4.78, 4.76]

# Plotting
plt.figure(figsize=(12, 6))

# TCP Comparison
plt.subplot(1, 2, 1)
plt.plot(tcp_task1_times, tcp_task1_bitrate, label='TCP Task 1.2', marker='o')
plt.plot(tcp_task4_times, tcp_task4_bitrate, label='TCP Task 4', marker='s')
plt.title('TCP Bitrate Comparison')
plt.xlabel('Time (s)')
plt.ylabel('Bitrate (Mbits/sec)')
plt.legend()
plt.grid(True)

# UDP Comparison
plt.subplot(1, 2, 2)
plt.plot(tcp_task1_times, udp_task1_bitrate, label='UDP Task 1.2', marker='o')
plt.plot(tcp_task4_times, udp_task4_bitrate, label='UDP Task 4', marker='s')
plt.title('UDP Bitrate Comparison')
plt.xlabel('Time (s)')
plt.ylabel('Bitrate (Mbits/sec)')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
