#eval $(python3 ../_py/ReadConfig.py)

#cd ./MyProjectDir
eval $(terraform output | sed 's/^/export /; s/ = /="/g; s/$/"/')

export datascraper_image_id=$(docker images datascraper:latest --format "{{.ID}}")
export myapache_image_id=$(docker images myapache:latest --format "{{.ID}}")

aws ecr get-login-password --region $aws_region | docker login --username AWS --password-stdin $aws_user_id.dkr.ecr.$aws_region.amazonaws.com

docker tag $datascraper_image_id $aws_user_id.dkr.ecr.$aws_region.amazonaws.com/kungfu-service
docker push $aws_user_id.dkr.ecr.$aws_region.amazonaws.com/kungfu-service
