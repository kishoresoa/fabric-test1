from fabric.api import local

def prepare_deploy():

    local("cd /home/devops/python/fabric-test1 && touch file1 file2 file3")

    local("cd /home/devops/python/fabric-test1 && git add . && git commit -m test")

    local("cd /home/devops/python/fabric-test1 && git push origin master")
