# Operating-System_project
📂 File System Consistency Checker (Simulator)

📌 Overview


The File System Consistency Checker is a Python-based simulator that verifies the correctness of a file system by analyzing its metadata structures. It replicates how operating systems manage files, disk blocks, and directory entries, and ensures system reliability by detecting inconsistencies.

🧠 Problem Statement

File systems may become inconsistent due to system crashes, improper shutdowns, or bugs. These inconsistencies can lead to:

Data loss
Corrupted file structures
Incorrect file references

This project simulates a solution that identifies such issues using metadata verification techniques.

🧩 Key Concepts Covered
File System Structure
Metadata Management
Disk Block Allocation
Directory Organization
Consistency Checking
🚀 Features
📁 Simulates files, disk blocks, and directories
🔍 Performs metadata-based consistency checks
⚠️ Detects:
Cross-linked blocks
Lost files
Invalid directory entries
🧾 Generates a detailed error report
💡 Simple and easy-to-understand Python implementation
🛠️ Technologies Used
Python 3
⚙️ System Design
📊 Components:
Files Table → Stores file names and allocated blocks
Block Map → Tracks which blocks are used
Directory Structure → Maintains file references
🔎 Types of Errors Detected
1️⃣ Cross-Linked Blocks

When a single disk block is shared by multiple files.

2️⃣ Lost Files

Files that exist in metadata but are not referenced in any directory.

3️⃣ Invalid Directory Entries

Directory entries pointing to non-existent files.
