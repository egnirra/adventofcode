import uuid



class Folder:
    def __init__(self, name: str) -> None:
        self.name = name
        self.uuid = ""
        self.parent = ""
        self.files = []
        self.size = 0

    def __str__(self) -> str:
        return f"Folder Name: {self.name}, Parent: {self.parent}, Size: {self.size}"

    def __repr__(self) -> str:
        return f"Folder Name: {self.name}, Parent: {self.parent}, Size: {self.size}"

    def size_contents(self):
        total = 0
        for c in self.files:
            if isinstance(c, File):
                total += c.size

        self.size = total
    
    def add_file(self, file) -> None:
        self.files.append(file)

class File:
    def __init__(self, name: str, size: int) -> None:
        self.name = name
        self.size = size

    def __str__(self) -> str:
        return f"File Name: {self.name}, Size: {self.size}"

    def __repr__(self) -> str:
        return f"File Name: {self.name}, Size: {self.size}"

dirs = []
current_dir: Folder = Folder("test")
current_dir.parent = "none"

def check_cmd(line: str):
    global current_dir
    split_line = line.split(" ")
    current_dir.size_contents()

    match line.split(" "):
        case [_, "cd", _]:
            if current_dir not in dirs:
                dirs.append(current_dir)

            if split_line[2] == "..":
                for d in dirs:
                    if d.uuid == current_dir.parent:
                        current_dir = d
            else:
                _parent = current_dir.uuid
                current_dir = Folder(split_line[2])
                current_dir.uuid = str(uuid.uuid4())
                current_dir.parent = _parent
        case [_, "ls"]:
            pass
        case ["dir", _]:
            pass
        case ["eof"]:
            dirs.append(current_dir)
        case _:
            new_file = File(split_line[1], int(split_line[0]))
            current_dir.add_file(new_file)

with open("2022/day7/input.txt") as f:
    for line in f.readlines():
        line = line.replace("\n","")
        check_cmd(line)

    dirs.reverse()
    for d in dirs:
        dir: Folder
        for dir in dirs:
            if d.parent == dir.uuid:
                idx = dirs.index(dir)
                dirs[idx].size += d.size
    part_one = []
    dirs.sort(key=lambda x: x.size)
    p: Folder
    for p in dirs:
        part_one.append(p.size)
            
    part_two = []
    p: Folder
    for p in dirs:
        if p.size > 30000000 - (70000000 - max(part_one)):
            part_two.append(p.size)

    print(max(part_one))
    print(min(part_two))