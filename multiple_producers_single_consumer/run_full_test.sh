
./test_suite.sh $1 $2
mkdir test_output
mv server_output* test_output
mv cpu_monitor_* test_output
cp output_processor/* test_output/
cd test_output
./process_output.sh
