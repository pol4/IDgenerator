# ID generator

A Python module for generating unique IDs based on time and MAC adress 

## Getting Started

### Prerequisites
You need:  
* python 3.9.2
* any IDE capable of working with python

### Installing

2. Install python 3.9.2 or later
3. Install python IDE of your choice

### Running the tests

Open the terminal from IDGenerator directory and run:

```
python3 -m unittest tests/test__IDGen.py
```

### Deploy

1. Create a new project and include IDmodule.py (from “source” directory of this package) in your project 
2. Copy & paste the text bellow into .py file you wish to use with ID generator.

```
from IDmodule import IDGen
```
3. Initialize an IDGen_object. You can call get_id() using set object. This method returns a newly generated ID. There are other methods in IDGen, but it is not recommended to use them

```
IDGen_object = IDGen()
ID = IDGen_object.get_id()
```

## Built With
	PyCharm by JetBrains

## Versioning

We use SemVer for versioning. For changelog see CHANGELOG.txt. 

## Authors

**Bugrov Svyatoslav** - *Initial work*

**Andrey Starchenkov** - *Supervision*

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

*my sanity


