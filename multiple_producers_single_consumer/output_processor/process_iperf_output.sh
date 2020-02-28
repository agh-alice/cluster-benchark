# Arguments:
# $1- path to directory with raw output from iperf. File names should be in convention: sth_sth_3clients_datagram_size_bandwidth
MY_PWD=`pwd`           # remember current position
cp add_identifier_as_row.py $1  # copy script to directory with raw files
cd $1                           # go to directory with raw files
python3 ./add_identifier_as_row.py   # create new file with indetifier inside each file and file name with "_" at the end
for i in ./*_
do
    cat $i >> server_output.csv     # merge all files
    rm $i
done
cd "$MY_PWD"
cp ${1}/server_output.csv .         # copy result file back
jupyter nbconvert --to notebook --execute iperf_result_process.ipynb       # generate plot

# Clean up
rm ${1}/add_identifier_as_row.py
rm iperf_result_process.nbconvert.ipynb
# rm server_output_m.csv