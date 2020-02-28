top -b -n 20 > cpu_monitor_${1}_${2} &
taskset -c 2 iperf -s -u -B 224.0.70.71 -l $1 -i 1 > server_output_3clients_${1}_${2} -y C &
../remote-multicast-executor/client.py iperf -c 224.0.70.71 -b $2 -u -l $1
sleep 11
pkill iperf
pkill top
