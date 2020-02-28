./process_iperf_output.sh server_output_raw
./process_cpu_utilisation_output.sh iperf iperf
./process_cpu_utilisation_output.sh irq ksoftirqd
mv iperf/*.png .
mv irq/*.png .
mkdir plots
mv *.png plots