#!/bin/python3
import os

def main():
    files = [file for file in os.listdir() if os.path.isfile(os.path.join(os.getcwd(), file))]
    for file_name in files:
        fragments = file_name.split("_")
        if len(fragments) == 5:
            (_, _, datagram_size, bandwidth, _) = file_name.split("_")
            with open(file_name) as source_handler:
                with open(file_name+"_", "w") as destiny_handler:
                    title_line = datagram_size + ";" + bandwidth + "\n"
                    destiny_handler.write(title_line)
                    source_file_content = source_handler.read()
                    monitored_process = get_number_of_monitored_process(source_file_content)
                    for line in source_file_content.split("\n"):
                        if len(line) != 0:
                            line_map = split_line_to_map(line)
                            if line_map["process_number"] == monitored_process:
                                destiny_handler.write(line_map["cpu"] + "\n")


def split_line_to_map(line):
    fragments = list(filter(lambda sign: sign != "", line.split(" ")))
    return {
        "process_number": fragments[0],
        "cpu": fragments[8]
    }

def get_number_of_monitored_process(file_content):
    process_numbers = []
    for line in file_content.split("\n"):
        if len(line) != 0:
            line_map = split_line_to_map(line)
            process_numbers.append(line_map["process_number"])
    
    process_counts = {}
    for process_number in process_numbers:
        if process_number in process_counts:
            process_counts[process_number] += 1
        else:
            process_counts[process_number] = 1

    sorted_processed = sorted(process_counts.items(), key=lambda kv:(kv[1], kv[0]), reverse=True)
    monitored_process = sorted_processed[0][0]
    return monitored_process

main()