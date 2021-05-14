import sys
import os
import requests

print (sys.argv[1])
print (sys.argv[2])

# blank filepath will create in current working directory
filepath = ''
filename = filepath + 'Power BI Desktop Localhost ' + sys.argv[1].strip('localhost:') + '.ipynb'

# URL for GitHub gist that includes the JSON for your Jupyter notebook template
gist_url = 'https://gist.githubusercontent.com/deldersveld/70e05dbc97086181641592f03d314800/raw/a413d9e67b7d8e744869f1ef2078fb7ff5aa2894/PowerBIDesktopNotebookBasicConnectionSample.json'
notebook_core = requests.get(gist_url).text.replace('<<PowerBIServer>>',sys.argv[1]).replace('<<PowerBIDatabase>>',sys.argv[2])
print (notebook_core)

# URL for ssas_api module (download .py script sample)
py_url = 'https://raw.githubusercontent.com/yehoshuadimarsky/python-ssas/3b0afc6f6b3a534a6c2a767b67ddadefd8f7bae1/ssas_api.py'
py_file = requests.get(py_url)
open('ssas_api.py', 'wb').write(py_file.content)

if os.path.exists(filename):
    print(filename + ' already exists. Not overwriting.')

try:
    if not os.path.exists(filename):
        print('Creating ' + filename)
        file = open(filename,'w+')
        file.write(notebook_core)
        file.close()

    print('Opening Jupyter')

    os.system('"C:/ProgramData/anaconda3/python.exe C:/ProgramData/anaconda3/Scripts/jupyter-notebook-script.py "' + filename + '""')

except:
    print('Unable to create Jupyter notebook file')



input()