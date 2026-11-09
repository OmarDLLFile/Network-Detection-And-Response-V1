import platform
import shutil
import os
import socket

def inspect_environment():
    print("=== NDR PHASE 0: SYSTEM INSPECTION ===")
    # 1. Python Version
    print(f"[+] Python Version: {platform.python_version()} (Required: >= 3.11)")
    
    # 2. Operating System
    print(f"[+] Operating System: {platform.system()} {platform.release()} ({platform.architecture()[0]})")
    
    # 3. Disk Space
    total, used, free = shutil.disk_usage("/")
    print(f"[+] Available Disk Space: {free // (2**30)} GB")
    
    # 4. Network Interfaces (Basic standard library check)
    print("[+] Available Network Interfaces:")
    interfaces = socket.if_nameindex() if hasattr(socket, 'if_nameindex') else []
    for interface in interfaces:
        print(f"    - {interface[1]}")
        
    # 5. Project Directory
    cwd = os.getcwd()
    print(f"[+] Current Directory: {cwd}")
    existing_files = os.listdir(cwd)
    print(f"[+] Existing files/folders: {', '.join(existing_files[:5])}{'...' if len(existing_files) > 5 else ''}")

if __name__ == "__main__":
    inspect_environment()
