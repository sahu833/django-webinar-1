# django-webinar

## Basic Requirements

### 1) Python Installation

#### WINDOWS

##### Step 1: Download the Python 3 Installer

1. Open a browser window and navigate to the [Download page for Windows](https://www.python.org/downloads/windows/) at python.org.

1. Underneath the heading at the top that says Python Releases for Windows, click on the link for the Latest Python 3 Release - Python 3.x.x. (As of this writing, the latest is Python 3.8.2).

1. Scroll to the bottom and select either Windows x86-64 executable installer for 64-bit or Windows x86 executable installer for 32-bit.

##### Step 2: Run the Installer

Run the downloaded Installer to install python as any other software in windows.
>Important: You want to be sure to check the box that says Add Python 3.x to PATH as shown to ensure that the interpreter will be placed in your execution path.

##### Step 3: Check Installation

open a powershell window and run `python --version` to check if python is installed.
the output should be something like

```
Python 3.8.2
```

#### USING WSL(WINDOWS SUBSYSTEM FOR LINUX)

Go to the following [link](https://docs.microsoft.com/en-us/windows/wsl/install-win10) to find the instructions for setting up wsl1 on your windows 10 machine.

Now before you could install python on wsl you need to [initialize your distro instance once](https://docs.microsoft.com/en-us/windows/wsl/initialize-distro), before it can be used.

after you have initialized your distro once. Fire up wsl and run the following command to install python(same as any linux installation).

`sudo apt install python3`

after a succesful installation run `python --version` to see if it has been correctly installed.

#### UBUNTU

If you have ubuntu 17.10 or higher they already come with python3.6 by default.

if you have a lower version Fire up a terminal window by pressing `Ctrl`+`Alt`+`T`.
and run the following command:

 `sudo apt-get install python3.6`

### 2) Django project setup

now you have python installed in your machines, Fire up a terminal window(powershell for windows) and follow these steps to setup a dummy project
#### Step 1: Install pip
Python now comes with pip by default. But most of the time, it comes with an old version. it is always a good practice to upgrade pip to the latest version

```
python -m pip install --upgrade pip
```

#### Step 2: Installing virtualenv

The main purpose of Python virtual environments is to create an isolated environment for Python projects. This means that each project can have its own dependencies, regardless of what dependencies every other project has.

In the same shell window run the following command
```
pip install virtualenv
```

#### Step 3: Create a work/project directory

let’s create a project directory. We will name it django_project

To create the directory:

```
mkdir django_project
```

Change into the `django_project` directory:

```
cd django_project
```

#### Step 4 : Create a new virtual environment in the directory

if you have python3 this command will generate a virtuan environment by the name of `env`. If you have python2 replace `venv` with `virtualenv`.
```
python3 -m venv env
```

#### Step 5: Activating the virtual environment

Before you can start installing or using packages in your virtual environment you’ll need to activate it.

On macOs or Linux
```
source env/bin/activate
```

On Windows
```
.\env\Scripts\activate
```
#### Step 6: Installing Django in virtualenv

Run the following command to install django in your current active virtual environment.
```
pip install Django
```


### Refrences

+ [Python Installation](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
+ [Virtual Environment Installation](https://realpython.com/installing-python/)
