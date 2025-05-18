from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "status": "success",
        "message": "AI健康平台API服务已成功部署",
        "version": "1.0.0"
    })

@app.route('/api/health-check')
def health_check():
    return jsonify({
        "status": "healthy",
        "services": {
            "api": "online",
            "database": "simulated"
        }
    })

# 为Vercel Serverless部署添加处理程序
def handler(event, context):
    return app(event, context)

# 本地运行时使用
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
