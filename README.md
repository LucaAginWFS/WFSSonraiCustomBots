WFSSonraiCustomBots
=======================
Contains code for Sonrai bots and template to deploy bot role
-----------------------

## Code Snippets

### Deploy Sonrai Bot IAM Roles
```shell
aws cloudformation deploy --template-file roles/bot-role.yaml --stack-name sonrai-bot-roles --capabilities CAPABILITY_NAMED_IAM --tags "App=cloudSecurity" "Domain=infrastructure" "Env=prod" "Name=sonrai-bot-role" "Owner=BlackOps@wfscorp.com"
```

### For Testing: Deploy 
```shell
aws cloudformation package --template-file proxy-lambda/cfn-templates/sonra-bot-poxy-function.yaml --s3-bucket wfs-cloud-security-sam-lambdas --output-template-file packaged-template.yaml
```
```shell
aws cloudformation deploy --template-file packaged-template.yaml --stack-name TEMP-sonrai-bot-proxy --capabilities CAPABILITY_IAM --tags "App=cloudSecurity" "Domain=infrastructure" "Env=prod" "Name=sonrai-bot-proxy" "Owner=BlackOps@wfscorp.com"
```


