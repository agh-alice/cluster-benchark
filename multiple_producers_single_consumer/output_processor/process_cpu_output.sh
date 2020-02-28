mkdir iperf
for i in ./cpu_monitor_*
do
    cat $i | grep iperf > iperf/${i}_iperf
done

mkdir irq
for i in ./cpu_monitor_*
do
    cat $i | grep ksoftirqd/8 > irq/${i}_irq
done