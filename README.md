# sktime-workshop-pydata-london-2022
PyData London 2022 sktime workshop

## Instalation guide
Follow the instructions below to get your environment for the workshop up and running.

### Using python venv:

1. Create a python virtual environment:  
`python -m venv .venv`
2. Activate your environment:  
`source .venv/bin/activate`
3. Install the package in development mode:  
`pip install -e .`
4. Make the environment available in jupyter:  
`python -m ipykernel install --user --name=pydata_sktime`

### Using conda env:

1. Create a python virtual environment:  
`conda create -y -n pydata_sktime python=3.9`
2. Make sure the environment has pip:  
`conda install -y -n pydata_sktime pip`
3. Activate your environment:  
`conda activate pydata_sktime`
4. Install the package in development mode:  
`pip install -e .`
5. Make the environment available in jupyter:  
`python -m ipykernel install --user --name=pydata_sktime`
