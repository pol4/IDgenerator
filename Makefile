all:
	echo -e "Sections:\n\
 clean - clean all addition file, build directory and output archive file\n\
 test - run all tests\n\
 pack - make output archive, IDgenerator.py.tar\n\
"

pack: test
	echo "Creating tar"
	tar -cf IDgenerator.py.tar IDgenerator/IDmodule.py IDgenerator_web/IDserver.py IDgenerator_web/url_mkr.py README.md LICENSE.md requirements.txt
	echo "Done"

test:
	echo "Running tests"
	python3 -m unittest tests/test__IDmodule.py
	python3 IDgenerator_web/IDserver.py 0.0.0.0 5000 &
	python3 -m unittest tests/test__IDserver.py
	kill "%python3"
clean:
	echo "Removing old tar"
	rm -rf IDgenerator.py.tar
	echo "Done"