# PsyNet APNG Animation Test

This experiment is implemented using the [PsyNet framework](https://www.psynet.dev/). It demonstrates how to create
interactive animations based on images in Animated Portable Network Graphics format (APNG, see [Wikipedia article on APNG here](https://en.wikipedia.org/wiki/APNG)).



## Installing PsyNet and preparing to run this experiment

We highly recommend to run this under Linux and in a Python virtual environment using `venv`. This will spare you the hassle of setting up WSL2 and Docker under Windows. For final testing of your experiment before deploying it, we would recommend to run it in Docker once (again under Linux).

### Quick install instructions for Linux

Make sure you have a recent Python version (e.g., Python 3.12) and the Google Chrome browser installed.

```sh
git clone https://github.com/dfsp-spirit/psynet-animation.git
cd psynet-animation/
pip install -r constraints.txt
psynet debug local   # opens your Chrome webbrowser.
```

Chrome should open and display the PsyNet overview page. Click on 




### Other way of installing

If you need to run this under Windows, please follow the full PsyNet installation instructions, available in [docs/INSTALL.md](./docs/INSTALL.md). In that case, you will also want to have a look at the list of run commands in [docs/RUN.md](./docs/RUN.md).

## General information on the PsyNet framework

For more information about PsyNet, see the [documentation website](https://psynetdev.gitlab.io/PsyNet/).
