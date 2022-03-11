# How to use the code
The code is submitted through a jupyter notebook, with the extension *.ipynb*.

To be able to look at it, here are the steps to follow:

# 1) clone the git repository locally

Go to the folder in which you want to clone the repository and input the following command:
```bash
git clone https://github.com/LucBourrat1/cas_test_company_b
```

Then go to the git folder with the command:
```bash
cd cas_test_company_b
```
Once inside the folder, add a folder named "data" and paste the 4 .csv files.

# 2) create an virtual evironment with all the necessary libraries

From the git folder, create a python virtual environment using the following command:
```bash
python3 -m venv cas_test_venv
```
Install the needed python libraries:

```bash
pip install -r requirements.txt
```

The library used to read the jupyter notebooks is included.

# 3) read the .ipynb file using jupyter notebook

To read the notebook from the jupyter lab web API:

```bash
jupyter lab
```

Then click on the hyperlink in the command line, and once in the API in your web browser, click on the .ipynb file.

From here, on the top menu, click on "Cellule -> Exécuter tout".

Wait until all the cells are correctly launched, and read the notebook.