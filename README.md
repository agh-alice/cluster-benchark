# cluster-benchark
Some scripts to test UDP performance. Base on iperf.
## How to use
### Consumers
On consumer nodes compile and run noded
```
cd remote-multicast-executor
make compile
./noded &
```

### Producer
You can start this part after running on consumers nodes program `noded`   
To start on consumer nodes `iperf -c`
```
./run_parallel_consumer datagram_size result_file_name number_of_threads output_format
```
Above line run on every consumer node `number_of_threads` processes of `iperf -c`. Every use anther port from 5200.   
Start test:
```
./run_parallel_sender bandwidth_of_single_thread datagram_size number_of_threads
```
After test consumers have to be closed. To do so:
```
./close_consumers
```
To merge output files to one run:
```
./harvester result_file_name
```
Use `result_file_name` like in first command
