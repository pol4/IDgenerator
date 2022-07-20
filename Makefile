all:
	echo -e "Sections:\n\
 clean - clean all addition file, build directory and output archive file\n\
 test - run all tests\n\
 pack - make output archive, IDgenerator.py.tar\n\
"

pack: test
	echo "Creating tar"
	tar -cf IDgenerator.py.tar IDgenerator/IDmodule.py README.md LICENSE.md requirements.txt
	echo "Done"

test:
	echo "Running tests"
	python3 -m unittest tests/test__IDmodule.py
	echo "Done"

clean:
	echo "Removing old tar"
	rm -rf ../IDGenerator
	echo "Done"