# ID generator

A Python module for generating unique IDs based on time and MAC adress 

## Getting Started

### Prerequisites
You need:  
* python 3.9.2
* any IDE capable of working with python


```bash
sudo apt-get update
sudo apt-get install python3

```

### Installing

1. open terminal with ctrl+alt+T
2. install python 3.9.2 or later:

	```bash
	sudo apt-get update
	sudo apt-get install python3

	```
3. install python IDE of your choice

### Running the tests

Open the terminal from IDGenerator directory and run:

	```bash
	python3 -m unittest tests/test__IDGen.py

	```

### Break down into end to end tests

	These tests check some methods in IDGen to ensure they work properly

```

```

###Deploy

1. create a new project and include IDmodule.py (from “source” directory of this package) in your project 
2. copy & paste the text bellow into .py file you wish to use with ID generator.

```
from source.IDmodule import IDGen
```
3. initialize a IDGen_object. You can call get_id() using set object. This method returns a newly generated ID. There are other methods in IDGen, but it is not recommended to use them

```
IDGen_object = IDGen()
ID = IDGen_object.get_id()
```

## Built With
	PyCharm by JetBrain

## Versioning

We use SemVer for versioning. For changelog see CHANGELOG.txt. 

## Authors

**Bugrov Svyatoslav** - *Initial work*
**Andrey Starchenkov** - *Supervision*

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

*my sanity


