WFSSonraiCustomBots
=======================
Contains code for Sonrai bots and template to deploy bot role
-----------------------

## Code Snippets

### Deploy CodeCommit Repos
```shell
aws cloudformation deploy --template-file roles/bot-role.yaml --stack-name sonrai-bot-roles --capabilities CAPABILITY_NAMED_IAM --tags "App=cloudSecurity" "Domain=infrastructure" "Env=prod" "Name=sonrai-bot-role" "Owner=BlackOps@wfscorp.com"
```