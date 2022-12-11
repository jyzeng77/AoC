class File():
    def __init__(self, name, size) -> None:
        self.name = name
        self.size = size

class Directory():
    nest_level = 0
    cwd = []

    def __init__(self, name) -> None:
        self.files = []
        self.name = name
    
    def add(self, obj):
        self.files.append(obj)
    
    def move(self, location):
        if location == '/':
            nest_level = 0
            cwd.clear()

        elif location == '..' and self.nest_level > 0:
            nest_level -= 1
            cwd.pop()
        
        else:
            nest_level += 1
            cwd.append(location)
            
    def ls(self):
        return self.files
    
directory = Directory('/')
level = 1
ls_called = False

with open('p7.txt') as f:
    for ln in f:
        cmd = ln.split()
        cwd = []
        if ln[0] == '$':
            if cmd[1] == 'cd':
                pass
