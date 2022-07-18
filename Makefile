IDgenerator.py.tar: test
	# Creating tar
	tar -cf IDgenerator.py.tar source/IDmodule.py README.md LICENSE.md requirements.txt
	# Done

test:
	# Running tests
	python3 -m unittest tests/test__IDmodule.py
	# Done