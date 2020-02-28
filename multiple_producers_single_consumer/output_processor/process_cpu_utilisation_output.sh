# Arguments
# $1- folder with data name
# $2- process name
MY_PWD=`pwd`
cp iperf_cleaner.py ${1}/
cp plot_generator_cpu_util.py ${1}/
cd $1
./iperf_cleaner.py
for file in ./*_
do
    cat $file >> output.csv
done
./plot_generator_cpu_util.py output.csv $2
rm iperf_cleaner.py plot_generator_cpu_util.py *_ output.csv output_m.csv