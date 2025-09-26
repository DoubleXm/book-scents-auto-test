import json

def formatter_parameterize_data(data_path):
    """
      @param data_path: 测试数据文件路径，仅支持 json 文件
      @return: 格式化后的测试参数
    """
    with open(data_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    result = list(map(lambda item: (item['test_input'], item['test_expect']), data))
    
    return result


if __name__ == '__main__':
    from pathlib import Path

    data = formatter_parameterize_data(Path(__file__).parent.parent.parent / 'src/api/data/book_failed_paramter.json')
    print(data)