# Linux Prerequisites Installation

## Installing Python

To install Python, open the Terminal and run the command below

```Shell
sudo apt update && sudo apt install python3 -y
```

## Installing the Pillow package

After you have installed Python, you need to install the Pillow package that's used for resizing images and creating thumbails.

To do that, open the Terminal and run the following command

```Shell
pip install Pillow
```

::: tip Note
If the command above doesn't work, or you get an error that pip could not be found, run the command below instead
:::

```Shell
python -m install Pillow
```

**You now have all the prerequisites you need installed! Go back to [Creating an image gallery](creating-an-image-gallery) to learn how to create a gallery!**