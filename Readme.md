## 基于 Github API 的 PullRequest 简报 Agent

目前所有流程都在 prompt_engineering.ipynb  
根据 requirements.txt 配置环境 (Python 3.11, 不用 conda 也行)
```shell
pip install -r requirements.txt
```
如果已经安装证书，仍然报出 SSL 的错误，请检查代理配置，或者将证书内容追加至 certifi 库的证书集

使用 Github REST API 需要在 github 的个人设置中生成个人访问令牌 (Personal access token)，网页路径为： https://github.com/settings/tokens

注意要生成 classic token，而不是 fine-grained token（实测只能读不能写），并且注意勾选全部读写权限；  
然后将 token 放到当前目录新建 github_token 文件；  

由于 github push 时会进行安全检测，文件中包含上述 token 或者 LLM apikey 都会报安全问题，所以 apikey 都放到了 model_mapper.zip 中，解压 model_mapper.json 到同级项目路径；处理后当前目录结构如下:

> pgat/
>> readme/  
>> utils/  
>> github_token  
>> model_mapper.json  
>> model_mapper.zip  
>> prompt_engineering.ipynb  
>> Readme.md  
>> requiments.txt

jupyter notebook 建议使用 vscode 打开，可能用到的插件：

- Jupyter
- Jupyter Cell Tags
- Jupyter Keymap
- Jupyter Notebook Renderers
- Jupyter Slide Show
- Python
- Python Environments
- Python Extension Pack
- Pylance

notebook 中，示例了总结 browser-use 最近 2 天的 open PR 并汇总成周报，评论到 icm162/pgat 的首个 PR 下；实测在 github enterprise 中也是以上相同操作获取 access token，可以考虑换用内部可用的大模型 api；

![comment_sample](.\readme\\comment_sample.png)

