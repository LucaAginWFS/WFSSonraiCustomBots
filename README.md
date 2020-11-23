WFSSonraiCustomBots
=======================
Contains code for Sonrai bots and template to deploy bot role
-----------------------

## Code Snippets

### Deploy Sonrai Bot IAM Roles
```shell
aws cloudformation deploy --template-file cfn-templates/sonrai-bot-roles.yaml --stack-name cloud-sec-sonrai-bot-roles --capabilities CAPABILITY_NAMED_IAM --tags "App=cloudSecurity" "Domain=infrastructure" "Env=prod" "Name=cloud-sec-sonrai-bot-roles" "Owner=BlackOps@wfscorp.com"
```

#### Packaging the pipeline template and deploying the packaged pipeline template
```shell
aws cloudformation package --template-file pipeline/sonrai-bot-roles-pipeline.yaml --s3-bucket wfs-cloud-security-sam-lambdas --output-template-file packaged-template.yaml

aws cloudformation deploy --template-file packaged-template.yaml --stack-name sonrai-bot-roles-pipeline --capabilities CAPABILITY_IAM --tags "App=cloudSecurity" "Domain=infrastructure" "Env=prod" "Name=cloud-sec-sonrai-bot-roles" "Owner=BlackOps@wfscorp.com"
```