'''
Created on Feb 14, 2016

@author: Daniel Ammon
'''

'''
git format-patch master --stdout > fix_empty_poster.patch
git apply --stat fix_empty_poster.patch
git apply --check fix_empty_poster.patch
git am --signoff < fix_empty_poster.patch
git reset --hard 414034972eb5d062140c3fb291e7d0880c48937a
git log -1 --pretty=format:%H
use git rebase when online to update to remote sha's
'''

import os, sys

def findPatchFilePath():
    "Searches for a patch file in the current dir"   
    patchName = "ImagePoint03_ImagePoint03.001.patch"  # todo: find path name with endig .patch
    pwd = os.path.split(os.path.abspath(sys.argv[0]))[0]  # current dir  
    patchPath = os.path.join(pwd, patchName) 
    
    if (os.path.isfile(patchPath)):
        print "found patch file: " + patchName
    else: 
        print "cannot find patch file --> exit"
        exit(1)
        
    return patchPath;

def findGitPath():
    "Searches for the path of the git repo"
    packageName = "ohm_bob_drive"  # todo: package name is not fix
    command = "rospack find " + packageName
    if (os.system(command + "> /dev/null") == 0):
        pipe = os.popen(command)
        content = pipe.read()
        content = content.rstrip("\n")
        gitPath = os.path.normpath(content)
        gitPath = os.path.split(os.path.split(os.path.split(gitPath)[0])[0])[0] # in case of bobbyrob catkin is ../../../ from packages
        return gitPath;
        # todo: check for active git repo here
    else:
        print "can't find package location --> exit"
        exit(1)
    
def resetGit(gitPath, SHA):
    "resets the git repo to a sha (debug function)"
    command = "git -C " + gitPath + " reset --hard " + SHA + " 2>> ./log 1>> ./log"
    if (os.system(command) == 0):
        print "reset git to " + SHA        
    else:
        print "not able to reset git --> exit"
        exit(1)
        
def getCurrentSHA(gitPath):
    "get the current SHA from gitPath"
    command = "git -C " + gitPath + " log -1 --pretty=format:%H"
    if (os.system(command + "> /dev/null") == 0):
        pipe = os.popen(command)
        content = pipe.read()
        content = content.rstrip("\n")
        currentSHA = content
        return currentSHA;
    else:
        print "can't get rollback sha --> exit"
        exit(1)

def applyPatch(gitPath, patchPath):
    "apply a patch file"
    command = "git -C " + gitPath + " apply --3way --check " + patchPath
    
    if (os.system(command + " 2>> ./log 1>> ./log") == 0):
        print "able to apply patch --> applying patch..."
        
        command = "git -C " + gitPath + " am --signoff --3way < " + patchPath + " 2>> ./log 1>> ./log" 
        if (os.system(command) == 0):
            print "...patch successfully applied!"
            return 0;
        else: 
            print "error while applying patch --> exit"
            return 1;  # do a rollback here?
    else:
        print "not able to apply patch --> exit"
        command = "git -C " + gitPath + " am --abort 2>> ./log 1>> ./log" 
        os.system(command)
        exit(1)
        
def compileCatkin(catkinPath):
    "compile a catkin_ws"
    print "compiling now..."
    command = "catkin_make" + " --directory " + catkinPath + " 2>> ./log 1>> ./log"     
    if(os.system(command) == 0):
        print "compilation successful"
        return 0;
    else:
        print "error at compilation --> rollback patch"
        return 1;

if __name__ == '__main__':   
    # start logfile
    os.system("echo \"\n\n**** log at: \" >> ./log")
    os.system("date >> ./log")
   
    patchPath = findPatchFilePath()   
   
    gitPath = findGitPath()
    
    catkinPath = os.path.split(os.path.split(gitPath)[0])[0]
        
    # resetGit(gitPath, SHA = "414034972eb5d062140c3fb291e7d0880c48937a")
    
    rollbackSha = getCurrentSHA(gitPath)
    
    resetGit(gitPath, SHA="f5a94f3baac2828f04d97a6ede2de01580fdeb7d")
   
    if(applyPatch(gitPath, patchPath) == 0):
        if(compileCatkin(catkinPath) == 0):
            print "\n+++++++++++++++++++"
            print "+  patching done  +"
            print "+++++++++++++++++++"
            
            print "\n--> please reboot now!"
            exit(0)
    
    # if we are here patch does not fit...       
    print "reverting patch..."
    resetGit(gitPath, SHA=rollbackSha)
    print "patch reverted!"
    
    
    if(compileCatkin(catkinPath) == 0):
        print "sorry, patch cannot be applied --> finished clean"
        exit(0)
    else: 
        print "sorry, patch cannot be applied --> CAUTION: executables could be corrupted now!"
        exit(1)
        
