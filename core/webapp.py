import os
from flask import Flask, request, jsonify, send_from_directory
from core.database import init_db, save_benefit, get_benefits, delete_benefit

# تحديد مسار المجلد الرئيسي للمشروع حيث يتواجد ملف index.html الآن
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__)

# إنشاء وتجهيز قاعدة البيانات تلقائياً عند التشغيل
init_db()

@app.route('/')
def home():
    """تقديم واجهة المنصة من المجلد الرئيسي للمستودع مباشرة"""
    return send_from_directory(BASE_DIR, 'index.html')

@app.route('/api/benefits', methods=['GET'])
def fetch_benefits():
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify([])
    return jsonify(get_benefits(user_id))

@app.route('/api/benefits', methods=['POST'])
def add_benefit():
    data = request.json
    if not data or 'user_id' not in data or 'benefit_text' not in data:
        return jsonify({"success": False, "error": "بيانات ناقصة"})
    
    save_benefit(data['user_id'], data.get('benefit_type', 'عامة'), data['benefit_text'])
    return jsonify({"success": True})

@app.route('/api/benefits/delete', methods=['POST'])
def remove_benefit():
    data = request.json
    if not data or 'benefit_id' not in data or 'user_id' not in data:
        return jsonify({"success": False, "error": "بيانات ناقصة"})
    
    success = delete_benefit(data['benefit_id'], data['user_id'])
    return jsonify({"success": success})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
