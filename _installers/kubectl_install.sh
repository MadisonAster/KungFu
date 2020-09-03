curl -o kubectl https://amazon-eks.s3.us-west-2.amazonaws.com/1.17.9/2020-08-04/bin/linux/amd64/kubectl
chmod +x ./kubectl
mkdir -p $HOME/bin && cp ./kubectl $HOME/bin/awskubectl && export PATH=$PATH:$HOME/bin #naming kubectl binary awskubectl to avoid potential WSL2 conflicts
#echo 'export PATH=$PATH:$HOME/bin' >> ~/.bashrc
kubectl version --short --client