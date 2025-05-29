# process model unittests

This is a unittests library developed for process modelling simulation.

## Virtual Environment
Create a virtual environment to isolate the packages you install from pypi (python package index).

```bash
python -m venv _virtualenvName_
```

## Installation

Then you can install the required packages for this code in the requirements.txt file.

```bash
pip install -r requirements.txt
```

## Updating the requirements

Any other reqiurements added in the course of updating this library, you can use the command statement below to update
the requirements.txt file

```bash
pip freeze > requirements.txt
```

## Usage

If running the unittest from the commandline. Note: The path "C:\SIMULIA\Commands" (this may vary depending on how Abaqus was installed), must be added to the environment variables.
```bash
abaqus cae noGUI="1elem.py"
```
When running via abaqus, we can easily run the python script by going to the "File" tab and clicking on "Run Script"


## License

iComp2