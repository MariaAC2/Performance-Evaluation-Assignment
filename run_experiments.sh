#!/bin/bash

# Create directories for results (if they don't exist)
mkdir -p results results/bw results/delay

# Kill process 6653
sudo fuser -k 6653/tcp

# Values for monitoring bandwidth and delay
BW_VALUES=(20 30 40)
DELAY_VALUES=(25ms 50ms 75ms)

# Default values for bandwidth and delay
DEFAULT_BW=10
DEFAULT_DELAY="100ms"

# Different bandwidths for h1-r1 and h2-r1
for BW in "${BW_VALUES[@]}"; do
    CSV_NAME="tcp_bw_${BW}.csv"

    echo "========================================="
    echo "Running bandwidth experiments for h1-r1 and h2-r1: ${BW}"
    echo "========================================="

    # Put bash content for mininet automatically
    sudo python3 topology.py \
      --bw-h1 $BW --delay-h1 $DEFAULT_DELAY \
      --bw-h2 $BW --delay-h2 $DEFAULT_DELAY <<EOF
h3 iperf3 -s -p 5201 &
h1 bash -c "sleep 2"
h1 iperf3 -c 10.0.2.101 -p 5201 -t 60 &
h1 bash -c "sleep 1"
h1 gcc socket_diag.c -o /tmp/socket_diag
h1 /tmp/socket_diag /proc/self/ns/net "results/bw/$CSV_NAME"
exit
EOF

    echo "Experiment completed: results/bw/$CSV_NAME"
    echo
done

# Different delays for h1-r1 and h2-r1
for DELAY in "${DELAY_VALUES[@]}"; do
    CSV_NAME="tcp_delay_${DELAY}.csv"

    echo "========================================="
    echo "Running delay experiments for h1-r1 and h2-r1: ${DELAY}"
    echo "========================================="

    # Put bash content for mininet automatically
    sudo python3 topology.py \
      --bw-h1 $DEFAULT_BW --delay-h1 $DELAY \
      --bw-h2 $DEFAULT_BW --delay-h2 $DELAY <<EOF
h3 iperf3 -s -p 5201 &
h1 bash -c "sleep 2"
h1 iperf3 -c 10.0.2.101 -p 5201 -t 60 &
h1 bash -c "sleep 1"
h1 gcc socket_diag.c -o /tmp/socket_diag
h1 /tmp/socket_diag /proc/self/ns/net "results/delay/$CSV_NAME"
exit
EOF

    echo "Experiment completed: results/delay_h1/$CSV_NAME"
    echo
done