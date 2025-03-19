# PsyNet APNG Animation Test

This experiment is implemented using the [PsyNet framework](https://www.psynet.dev/). It demonstrates how to create
interactive animations based on images in Animated Portable Network Graphics format (APNG, see [Wikipedia article on APNG here](https://en.wikipedia.org/wiki/APNG)).



## Installing PsyNet and preparing to run this experiment

We highly recommend to run this under Linux and in a Python virtual environment using `venv`. This will spare you the hassle of setting up WSL2 and Docker under Windows. For final testing of your experiment before deploying it, we would recommend to run it in Docker once (again under Linux).

### Quick install instructions for Linux

Make sure you have a recent Python version (e.g., Python 3.12) and the Google Chrome browser installed.

Then get python dev packages, a database server and redis. E.g., for Ubuntu 22.04 LTS:

```sh
sudo apt install vim python3.11-dev python3.11-venv python3-pip redis-server git libenchant-2-2 postgresql postgresql-contrib libpq-dev unzip
```

For Ubuntu 24.04 LTS, just replace `python3.11-dev python3.11-venv` with `python3.12-dev python3.12-venv`.

Then setup the postgres database:

```sh
sudo service postgresql start
sudo -u postgres -i    # opens a new shell as the database user 'postgres'
createuser -P dallinger --createdb  # add DB user dallinger with createDB permission. When asked for new password, enter 'dallinger' (twice).
createdb -O dallinger dallinger    # create database dallinger owned by user dallinger
createdb -O dallinger dallinger-import   # create database dallinger-import owned by user dallinger
exit  # exits the shell of user postgres, so you are back to your user
sudo service postgresql reload  # important to apply configuration
```

Now install the experiment from this repo, which will install dependencies like the PsyNet and Dallinger python packages:

```sh
git clone https://github.com/dfsp-spirit/psynet-animation.git
cd psynet-animation/
python -m venv venv
source venv/bin/activate
pip install -r constraints.txt    # This will get you PsyNet, Dallinger and their dependencies
psynet debug local   # opens your Chrome webbrowser.
```

Chrome should open automatically and display the PsyNet overview page. If not, open Chrome manually and connect to [localhost:5000](http://localhost:5000).

Select the `Development` tab and click `New Participant` to run the experiment.

Note: If you are running an older Linux version and your system Python is very old, you can install [miniconda](https://www.anaconda.com/docs/getting-started/miniconda/install) and use it to get a more recent Python.


### Other ways of installing

If you need to run this under Windows, please follow the full PsyNet installation instructions, available in [docs/INSTALL.md](./docs/INSTALL.md). In that case, you will also want to have a look at the list of run commands in [docs/RUN.md](./docs/RUN.md).

## General information on the PsyNet framework

For more information about PsyNet, see the [documentation website](https://psynetdev.gitlab.io/PsyNet/).


## Troubleshooting hints

#### Problem: I am being asked for credentials I don't know when manually connecting to the PsyNet overview page at http://localhost:5000.

Solution: PsyNet uses a user and password to protect its overview page and provides these credentials to Chrome automatically on startup. If you connect manually, you will be asked for this information. The easiest way to get the information is to define it yourself in the config file `~/.dallingerconfig` like this:

Create the file `~/.dallingerconfig` and put these lines into it (it's in INI format):

```
[Dashboard]
dashboard_user = admin
dashboard_password = 12345
```

Restart the PsyNet server. Then use these credentials to login when asked.


