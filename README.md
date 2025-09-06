# Performance Evaluation Assignment

This repository collects solutions and tooling for the first homework of the *Performance Evaluation* course. The original specification can be found at [ocw.cs.pub.ro/courses/ep/teme/01](https://ocw.cs.pub.ro/courses/ep/teme/01).

The goal of the assignment is to analyse TCP behaviour in a Mininet topology, gather kernel metrics through the `socket_diag` interface and visualise the results.

## Requirements

The experiments assume a Linux host with root privileges and the following software installed:

- [Mininet](https://github.com/mininet/mininet)
- [iperf3](https://iperf.fr/)
- GCC and make (for building `socket_diag.c`)
- Python 3 with `pandas` and `matplotlib`

## Repository layout

| File/Directory       | Description |
|----------------------|-------------|
| `run_experiments.sh` | Launches Mininet and performs bandwidth and delay experiments.
| `clear_csv.sh`       | Cleans raw CSV files and stores processed data under `cleaned/`.
| `socket_diag.c`      | Collects TCP metrics (RTT, cwnd, delivery rate, etc.) via Netlink and writes them to a CSV file.
| `task_1_plots.py`    | Plots bitrate for the introductory throughput experiments.
| `task_2_plots.py`    | Visualises metrics from a single TCP flow stored in `tcp_stats.csv`.
| `task_3_plots.py`    | Compares metrics across experiments stored in `cleaned/`.
| `task_4_plots.py`    | Compares TCP vs. UDP throughput for the additional scenario.

## Running the experiments

1. **Collect measurements**

   ```bash
   sudo ./run_experiments.sh
   ```

   The script produces CSV files under `results/bw/` and `results/delay/` containing per–second TCP statistics for a series of bandwidth (20–40 Mbps) and delay (25–75 ms) settings.

2. **Clean the data**

   ```bash
   ./clear_csv.sh
   ```

   Deduplicated files are written to `cleaned/` preserving the directory hierarchy from `results/`.

3. **Generate plots**

   ```bash
   python3 task_1_plots.py   # task 1 graphs
   python3 task_2_plots.py   # per-metric plots for tcp_stats.csv
   python3 task_3_plots.py   # comparison across experiments
   python3 task_4_plots.py   # additional TCP/UDP comparison
   ```

## Assignment tasks

The assignment from the course requires:

1. **Throughput analysis** – Measure TCP throughput with and without competing UDP traffic using Mininet and iperf3.
2. **Socket diagnostics** – Implement a Netlink-based tool (`socket_diag.c`) that records RTT, congestion window, send window, bytes sent and delivery rate for an active TCP connection.
3. **Impact of bandwidth and delay** – Run experiments over multiple bandwidth and latency configurations and study how the collected metrics change.
4. **Cross-traffic comparison** – Evaluate the behaviour of TCP and UDP flows when they share the same link.

Refer to the [official assignment statement](https://ocw.cs.pub.ro/courses/ep/teme/01) for complete requirements and grading details.

