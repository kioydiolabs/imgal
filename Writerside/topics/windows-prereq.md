# Windows Prerequisites Installation

### Installing Python

To install Python, go to [](https://www.python.org/downloads/) and download the latest version.

<img src="install_python.png" height="300"></img>

Then, run the executable and follow the installation instructions.

### Installing the Pillow package

After you have installed Python, you need to install the Pillow package that's used for resizing images and creating thumbails.

To do that, open Powershell and run the following command

```Shell
pip install Pillow
```

<note>If the command above doesn't work, or you get an error that pip could not be found, run the command below instead</note>

```Shell
python -m install Pillow
```

**You now have all the prerequisites you need installed! Go back to [Creating an image gallery](Creating-an-Image-gallery.md) to learn how to create a gallery!**