compile:
	gcc node.c -o noded
run_test: compile
	./noded &
	python3 client.py

run_server:
	./noded &

run_client:
	python3 client.py