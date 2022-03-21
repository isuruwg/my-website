[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)

# personal-website <!-- omit in toc -->

Currently, this is a mostly static website. This doesn't technically need to be hosted on GCP and it also doesn't have to be a Flask app (There are much easier ways to host static websites). I just had some extra GCP credits and also want to be able to extend this in the future with more cooler things (eg: logging into my home automation system)

# TOC <!-- omit in toc -->

- [1. Set up instructions for setting things up from scratch](#1-set-up-instructions-for-setting-things-up-from-scratch)
  - [1.1. Python environment management](#11-python-environment-management)
    - [1.1.1. First time environment setup using Poetry](#111-first-time-environment-setup-using-poetry)
  - [1.2. Pre-commit](#12-pre-commit)
- [2. CloudBuild](#2-cloudbuild)
- [3. Black](#3-black)
- [4. PyTest](#4-pytest)
- [5. Safety tests and upgrading](#5-safety-tests-and-upgrading)
  - [5.1. Test production packages](#51-test-production-packages)
  - [5.2. Test development packages](#52-test-development-packages)
  - [5.3. Run cloudbuild locally to see if everything looks good](#53-run-cloudbuild-locally-to-see-if-everything-looks-good)


This GitHub repository contains the code used in my personal website [isuru.ca](isuru.ca)

# 1. Set up instructions for setting things up from scratch

As the title suggests, this is for someone who wants to set things up from scratch and understand how things work. If you already cloned this repo from my GitHub and want to just run this, you don't have to run the steps here. Go directly to section 3.

## 1.1. Python environment management

[Poetry](https://python-poetry.org/) is used for managing the Python environment for this repo. An environment for production along with a separate environment for development is managed using Poetry.

You can also set-up the environment without using poetry by using the provided [requirements.txt](requirements.txt) and [requirements-dev.txt](requirements-dev.txt) files. This can be done by doing; 
```bash
# Manual environment setup without using Poetry
python -m venv venv
pip install -r requirements.txt # or use requirements-dev.txt as appropriate
```

### 1.1.1. First time environment setup using Poetry

If you just cloned this repo and want to setup the Python environment locally, please do the following:

```bash
# cd into the root of this repo and install all the dependencies
poetry install --no-root

# Activate poetry shell
poetry shell

# Run app
python main.py
```

## 1.2. Pre-commit

```bash
# pre-commit is added to poetry as a dev dependency. poetry add pre-commit --dev (This step has already been done)

# Install pre-commit
pre-commit install --allow-missing-config
```

# 2. CloudBuild

I'm using Google CloudBuild to run tests and then deploy my app to GCP AppEngine automatically. The tests are defined in [cloudbuild.yaml](./cloudbuild.yaml)

You can run CloudBuild locally by installing the necessary packages as shown in the [GCP official guide](https://cloud.google.com/cloud-build/docs/build-debug-locally) and then running `cloud-build-local --dryrun=false .` from the top level folder. The commands to do this as of 2022-03-19 are listed below for convenience:

1. Install Google Cloud CLI
    ```bash
    sudo apt-get install apt-transport-https ca-certificates gnupg
    # Add the deb package source
    echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
    # Import the public key
    curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key --keyring /usr/share/keyrings/cloud.google.gpg add -
    # Install the google cloud cli
    sudo apt-get update && sudo apt-get install google-cloud-cli
    ```
2. Install Docker
3. Install the local builder  
    NOTE: As of 2022-03-19, the [official instructions](https://cloud.google.com/build/docs/build-debug-locally#apt-get) are outdated. The package name should be `google-cloud-cli-cloud-build-local` and not `google-cloud-sdk-cloud-build-local`. [REF: NOTE: For releases prior to 371.0.0, the package name is google-cloud-sdk](https://cloud.google.com/sdk/docs/install#deb)
    ```bash
    sudo apt-get install google-cloud-cli-cloud-build-local
    ``` 
4. Log in using `gcloud auth login` (You can do `gcloud auth list` to see if you have already logged in)
5. List the available projects: `gcloud projects list`
6. Create a new project in the console if you haven't already done so
7. Set project: `gcloud config set project PROJECT_ID`
8. Create an app engine app by: `gcloud app create` (If you haven't already done so)
9. Navigate to the folder containing your [cloudbuild.yaml](cloudbuild.yaml) file and run Cloud build: `cloud-build-local --dryrun=false .`. Note: If you run docker in rootless mode, this will fail, there's currently an open issue [here](https://github.com/GoogleCloudPlatform/cloud-build-local/issues/116)
    


# 3. Black
I use Python Black to do code formatting. Run black by doing `black .` on the top folder after activating the `venv-dev` environment.

# 4. PyTest

Run `PyTest` by running `pytest` on the top level folder. The tests are defined in the [/tests](/tests) folder.

You can do `coverage run -m pytest` to get the coverage report.

Coverage report can be viewed by:
- `coverage report` : Shows a report in the terminal
- `coverage html` : creates a html coverage report. You can open this in your favourite browser. eg: `firefox htmlcov/index.html`

# 5. Safety tests and upgrading

## 5.1. Test production packages

```bash
. ./venv-dev/bin/activate
python -m safety check -r requirements.txt
```
Upgrade the affected versions by:

```bash
# deactivate # deactivate virtual environment if a different one was active
. ./venv/bin/activate
pip install -U <AFFECTED PACKAGES>
pip freeze > requirements/common.txt
```

## 5.2. Test development packages

```bash
python -m safety check -r requirements/dev.txt
pip install -U <AFFECTED PACKAGES>
pip freeze > requirements/venv-dev-freeze.txt
```

## 5.3. Run cloudbuild locally to see if everything looks good

`cloud-build-local --dryrun=false .`  (Refer to [3. CloudBuild](#3-cloudbuild) for more info)