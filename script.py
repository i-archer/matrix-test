#!/usr/bin/env python

import platform
from datetime import datetime

def create_artifact():
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    os_info = platform.platform()

    artifact_content = f"Current Date & Time: {current_datetime}\n"
    artifact_content += f"OS Name & Version: {os_info}"

    with open('artifact.txt', 'w') as file:
        file.write(artifact_content)

if __name__ == "__main__":
    create_artifact()
    
