#Imports##########################################
import os, yaml
from FooFinder import KungFu
##################################################

#Test#############################################
class test_envsubst(KungFu.TimedTest):
    def __init__(self, *args):
        super().__init__(*args)
        self.cwd = os.path.dirname(os.path.abspath(__file__))
    
    def test_11_EFSVolume_temp(self):
        inpath = self.cwd+'/EKS/EFSCluster/eks_efsvolume.yaml'
        outpath = self.cwd+'/EKS/EFSCluster/eks_efsvolume_temp.yaml'
        vars = {
            'efs_id' : 'fs.TESSST',
        }
        envsubst(inpath, outpath, vars)

##################################################

#Code#############################################
def recurse_replace(data, find, replace):
    for key, value in data.items():
        if isinstance(value, dict):
            recurse_replace(value, find, replace)
        elif isinstance(value, list):
            for i in range(len(value)):
                value[i].replace(find, replace)
        elif isinstance(value, str):
            data[key] = value.replace(find, replace)

def envsubst(inpath, outpath, vars):
    with open(inpath, 'r') as file:
        ydata = yaml.safe_load(file)
    for key, value in vars.items():
        if isinstance(value, str):
            recurse_replace(ydata, '${'+key+'}', value)
    with open(outpath, 'w') as file:
        ydump = yaml.dump(ydata)
        file.write(ydump)
##################################################

#Main#############################################
if __name__ == '__main__':
    KungFu.main(__file__)
##################################################
