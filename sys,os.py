import sys,os
sys.argv        # List of command-line arguments
sys.exit([arg])  # Exit the interpreter by raising SystemExit(status)
sys.getfilesystemencoding()  # Return the encoding used to convert file names
sys.getsizeof(object)  # Return the size of an object in bytes
sys.getrefcount(object)  # Return the reference count of the object
sys.getrecursionlimit()  # Return the current value of the recursion limit
sys.setrecursionlimit(limit)  # Set the maximum depth of the Python interpreter stack
sys.getdefaultencoding()  # Return the name of the current default string encoding

sys.stdin   # Standard input stream
sys.stdout  # Standard output stream
sys.stderr  # Standard error stream

sys.stdout = open('output.txt', 'w')
print('Hello, world!')  # This will be written to 'output.txt'

sys.version  # String containing the version number of the Python interpreter
sys.version_info  # Tuple containing the five components of the version number
sys.platform  # Platform identifier (e.g., 'win32', 'darwin', 'linux')

sys.modules  # Dictionary that maps module names to modules that have already been loaded
sys.path     # List of strings specifying the search path for modules

sys.exc_info()  # Return a tuple of the current exception type, value, and traceback





print(os.getlogin())  # Get the name of the logged-in user
print(os.getloadavg())  # Get the load average
print(os.urandom(16))  # Get 16 random bytes

print(os.path.basename('/path/to/file.txt'))  # 'file.txt'
print(os.path.dirname('/path/to/file.txt'))  # '/path/to'
print(os.path.join('/path/to', 'file.txt'))  # '/path/to/file.txt'
print(os.path.split('/path/to/file.txt'))  # ('/path/to', 'file.txt')
print(os.path.splitext('/path/to/file.txt'))  # ('/path/to/file', '.txt')
print(os.path.abspath('file.txt'))  # Absolute path to 'file.txt'
print(os.path.exists('file.txt'))  # True if file exists
print(os.path.isfile('file.txt'))  # True if it's a regular file
print(os.path.isdir('/path/to'))  # True if it's a directory

print(os.environ)  # Get all environment variables
print(os.getenv('HOME'))  # Get the value of the 'HOME' environment variable
os.putenv('MY_VAR', 'value')  # Set a new environment variable
os.unsetenv('MY_VAR')  # Unset (remove) an environment variable

os.mkdir('new_dir')  # Create a new directory
os.makedirs('new_dir/sub_dir', exist_ok=True)  # Create directories recursively
os.rmdir('new_dir')  # Remove a directory

os.remove('file.txt')  # Remove a file
os.rename('old_name.txt', 'new_name.txt')  # Rename a file or directory

print(os.getcwd())  # Get current working directory
os.chdir('/path/to/new/directory')  # Change directory

