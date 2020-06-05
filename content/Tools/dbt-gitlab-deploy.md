title: How to setup dbt devops with GitLab CI/CD with Snowflake database
date: 5th June 2020
author: Robin Beer
summary: Short description of the content
tags: HowTo, backend, devops, dataops,  
status:draft

Working with databases
-> SQL

Object-oriented SQL?

dbt! 

"The T in ELT"


https://www.youtube.com/watch?v=-XBIIY2pFpc&feature=youtu.be&t=1305

https://gitlab.com/gitlab-data/analytics/-/blob/master/transform/snowflake-dbt/snowflake-dbt-ci.yml


https://gitlab.com/gitlab-data/analytics/-/blob/master/transform/snowflake-dbt/profile/profiles.yml

## Local installation

pip install dbt

dbt init

bigquery or snowflake config


first simple query

## Write your first dbt models

tbd

## GitLab CI/CD pipeline

GitLab environment variables for Snowflake

profile/profiles.yml

environment variable for dbt run options
- export CI_PROFILE_TARGET="--profiles-dir profile --target ci"


```bash
image: python:latest

variables:
  PIP_CACHE_DIR: "$CI_PROJECT_DIR/.cache/pip"

cache:
  paths:
    - .cache/pip
    - venv/

before_script:
  - python -V  # Print out python version for debugging
  - pip install virtualenv
  - virtualenv venv
  - source venv/bin/activate
  - pip install dbt
  - export CI_PROFILE_TARGET="--profiles-dir profile --target dev"
  - echo $CI_PROFILE_TARGET

run:
  script:
     dbt run $CI_PROFILE_TARGET 
```

## Conclusion

dbt = data build tool
"the T in ELT" 
locally installed, built your own simple model and connected and tested it on snowflake (or bigquery)

Finally, setup CI/CD pipeline on GitLab. 

Go deplo