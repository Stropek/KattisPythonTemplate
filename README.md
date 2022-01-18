# Kattis Solution

[![Build Status](https://travis-ci.org/Stropek/KattisPythonTemplate.svg?branch=master)](https://travis-ci.org/Stropek/KattisPythonTemplate)

Python 3 scaffolding for solving Kattis problems.

# Prep

* Install VS Code
* Install VS Code Extensions:
    * [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
    * [Python Test Explorer for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=LittleFoxTeam.vscode-python-test-adapter)
* Clone this repo
* Install python packages from _requirements.txt_
* Log in to [Open Kattis](https://open.kattis.com/)
* Download your [personal configuration file](https://open.kattis.com/download/kattisrc) to your *home* path.

# Init

From _Scripts_ directory, run 
    
    .\init.ps1 [POBLEM_NAME]
    
This should create a *Python* directory next to where you cloned the scaffolding repo, download sample test files for your problem and open VS Code instance ready for you to start working on your solution. 

# Solving

Solutions should go in Solution.py file.

# Unit tests

For unit tests to work all output needs to be written to _out_

    def solve(self, in_file_stream, out=sys.stdout):
      out.write('expected output')

# Submitting

Be sure to uncomment this line: 

    Solution().solve(sys.stdin, sys.stdout)
    
Run *submit.bat*.

# IDEs

Scaffolding is set to work with *Visual Studio Code*, but if you prefer to use *PyCharm* you can by commenting line 32 and uncommenting line 31 in _projectSetup.ps1_.

    31. #Start-Process Pycharm $workingDir.ToString()
    32. Start-Process code $workingDir.ToString() -NoNewWindow
