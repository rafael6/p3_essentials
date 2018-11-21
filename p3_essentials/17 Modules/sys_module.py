import sys
# clean termination closing any open files.
# Optional int argument which is passed to the calling shell.
#sys.close()

print(sys.platform)
print('Python version {}.{}.{}'.format(*sys.version_info))
print('The category of the OS is: {}'.format(sys.platform))  # Ex. if sys.plaform.startswith(“win”)
print(sys.executable)  # Absolute path of interpreter
print(sys.path)  # Search path for modules when importing
print(sys.exit(0))  # Exit from Python
