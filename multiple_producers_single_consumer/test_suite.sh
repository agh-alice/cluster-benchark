# arguments:
# $1- file with datagram sizes
# $2- file with bandwidth to test
while read bandwidth;
do
    while read datagram_size;
    do
        ./unit_test.sh $datagram_size $bandwidth
    done <$1
done <$2