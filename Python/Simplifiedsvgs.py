from xml.dom import minidom
from svg.path import parse_path
import os

path = r"" # path to svg file

os.chdir(path)
for file in os.listdir():
   
   with open(file) as f:
        content = '\n'.join([line.strip() for line in f.readlines()])
        contentcopy = content
       
        svg_dom = minidom.parseString(content)
        
        path_strings = [path.getAttribute('d') for path in svg_dom.getElementsByTagName('path')]
        # d attribute parsing
        for path_string in path_strings:
            path_data = parse_path(path_string)
            data = path_data.d()
            new = contentcopy.replace(path_string,data)
            contentcopy = new 
        
        # placing modified svg file in same svg file
        with open(file,'w') as s:
         s.write(contentcopy)