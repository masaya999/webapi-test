# webapi-test
for testing web API with python

## Install
In this project I used pipenv for managing packeges.<br>
`pip install pipenv`<br>
Then add fastai and uvicorn to pipenv<br>
```
pipenv install fastai 'uvicorn[standard]'
```
https://fastapi.tiangolo.com/<br>
https://www.uvicorn.org/<br>

## Local Test
`cd <repo dir>`<br>
Start API server with the command below<br>
`$ uvicorn main:app --reload`<br>

We can check all endpoints, methods and schemes if moving to http//localhost:8000/docs<br>

## Reference
- [FastAPIでPythonアプリを素早く構築する](https://kinsta.com/jp/blog/fastapi/)<br>
- [GitHub Docs: 基本的な書き方とフォーマットの構文](https://docs.github.com/ja/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)<br>
- [FastAPI: セキュリティ - 最初の一歩](https://fastapi.tiangolo.com/ja/tutorial/security/first-steps/)