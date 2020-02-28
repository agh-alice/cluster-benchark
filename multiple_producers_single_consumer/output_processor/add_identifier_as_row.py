import os


files = [file for file in os.listdir() if os.path.isfile(os.path.join(os.getcwd(), file))]
for file_name in files:
    fragments = file_name.split("_")
    if len(fragments) == 5:
        (_, _, clients_number, datagram_size, bandwidth) = file_name.split("_")
        with open(file_name) as source_handler:
            with open(file_name+"_", "w") as destiny_handler:
                title_line = clients_number + "," + datagram_size + "," + bandwidth + "\n"
                destiny_handler.write(title_line)
                destiny_handler.write(source_handler.read())
