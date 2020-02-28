SERVER_OUTPUT_FOLDER="server_output_raw"
mkdir $SERVER_OUTPUT_FOLDER
cp server_output_3* $SERVER_OUTPUT_FOLDER
cd $SERVER_OUTPUT_FOLDER
for i in ./*
do 
    head -28 $i > ${i}_
    rm $i
    cat ${i}_ > $i
done