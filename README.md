[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)

# 1. personal-website

- [1. personal-website](#1-personal-website)
- [2. Set up instructions for setting things up from scratch](#2-set-up-instructions-for-setting-things-up-from-scratch)
  - [2.1. Virtual environments](#21-virtual-environments)
    - [2.1.1. Production virtual environment](#211-production-virtual-environment)
    - [2.1.2. Development and Testing virtual environment](#212-development-and-testing-virtual-environment)
- [3. CloudBuild](#3-cloudbuild)
- [4. Black](#4-black)
- [5. PyTest](#5-pytest)
- [6. Safety tests and upgrading](#6-safety-tests-and-upgrading)
  - [6.1. Test production packages](#61-test-production-packages)
  - [6.2. Test development packages](#62-test-development-packages)
  - [6.3. Run cloudbuild locally to see if everything looks good](#63-run-cloudbuild-locally-to-see-if-everything-looks-good)


This GitHub repository contains the code used in my personal website [isuru.ca](isuru.ca)

# 2. Set up instructions for setting things up from scratch

As the title suggests, this is for someone who wants to set things up from scratch and understand how things work. If you already cloned this repo from my GitHub and want to just run this, you don't have to run the steps here. Go directly to section 3.

## 2.1. Virtual environments

In order to keep our production and development/testing virtual environments separate, we'll create a couple of different virtual environments

### 2.1.1. Production virtual environment

- Create a virtual environment with `python -m venv venv`
- Activate venv by doing `. ./venv/bin/activate`
- Install the following packages (or you can use included requirements.txt file if the same versions are needed)

    ```
    pip install flask
    pip install flask-bootstrap
    ```
- Do `pip freeze > requirements/common.txt` to create a common requirements file.
- Run this app by doing `python main.py` on the base folder.

**We'll also create a couple of other requirements files as follows**
- create a `requirements/prod.txt` file
    ```
    # production requirements
    -r common.txt
    ```
- Create a top level `requirements.txt` file to mirror the `requirements/prod.txt` file
    ```
    # Mirrors requirements/prod.txt
    -r requirements/prod.txt
    ```

### 2.1.2. Development and Testing virtual environment

Now we'll create another virtual environment and requirements file in order to keep our development environment separate.

- Create a virtual environment with `python -m venv venv-dev`
- Activate the new environment with `. ./venv-dev/bin/activate`
- Install the requirements from our common requirements file: `pip install -r requirements.txt`
- Install the following development only dependencies:
    ```
    pip install flake8
    pip install bandit
    pip install safety
    pip install pytest
    pip install coverage
    pip install black
    ```
- Create the following files: 
  - `pip freeze > requirements/venv-dev-freeze.txt`
  - Create a new file named `requirements/dev.txt`
    ```
    # These are the requirements for ../venv-dev/ virtual environment
    # This combines the venv-dev file created by pip freeze on venv-dev environment and any other missing dependencies from production
    -r common.txt
    -r venv-dev-freeze.txt
    ```

# 3. CloudBuild

I'm using Google CloudBuild to run tests and then deploy my app to GCP AppEngine automatically. The tests are defined in [cloudbuild.yaml](./cloudbuild.yaml)

You can run CloudBuild locally by installing the necessary packages as shown in the [GCP official guide](https://cloud.google.com/cloud-build/docs/build-debug-locally) and then running `cloud-build-local --dryrun=false .` from the top level folder.

# 4. Black
I use Python Black to do code formatting. Run black by doing `black .` on the top folder after activating the `venv-dev` environment.

# 5. PyTest

Run `PyTest` by running `pytest` on the top level folder. The tests are defined in the [/tests](/tests) folder.

You can do `coverage run -m pytest` to get the coverage report.

Coverage report can be viewed by:
- `coverage report` : Shows a report in the terminal
- `coverage html` : creates a html coverage report. You can open this in your favourite browser. eg: `firefox htmlcov/index.html`

# 6. Safety tests and upgrading

## 6.1. Test production packages

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

## 6.2. Test development packages

```bash
python -m safety check -r requirements/dev.txt
pip install -U <AFFECTED PACKAGES>
pip freeze > requirements/venv-dev-freeze.txt
```

## 6.3. Run cloudbuild locally to see if everything looks good

`cloud-build-local --dryrun=false .`