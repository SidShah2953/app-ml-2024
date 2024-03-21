# Assignment 2: Experiment Tracking

## Due 20 Feb 2024

- Data Version Control
  - [x] In `prepare.ipynb` track the versions of data using `dvc`
  - [x] Load the raw data into `raw_data.csv` and save the split data into `train.csv`/`validation.csv`/`test.csv`
  - [x] Update train/validation/test split by choosing different random seed
  - [x] Checkout the first version (before update) using `dvc` and print the distribution of target variable (number of $0$s and number of $1$s) in `train.csv`, `validation.csv`, and `test.csv`
  - [x] Checkout the updated version using `dvc` and print the distribution of target variable in `train.csv`, `validation.csv`, `test.csv`
  - [x] Bonus: (decouple compute and storage) track the data versions using google drive as storage
- Model Version Control and Experiment Tracking
  - [x] In `train.ipynb` track the experiments and model versions using `mlflow`
  - [x] Build, track, and register 3 benchmark models using MLflow
  - [x] Checkout and print AUCPR for each of the three benchmark models

## References

- <https://dvc.org/doc/start/data-management/data-versioning>
- <https://realpython.com/python-data-version-control/>
- <https://towardsdatascience.com/how-to-manage-files-in-google-drive-with-python-d26471d91ecd>
- <https://mlflow.org/docs/latest/tracking.html>
- <https://www.datarevenue.com/en-blog/how-we-track-machine-learning-experiments-with-mlflow>
- <https://towardsdatascience.com/experiment-tracking-with-mlflow-in-10-minutes-f7c2128b8f2c>
