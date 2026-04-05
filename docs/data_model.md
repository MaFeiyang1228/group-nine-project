# 本项目图数据模型草图

## 1. 节点类型与属性

### 1.1 论文节点 (Article)
- **类型**: `article`
- **属性**:
  - `id`: 唯一标识符 (如WOS:000876084300010)
  - `title`: 论文标题
  - `abstract`: 摘要
  - `publication_year`: 发表年份
  - `journal`: 期刊名称
  - `volume`: 卷号
  - `issue`: 期号
  - `pages`: 页码范围
  - `doi`: DOI
  - `cited_reference_count`: 引用参考文献数量

### 1.2 作者节点 (Author)
- **类型**: `author`
- **属性**:
  - `id`: 唯一标识符 (如作者姓名的标准化形式)
  - `name`: 作者姓名

### 1.3 关键词节点 (Keyword)
- **类型**: `keyword`
- **属性**:
  - `id`: 唯一标识符 (关键词本身)
  - `name`: 关键词名称

### 1.4 期刊节点 (Journal)
- **类型**: `journal`
- **属性**:
  - `id`: 唯一标识符 (期刊名称)
  - `name`: 期刊名称

## 2. 边类型与权重

### 2.1 作者-论文关系 (Authorship)
- **类型**: `authored`
- **方向**: 作者 → 论文
- **权重**: 1 (固定权重)
- **含义**: 作者撰写了论文

### 2.2 论文-关键词关系 (Keyword Assignment)
- **类型**: `has_keyword`
- **方向**: 论文 → 关键词
- **权重**: 1 (固定权重)
- **含义**: 论文包含该关键词

### 2.3 论文-期刊关系 (Publication)
- **类型**: `published_in`
- **方向**: 论文 → 期刊
- **权重**: 1 (固定权重)
- **含义**: 论文发表在该期刊

### 2.4 论文-论文引用关系 (Citation)
- **类型**: `cites`
- **方向**: 引用论文 → 被引用论文
- **权重**: 1 (固定权重)
- **含义**: 一篇论文引用了另一篇论文

### 2.5 作者-作者合作关系 (Co-authorship)
- **类型**: `coauthored_with`
- **方向**: 双向
- **权重**: 合作次数
- **含义**: 两位作者共同撰写过论文

### 2.6 关键词-关键词共现关系 (Keyword Co-occurrence)
- **类型**: `co_occurs_with`
- **方向**: 双向
- **权重**: 共现次数
- **含义**: 两个关键词在同一篇论文中出现

### 2.7 论文-论文共被引关系 (Co-citation)
- **类型**: `co_cited_with`
- **方向**: 双向
- **权重**: 共被引次数
- **含义**: 两篇论文被同一篇其他论文引用

## 3. 示例数据

### 3.1 节点示例

#### 论文节点
```
{"id": "WOS:000876084300010", "type": "article", "title": "Microarchitecture based RISC-V Instruction Set Architecture for Low Power Application", "abstract": "The goal of many contemporary and speculative applications is to create highly efficient CPUs and one among the architecture that is meeting out the above said condition is RISC V processor microarchitecture...", "publication_year": 2022, "journal": "JOURNAL OF PHARMACEUTICAL NEGATIVE RESULTS", "volume": 13, "pages": "362-371", "doi": "10.47750/pnr.2022.13.S06.051", "cited_reference_count": 10}
```

#### 作者节点
```
{"id": "Deepika_R", "type": "author", "name": "Deepika, R"}
{"id": "Priyadharsini_SMG", "type": "author", "name": "Priyadharsini, SMG"}
{"id": "Malar_MM", "type": "author", "name": "Malar, MM"}
{"id": "Anand_IV", "type": "author", "name": "Anand, IV"}
```

#### 关键词节点
```
{"id": "Micro_Architecture", "type": "keyword", "name": "Micro Architecture"}
{"id": "Pipelining", "type": "keyword", "name": "Pipelining"}
{"id": "RISC_V", "type": "keyword", "name": "RISC V"}
```

#### 期刊节点
```
{"id": "JOURNAL_OF_PHARMACEUTICAL_NEGATIVE_RESULTS", "type": "journal", "name": "JOURNAL OF PHARMACEUTICAL NEGATIVE RESULTS"}
```

### 3.2 边示例

#### 作者-论文关系
```
{"source": "Deepika_R", "target": "WOS:000876084300010", "type": "authored", "weight": 1}
{"source": "Priyadharsini_SMG", "target": "WOS:000876084300010", "type": "authored", "weight": 1}
{"source": "Malar_MM", "target": "WOS:000876084300010", "type": "authored", "weight": 1}
{"source": "Anand_IV", "target": "WOS:000876084300010", "type": "authored", "weight": 1}
```

#### 论文-关键词关系
```
{"source": "WOS:000876084300010", "target": "Micro_Architecture", "type": "has_keyword", "weight": 1}
{"source": "WOS:000876084300010", "target": "Pipelining", "type": "has_keyword", "weight": 1}
{"source": "WOS:000876084300010", "target": "RISC_V", "type": "has_keyword", "weight": 1}
```

#### 论文-期刊关系
```
{"source": "WOS:000876084300010", "target": "JOURNAL_OF_PHARMACEUTICAL_NEGATIVE_RESULTS", "type": "published_in", "weight": 1}
```

#### 作者-作者合作关系
```
{"source": "Deepika_R", "target": "Priyadharsini_SMG", "type": "coauthored_with", "weight": 1}
{"source": "Deepika_R", "target": "Malar_MM", "type": "coauthored_with", "weight": 1}
{"source": "Deepika_R", "target": "Anand_IV", "type": "coauthored_with", "weight": 1}
{"source": "Priyadharsini_SMG", "target": "Malar_MM", "type": "coauthored_with", "weight": 1}
{"source": "Priyadharsini_SMG", "target": "Anand_IV", "type": "coauthored_with", "weight": 1}
{"source": "Malar_MM", "target": "Anand_IV", "type": "coauthored_with", "weight": 1}
```

#### 关键词-关键词共现关系
```
{"source": "Micro_Architecture", "target": "Pipelining", "type": "co_occurs_with", "weight": 1}
{"source": "Micro_Architecture", "target": "RISC_V", "type": "co_occurs_with", "weight": 1}
{"source": "Pipelining", "target": "RISC_V", "type": "co_occurs_with", "weight": 1}
```

## 4. 共被引边权重计算方法

### 4.1 Cosine相似度

对于两篇论文A和B，共被引相似度计算公式：

```
cosine_similarity(A, B) = (C(A,B)) / (sqrt(C(A)) * sqrt(C(B)))
```

其中：
- C(A,B) 是A和B的共被引次数
- C(A) 是A被引用的总次数
- C(B) 是B被引用的总次数

### 4.2 Jaccard相似度

对于两篇论文A和B，共被引相似度计算公式：

```
jaccard_similarity(A, B) = (C(A,B)) / (C(A) + C(B) - C(A,B))
```

其中：
- C(A,B) 是A和B的共被引次数
- C(A) 是A被引用的总次数
- C(B) 是B被引用的总次数

## 5. 阈值选择逻辑

### 5.1 Top-N阈值
- 选择共被引次数或相似度排名前N的边
- 优点：保证网络规模可控
- 缺点：可能忽略低权重但有意义的连接

### 5.2 Min Weight阈值
- 选择共被引次数或相似度大于等于某个阈值的边
- 优点：保留所有达到一定重要性的连接
- 缺点：网络规模可能过大或过小

## 6. 网络定义参数

| 参数 | 说明 | 默认值 |
|------|------|--------|
| node_types | 节点类型 | article, author, keyword, journal |
| edge_types | 边类型 | authored, has_keyword, published_in, cites, coauthored_with, co_occurs_with, co_cited_with |
| co_citation_threshold | 共被引边权重阈值 | 1 |
| top_n_co_citations | 共被引边Top-N数量 | 1000 |
| similarity_measure | 相似度计算方法 | cosine |

## 7. 数据清洗与消歧规则

### 7.1 作者消歧
- 基于姓名标准化（去除空格、标点符号）
- 结合机构信息进行匹配
- 利用共现关系增强消歧效果

### 7.2 关键词标准化
- 去除大小写差异
- 合并同义词（如RISC-V和RISC V）
- 去除冗余关键词

### 7.3 论文去重
- 基于DOI或标题+作者组合进行去重
- 合并重复记录的引用信息