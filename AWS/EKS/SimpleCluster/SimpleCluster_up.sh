##############Read UserConfig#################
eval $(python3 ../_py/ReadConfig.py)
##############################################



##############docker build####################
#./myimage_build.sh
#./ecr_push.sh
##############################################



##############terraform apply##################
terraform init
terraform apply -target=SimpleCluster.tf -var-file=SimpleCluster_Variables.tf
eval $(terraform output | sed 's/^/export /; s/ = /="/g; s/$/"/')
##############################################



############kubectl apply#####################
#aws eks update-kubeconfig --name $cluster_name
###############################################



##########Print Commands#######################
#awskubectl get all
#awskubectl get service -o wide
#awskubectl describe all
#awskubectl describe pods
#awskubectl get pods
#awskubectl get services --all-namespaces -o wide
###############################################

##############Shell Commands#######################
#awskubectl exec -it resume-deployment-############## sh
###############################################

##################Refresh Image################
#awskubectl set image deployment/datascraper-deployment image=$datascraper_image --record
###############################################

