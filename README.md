# Python Sandbox

## Using Environments
This repo uses `venv` to manage python packages. Please refer to [this](https://codesolid.com/what-is-a-python-package/#htoc-i) article for further reading.

### Creating from VSCode
1. Open command palette `Ctrl` + `Shift` + `P`
2. Type `env`
3. Choose "Create Python Environment"
4. Choose `venv` from the selection
5. This will create a venv on the root, that can be accessed by ipynbs

### Recreating 
Please refer to [this](https://stackoverflow.com/questions/9207430/how-to-copy-clone-a-virtual-environment-from-server-to-local-machine) article.
1. Run `pip freeze > requirements.txt` on source machine
2. Copy to destination machine (or to remote repo)
3. Run `pip install -r requirements.txt` on target machine

---
### Creating the Virtual Env
  - change to desired directory
  - run module `venv` in directory `.venv`
```bash
python -m venv .venv
```

### Activating the Virtual Env
For Windows:
```bash
.venv\scripts\activate
```

For Linux/Mac:
```bash
source .venv/bin/activate
```

### Deactivating the Virtual Env
```
deactivate
```

## Using Jupyter Notebooks with Environments
Notebooks do not work out of the box with `venv` Environments. Please refer to [this](https://anbasile.github.io/posts/2017-06-25-jupyter-venv/) article for further reading.

### Installing `ipykernel`
From the active virtual environment, install ipykernel
```bash
pip install ipykernel
```

Then install a new kernel from the directory name used in venv installation beforehand
```bash
ipython kernel install --user --name=.venv
```

Don't forget to **restart** VSCode!!

## Converting `.ipynb` to `.md`
Install `nbconvert`
```bash
pip install nbconver
```
Run the following command
```bash
jupyter nbconvert --to markdown <file.ipynb>
```