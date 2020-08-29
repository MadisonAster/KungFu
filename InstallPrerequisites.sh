#Install these packages if you would like to run the entire suite of unittests via TestKit.py 
#Each template module in this library is individually testable as well.
#
#Please also note this particular shell script is currently untested, and installation processes are subject to change.
#Double check the installation instructions from each individual vendor.
#
#I test all of this code on both Windows and Ubuntu, but be aware that future modules I will add to this library will be windows only.
#e.g. unreal

pip3 install pyside2
pip3 install qt.py
pip3 install pandas

curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
aws --version

curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo apt-key add -
sudo apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main"
sudo apt-get update && sudo apt-get install terraform
terraform -help

curl -o kubectl https://amazon-eks.s3.us-west-2.amazonaws.com/1.17.9/2020-08-04/bin/linux/amd64/kubectl
chmod +x ./kubectl
mkdir -p $HOME/bin && cp ./kubectl $HOME/bin/awskubectl && export PATH=$PATH:$HOME/bin #naming kubectl binary awskubectl to avoid potential WSL2 conflicts
#echo 'export PATH=$PATH:$HOME/bin' >> ~/.bashrc
kubectl version --short --client

