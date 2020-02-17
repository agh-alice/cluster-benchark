compile:
	gcc node.c -o noded
run: compile
	./noded &
	python3 client.py