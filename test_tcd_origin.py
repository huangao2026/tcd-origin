"""
TCD Origin API 测试脚本
"""
import requests

# 你的 API 配置
API_URL = "https://kzh9kgwxb3.coze.site/stream_run"
API_TOKEN = "把你的API_TOKEN粘贴在这里"  # 从扣子部署页面获取

def test_topology():
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }
    
    data = {
        "content": {
            "query": {
                "prompt": [
                    {
                        "type": "text",
                        "content": {
                            "text": "\"日\"字的8维拓扑特征向量是什么？请严格按以下定义回答：V = [水平对称, 垂直对称, 宽高比, 欧拉数, 连通分量, 环数, 像素密度, 宽高比归一化]"
                        }
                    }
                ]
            }
        },
        "type": "query",
        "session_id": "test-topology"
    }
    
    print("正在调用 TCD Origin API...")
    print("问题: \"日\"字的8维拓扑特征向量是什么？")
    print("-" * 50)
    
    response = requests.post(API_URL, headers=headers, json=data, timeout=120)
    
    print(f"状态码: {response.status_code}")
    print(f"响应: {response.text}")

if __name__ == "__main__":
    test_topology()
