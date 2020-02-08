import json
import boto3

codebuild = boto3.client('codebuild')

def lambda_handler(event, context):
    # Start codeBuild when codeCommit trigger lambda func
    response = codebuild.start_build(
        projectName = 'DemoQuestionExamCodeBuild',
        sourceVersion = 'refs/heads/master'
        )
