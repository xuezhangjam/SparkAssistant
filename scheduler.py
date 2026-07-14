import json
import os
import subprocess
import time

CONFIG_FILE = "clients.json"
RUNNER_SCRIPT = "runner.py"

def main():
    print("=== 抖音代续火花 批量调度系统 ===")
    if not os.path.exists(CONFIG_FILE):
        print(f"配置文件 {CONFIG_FILE} 不存在，请先使用 add_client.py 录入客户！")
        return
        
    with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
        config = json.load(f)
        
    active_clients = [cid for cid, c in config.items() if c.get("status") == "active"]
    
    if not active_clients:
        print("当前没有任何活跃客户，调度结束。")
        return
        
    print(f"共发现 {len(active_clients)} 个活跃客户，准备开始串行处理...")
    
    for client_id in active_clients:
        client = config[client_id]
        print("\n" + "="*50)
        print(f"⏰ 开始处理客户: {client.get('alias', client_id)} (ID: {client_id})")
        print("="*50)
        
        # 使用 subprocess 调用 runner.py
        try:
            import sys
            subprocess.run([sys.executable, RUNNER_SCRIPT, client_id], check=True)
            print(f"✅ 客户 {client_id} 处理完成！")
        except subprocess.CalledProcessError as e:
            if e.returncode == 2:
                print(f"⚠️ 客户 {client_id} 触发安全验证，已自动跳过。")
                try:
                    subprocess.run([
                        "notify-send", 
                        "-a", "抖音续火花系统", 
                        "-i", "dialog-warning", 
                        "客户状态失效预警", 
                        f"客户【{client.get('alias', client_id)}】遇到安全验证或登录过期，已自动跳过！请前往控制台重新验证。"
                    ])
                except Exception:
                    pass
            else:
                print(f"❌ 客户 {client_id} 处理失败，错误码: {e.returncode}")
            
        print("休息 5 秒后继续下一个客户...")
        time.sleep(5)
        
    print("\n🎉 所有活跃客户的代续火花任务已完成！")

if __name__ == "__main__":
    main()
