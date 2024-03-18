# webapi-test
for testing web API with python

## Install
In this project I used pipenv for managing packeges.
`pip install pipenv`
Then add fastai and uvicorn to pipenv
```
pipenv install fastai 'uvicorn[standard]'
```
https://fastapi.tiangolo.com/
https://www.uvicorn.org/

## Local Test
`cd <repo dir>`
Start API server with the command below
`$ uvicorn main:app --reload`

We can check all endpoints, methods and schemes if moving to http//localhost:8000/docs

## Reference
[FastAPIでPythonアプリを素早く構築する](https://kinsta.com/jp/blog/fastapi/)
[GitHub Docs: 基本的な書き方とフォーマットの構文](https://docs.github.com/ja/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)