## bibtex2item

#### 使用说明

1. 在google scholar文章引用复制Bibtex格式，例如:
```
@article{agmls2009novel,
  title={A novel connectionist system for improved unconstrained handwriting recognition},
  author={AGMLS, Fernandez and Bunke, RBH and Schmiduber, J},
  journal={IEEE Transactions on Pattern Analysis Machine Intelligence},
  volume={31},
  year={2009}
}
```
2. 将Bibtex格式复制到test.tex文件中
3. 调用函数`parse_bibs`，读取`test.tex`文件
4. 期刊引文生成，先调用函数`parse_article`，读取期刊数据，生成期刊格式调用函数`bibtex2bibitem_article`
5. 会议引文生成，先调用函数`parse_conference`，读取会议数据，生成会议调用函数`bibtex2bibitem_conference`