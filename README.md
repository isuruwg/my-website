# 1. personal-website

- [1. personal-website](#1-personal-website)
- [2. Set up instructions for setting things up from scratch](#2-set-up-instructions-for-setting-things-up-from-scratch)
  - [2.1. Virtual environments](#21-virtual-environments)
    - [2.1.1. Production virtual environment](#211-production-virtual-environment)
    - [2.1.2. Development and Testing virtual environment](#212-development-and-testing-virtual-environment)
- [3. CloudBuild](#3-cloudbuild)


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