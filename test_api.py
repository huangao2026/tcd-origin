"""
TCD Origin API 测试脚本
"""
import requests

# 你的 API 配置
API_URL = "https://kzh9kgwxb3.coze.site/stream_run"
API_TOKEN = "把你的API_TOKEN粘贴在这里"  # 从扣子部署页面获取

def test_api():
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
                            "text": "你好，请介绍一下你自己"
                        }
                    }
                ]
            }
        },
        "type": "query",
        "session_id": "test-session-1"
    }
    
    print("正在调用 TCD Origin API...")
    response = requests.post(API_URL, headers=headers, json=data, timeout=60)
    
    print(f"状态码: {response.status_code}")
    print(f"响应: {response.json()}")

if __name__ == "__main__":
    test_api()
