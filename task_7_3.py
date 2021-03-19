import os
from shutil import copytree

project_dir = 'my_project'
dst_dir = 'my_project/templates'

if not os.path.isdir(dst_dir):
    os.mkdir(dst_dir)

for root, dirs, files in os.walk(project_dir):
    if root.endswith('/templates'):
        for t_dir in dirs:
            if not os.path.exists(os.path.join(dst_dir, t_dir)):
                copytree(os.path.join(root, t_dir), os.path.join(dst_dir, t_dir))
