class FileSystemSimulator:
    def __init__(self):
        self.blocks = {}

        self.files = {}

        self.directories = {
            "root": []
        }

    def create_file(self, file_name, block_list):
        self.files[file_name] = block_list
        self.directories["root"].append(file_name)

        for block in block_list:
            if block in self.blocks:
                self.blocks[block].append(file_name)
            else:
                self.blocks[block] = [file_name]

    def display(self):
        print("\n--- File System State ---")
        print("Files:", self.files)
        print("Blocks:", self.blocks)
        print("Directories:", self.directories)

    def check_consistency(self):
        print("\n--- Consistency Check Report ---")

        self.check_cross_linked_blocks()
        self.check_lost_files()
        self.check_invalid_directory_entries()

    def check_cross_linked_blocks(self):
        print("\n[1] Cross-linked Blocks:")
        found = False

        for block, file_list in self.blocks.items():
            if len(file_list) > 1:
                found = True
                print(f"Block {block} is shared by files: {file_list}")

        if not found:
            print("No cross-linked blocks found.")

    def check_lost_files(self):
        print("\n[2] Lost Files:")

        found = False
        for file in self.files:
            if file not in self.directories["root"]:
                found = True
                print(f"Lost file detected: {file}")

        if not found:
            print("No lost files found.")

    def check_invalid_directory_entries(self):
        print("\n[3] Invalid Directory Entries:")

        found = False
        for file in self.directories["root"]:
            if file not in self.files:
                found = True
                print(f"Invalid directory entry: {file}")

        if not found:
            print("No invalid directory entries found.")


if __name__ == "__main__":
    fs = FileSystemSimulator()
    fs.create_file("file1", [1, 2, 3])
    fs.create_file("file2", [4, 5])
    
    fs.create_file("file3", [3, 6])

    fs.files["file4"] = [7, 8]

    fs.directories["root"].append("file_invalid")

    fs.display()

    fs.check_consistency()