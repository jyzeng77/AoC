# Media type definitions

class File():
    def __init__(self, name, size) -> None:
        self.name = name
        self.size = size
    
    def __str__(self) -> str:
        return f"File '{self.name}', size {self.size}"

class Directory():
    nest_level = 0
    cwd = []
    root_dir = None

    def __init__(self, name, is_root=False) -> None:
        self.files = []
        self.name = name
        if is_root:
            self.root_dir = self
    
    def __str__(self) -> str:
        return f'Directory \'{self.name}\''
    
    def add(self, obj):
        self.files.append(obj)
    
    def move(self, location):
        if location == '/':
            self.nest_level = 0
            self.cwd.clear()

        elif location == '..' and self.nest_level > 0:
            self.nest_level -= 1
            self.cwd.pop()
        
        else:
            self.nest_level += 1
            self.cwd.append(location)
    
    def open_cwd(self):

        directory = self.root_dir

        if len(self.cwd) == 0:
            return directory

        for i in range(self.nest_level):
            for thing in directory.ls():
                if thing.name == self.cwd[i] and isinstance(thing, Directory):
                    directory = thing
        return directory
            
    def ls(self):
        return self.files
    
    def print_cwd(self):
        # Prettier print out of ls with cwd
        print('/'.join(directory.cwd), directory.open_cwd().ls())
    
    def find_directories(self, d=None):
        directory = []
        if d == None:
            current_dir = self.root_dir
            directory.append(self.root_dir)
        else:
            current_dir = d
        for thing in current_dir.ls():
            if isinstance(thing, Directory):
                directory.append(thing)
                current_dir = thing
                directory.extend(thing.find_directories(current_dir))
        return directory
    
    def size(self):
        size = 0
        for thing in self.ls():
            if isinstance(thing, File):
                size += thing.size
            elif isinstance(thing, Directory):
                size += thing.size()
        
        return size

# Solution starts here

directory = Directory('/', is_root=True)
ls_called = False

with open('p7.txt') as f:
    for ln in f:
        cmd = ln.split()
        cwd = []
        if ln[0] == '$':
            ls_called = False
        
        if not ls_called:
            if cmd[1] == 'cd':
                directory.move(cmd[2])
            elif cmd[1] == 'ls':
                ls_called = True
        else:
            if cmd[0] == 'dir':
                directory.open_cwd().add(Directory(cmd[1]))
            else:
                directory.open_cwd().add(File(cmd[1], int(cmd[0])))

max_space = 70000000 - 30000000
min_deletion_size = directory.root_dir.size() - max_space

folder_sizes = [d.size() for d in directory.find_directories()]
folder_sizes.sort()

for deletion_size in folder_sizes:
    if deletion_size >= min_deletion_size:
        print(deletion_size)
        break
