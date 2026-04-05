import pandas as pd
import re

def parse_ris_file(file_path):
    """
    解析RIS格式的文献数据文件
    :param file_path: RIS文件路径
    :return: 包含文献数据的列表
    """
    records = []
    current_record = {}
    
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            
            if line.startswith('ER  -'):
                # 记录结束
                if current_record:
                    records.append(current_record)
                    current_record = {}
            else:
                # 解析字段
                if len(line) >= 6 and line[2:4] == '  -':
                    tag = line[:2]
                    value = line[6:].strip()
                    
                    if tag in current_record:
                        # 如果字段已存在，转换为列表
                        if not isinstance(current_record[tag], list):
                            current_record[tag] = [current_record[tag]]
                        current_record[tag].append(value)
                    else:
                        current_record[tag] = value
    
    # 处理最后一条记录
    if current_record:
        records.append(current_record)
    
    return records

def normalize_data(records):
    """
    标准化数据，处理列表类型字段和缺失值
    :param records: 原始记录列表
    :return: 标准化后的记录列表
    """
    normalized_records = []
    
    for record in records:
        normalized = {}
        
        # 处理标题
        normalized['title'] = record.get('TI', '')
        
        # 处理作者
        authors = record.get('AU', [])
        if not isinstance(authors, list):
            authors = [authors]
        normalized['authors'] = '; '.join(authors)
        normalized['author_count'] = len(authors)
        
        # 处理摘要
        normalized['abstract'] = record.get('AB', '')
        
        # 处理关键词
        keywords = record.get('KW', [])
        if not isinstance(keywords, list):
            keywords = [keywords]
        normalized['keywords'] = '; '.join(keywords)
        
        # 处理发表年份
        normalized['publication_year'] = record.get('PY', '')
        
        # 处理期刊
        normalized['journal'] = record.get('T2', '') or record.get('SO', '')
        
        # 处理卷号
        normalized['volume'] = record.get('VL', '')
        
        # 处理期号
        normalized['issue'] = record.get('IS', '')
        
        # 处理页码
        start_page = record.get('SP', '')
        end_page = record.get('EP', '')
        if start_page and end_page:
            normalized['pages'] = f"{start_page}-{end_page}"
        else:
            normalized['pages'] = start_page or end_page or ''
        
        # 处理DOI
        normalized['doi'] = record.get('DO', '')
        
        # 处理引用参考文献数量
        cited_ref_count = record.get('N1', '')
        # 从字符串中提取数字
        match = re.search(r'Cited Reference Count:\s*(\d+)', cited_ref_count)
        if match:
            normalized['cited_reference_count'] = match.group(1)
        else:
            normalized['cited_reference_count'] = ''
        
        # 处理WOS ID
        normalized['wos_id'] = record.get('AN', '')
        
        normalized_records.append(normalized)
    
    return normalized_records

def create_dataframe(records):
    """
    将记录列表转换为pandas DataFrame
    :param records: 标准化后的记录列表
    :return: pandas DataFrame
    """
    df = pd.DataFrame(records)
    return df

def main():
    """
    主函数，执行数据处理流程
    """
    # 输入文件路径
    input_file = r'd:\CCCPPPUUU\github_nine\group-nine-project\data\raw\wos_riscv_2015-2026_raw.ris'
    
    # 解析RIS文件
    print("正在解析RIS文件...")
    records = parse_ris_file(input_file)
    print(f"解析完成，共{len(records)}条记录")
    
    # 标准化数据
    print("正在标准化数据...")
    normalized_records = normalize_data(records)
    
    # 创建DataFrame
    print("正在创建DataFrame...")
    df = create_dataframe(normalized_records)
    
    # 保存为CSV文件
    output_file = r'd:\CCCPPPUUU\github_nine\group-nine-project\data\processed\normalized_data.csv'
    df.to_csv(output_file, index=False, encoding='utf-8-sig')
    print(f"数据已保存到{output_file}")
    
    # 显示数据概览
    print("\n数据概览:")
    print(df.head())
    print(f"\n数据形状: {df.shape}")
    print("\n字段列表:")
    print(df.columns.tolist())

if __name__ == "__main__":
    main()