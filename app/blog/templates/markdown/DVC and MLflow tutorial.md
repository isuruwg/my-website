# Tutorial on how to use DVC and MLFlow <!-- omit in toc -->

The code for this tutorial can be found [here](https://github.com/isuruwg/dvc-and-mlflow-tutorial)

# Contents <!-- omit in toc -->
- [1. Introduction](#1-introduction)
  - [1.1. Environment setup](#11-environment-setup)
  - [1.2. Initialize DVC](#12-initialize-dvc)
  - [1.3. Configure remote storage](#13-configure-remote-storage)
  - [1.4. Copy some data and let dvc manage it](#14-copy-some-data-and-let-dvc-manage-it)
  - [1.5. Fetching data from remote](#15-fetching-data-from-remote)
  - [1.6. Modifying data](#16-modifying-data)
  - [1.7. Using different data versions](#17-using-different-data-versions)
    - [1.7.1. In python](#171-in-python)
    - [1.7.2. Using dvc command line](#172-using-dvc-command-line)
  - [1.8. Usage with MLFlow](#18-usage-with-mlflow)
- [2. Appendix](#2-appendix)
  - [2.1. Setting up Python environment from scratch](#21-setting-up-python-environment-from-scratch)
  - [2.2. Setting up gsutil if you are using GCP storage as a remote](#22-setting-up-gsutil-if-you-are-using-gcp-storage-as-a-remote)
- [3. References](#3-references)

# 1. Introduction

This introductory tutorial will walk you through how to track different versions of your datasets using DVC and experiments (hyperparameters, results, datasets used, etc.) using MLFlow. This walkthrough is designed to give a quick idea of how to use both these tools. However, since there are some overlaps in the features of DVC and MLFlow, you can use just one tool or the other for your applications too to achieve similar results. 

This is based on [Data Versioning and Reproducible ML with DVC and MLflow - Youtube](https://www.youtube.com/watch?v=W2DvpCYw22o&t).

Please refer to the [dvc](https://dvc.org/doc/start) and [mlflow](https://www.mlflow.org/docs/latest/tutorials-and-examples/tutorial.html) official tutorials for more info.

## 1.1. Environment setup

This tutorial was tested with Python 3.9.2.

Create virtual environment:

```bash
python -m venv venv
. ./venv/bin/activate
```

Install requirements:

```bash
pip install -r requirements.txt
```

## 1.2. Initialize DVC

This guide assumes you are already inside a git repo. If not, please initialize a git repo by doing `git init` or some other method.

Run: 

```bash
dvc init
```
This initializes dvc and also adds some of the newly created files to git staging.

If you run `git status` it'll show something like: 

```bash
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   .dvc/.gitignore
        new file:   .dvc/config
        new file:   .dvc/plots/confusion.json
        new file:   .dvc/plots/confusion_normalized.json
        new file:   .dvc/plots/default.json
        new file:   .dvc/plots/linear.json
        new file:   .dvc/plots/scatter.json
        new file:   .dvc/plots/smooth.json
        new file:   .dvcignore
```

## 1.3. Configure remote storage

Reference: [dvc `add`](https://dvc.org/doc/command-reference/remote/add)

The remote storage in dvc can be `s3`, `gs`, `gdrive`, etc. For this example we'll use a local folder `~/tmp/dvc-storage` for simplicity. 

```bash
# We'll add a location inside a local ~/tmp folder for testing 
dvc remote add -d dvc-remote ~/tmp/dvc-storage
# You can also add GCP or other remote storage as the remote.
# Please refer to https://dvc.org/doc/command-reference/remote/add 
```

This adds the following to the .dvc/config file

```ini
[core]
    remote = dvc-remote
['remote "dvc-remote"']
    url = /home/isuru/tmp/dvc-storage
```

If you would like to add a remote storage like GCP, you can do so by:

```bash
dvc remote add -d gcp_bucket gs://dvc-mlflow-bucket
```

## 1.4. Copy some data and let dvc manage it

Let's now copy some data to a local folder `data/`

```bash
mkdir data
```

Copy an example file;

For this we'll copy [wine-quality.csv example file from mlflow](https://github.com/mlflow/mlflow/blob/master/examples/sklearn_elasticnet_wine/wine-quality.csv) into the [data/](data/) folder.
```bash
wget --directory-prefix=data/ https://raw.githubusercontent.com/mlflow/mlflow/master/examples/sklearn_elasticnet_wine/wine-quality.csv
```

Add the file to dvc:

```bash
dvc add data/wine-quality.csv
```
DVC creates a [wine-quality.csv.dvc](data/wine-quality.csv.dvc) file and also adds a [.gitignore](data/.gitignore) file inside the `data/` folder.

Let's also add a git tag to make it easier to track the data versions through git:

```bash
# Add and commit:
git add data/wine-quality.csv.dvc data/.gitignore
git commit -m "data: track"

git tag -a 'v1' -m 'raw data'
```

Now let's sync our local data with our remote:

```bash
dvc push
```

Let's now see what's inside our remote

```bash
ls -lR ~/tmp/dvc-storage/
```

This gives:

```bash
/home/user/tmp/dvc-storage/:
total 4
drwxrwxr-x 2 user user 4096 Apr 13 14:47 5d

/home/user/tmp/dvc-storage/5d:
total 260
-r--r--r-- 1 user user 264426 Apr 13 14:47 6f24258e3c50bb01a61194b5401f5d
```

Now, we can remove the local data if required:

```bash
rm -rf data/wine-quality.csv
# Let's remove the data from .dvc/cache too
rm -rf .dvc/cache
```

## 1.5. Fetching data from remote

Since we deleted our data in the section above, we can bring them back from remote using `dvc pull`

```bash
dvc pull
```

## 1.6. Modifying data

```bash
# Let's do a simple modification to our csv file
sed -i '2,1001d' data/wine-quality.csv
# let's check dvc status
dvc status
```
`dvc status` command shows that our file was changed:

```bash
data/wine-quality.csv.dvc:                                            
        changed outs:
                modified:           data/wine-quality.csv
```

Now let's add the new data file to dvc:

```bash
dvc add data/wine-quality.csv
```

Now let's do a git commit:
```bash
git add data/wine-quality.csv.dvc
git commit -m "data: remove 1000 lines"
```

Let's also add a git tag:

```bash
git tag -a 'v2' -m 'removed 1000 lines'
```

Let's also push our data to remote storage:

```bash
dvc push
```

Also remember to push your tag to the remote repo by doing `git push --tags`.

## 1.7. Using different data versions

### 1.7.1. In python

```python
import dvc.api

data_url = dvc.api.get_url(
        path = 'data/wine-quality.csv',
        repo = '.',
        # You can use different values for rev here.
        # This can be any revision such as a branch tag name or a comit hash
        # ref: https://dvc.org/doc/api-reference/get_url
        rev = 'v2'
    )

# Then you can use the data in your favourite tool, eg: pandas;
data = pd.read_csv(data_url)
```

### 1.7.2. Using dvc command line

`git checkout` combined with `dvc checkout` is one way to do this. Please refer to [dvc checkout documentation](https://dvc.org/doc/command-reference/checkout) for more info.

## 1.8. Usage with MLFlow

For this, we'll use [this file from mlflow examples](https://github.com/mlflow/mlflow/blob/master/examples/sklearn_elasticnet_wine/train.py). 

This file has been downloaded to [train.py](train.py). ( [exact same version of file used can be accessed through this link](https://github.com/mlflow/mlflow/blob/d743a40426d5dedbde395a4e6bbdeebadbccd4dc/examples/sklearn_elasticnet_wine/train.py) )


This guide shows **one** of the many ways you can use mlflow and dvc together. However, please note that these two tools also have some overlaps between their features which allow you to use these tools in many other different ways (either together or independently). Please follow the docs for [mlflow]() and [dvc]() for more info.

MLFlow allows to track hyperparameters, performance metrics, using a helpful python package. Values of python variables can be tracked across different runs by using the `log_param` function.

```python
mlflow.log_param('data_url', data_url)
mlflow.log_param('data_version', VERSION)
mlflow.log_param('input_rows', data.shape[0])
mlflow.log_param('input_cols', data.shape[1]) 
```

MLFLow runs can be recorded using the following different methods [[ref](https://www.mlflow.org/docs/latest/tracking.html#where-runs-are-recorded)]:

- Local file path
- SQL db
- MLflow tracking server
- Databricks workspace

For this example we'll use a local file method. This is the easiest way to do things. But if we want to track and share our experiments with colleagues, using one of the [other](https://www.mlflow.org/docs/latest/tracking.html#where-runs-are-recorded) supported methods to store experiment data is recommended.

Now let's try two different experiments with two different versions of data:

open [train.py](train.py) and find the following constants (lines 25 to 28): 

```python
# Constants for dvc
PATH = 'data/wine-quality.csv'
REPO = '.' # Path to the Git repo
VERSION = 'v2' # This is the GitHub tag corresponding to the data version
```

The `VERSION` constant here defines the GitHub tag associated with the data version we want to use. Run [train.py](train.py) (`python train.py`) and see the results, now change the `VERSION` constant to `VERSION=v1` and run [train.py](train.py) again. You can see based on the results that a different data version has been used.

You can now open the MLFlow ui by running,

```bash
# activate virtual environment if you haven't already
# . ./venv/bin/activate

mlflow ui
```

And visit http://127.0.0.1:5000/ to view experiments.

# 2. Appendix

## 2.1. Setting up Python environment from scratch

This section shows how to create the development environment from scratch.

Create virtual environment:

```bash
python -m venv venv
. ./venv/bin/activate
```

Install dependencies:
```bash
pip install mlflow
# dvc has many installation options such as [all], [s3], [gdrive], etc.
# Please refer to: https://dvc.org/doc/install/linux
pip install dvc[gs]

# Dependencies for the MLFlow, DVC combined tutorial
pip install scikit-learn
```

Freeze dependencies:
```bash
pip freeze > requirements.txt
```

## 2.2. Setting up gsutil if you are using GCP storage as a remote

Please refer to [this guide](https://cloud.google.com/sdk/docs/install#deb) to install and setup `gsutil` and make sure you are logged in.

Please refer to the relevent GCP section in [this guide](https://dvc.org/doc/command-reference/remote/add) to see the most up to date information about setting up gcp credentials.

# 3. References 

1. [Data Versioning and Reproducible ML with DVC and MLflow - Youtube](https://www.youtube.com/watch?v=W2DvpCYw22o&t)
