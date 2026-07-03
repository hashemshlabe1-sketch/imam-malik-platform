from flask import Flask, render_template, request, jsonify
from core.database import init_db, add_benefit, get_user_benefits, delete_benefit
import config

app = Flask(__name__, template_folder='../templates')

# تهيئة قاعدة البيانات والتأكد من وجود الجداول فور تشغيل الخادم
init_db()

@app.route('/')
def index():
    """عرض الواجهة الرئيسية للمنصة"""
    return render_template('index.html')

@app.route('/api/benefits', methods=['GET'])
def get_benefits():
    """منفذ لجلب فوائد طالب معين بناءً على معرف التيليجرام الخاص به"""
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({"error": "user_id مطلوب"}), 400
    
    benefits = get_user_benefits(user_id)
    return jsonify(benefits)

@app.route('/api/benefits', methods=['POST'])
def save_benefit():
    """منفذ لحفظ فائدة جديدة أرسلها الطالب من الكناشة"""
    data = request.json
    user_id = data.get('user_id')
    benefit_type = data.get('benefit_type')
    benefit_text = data.get('benefit_text')
    
    if not user_id or not benefit_type or not benefit_text:
        return jsonify({"error": "جميع الحقول مطلوبة"}), 400
        
    add_benefit(user_id, benefit_type, benefit_text)
    return jsonify({"success": True, "message": "تم تقييد الفائدة بنجاح"})

@app.route('/api/benefits/delete', methods=['POST'])
def remove_benefit():
    """منفذ لحذف فائدة معينة بشكل آمن"""
    data = request.json
    benefit_id = data.get('benefit_id')
    user_id = data.get('user_id')
    
    if not benefit_id or not user_id:
        return jsonify({"error": "بيانات غير مكتملة"}), 400
        
    delete_benefit(benefit_id, user_id)
    return jsonify({"success": True, "message": "تم حذف الفائدة"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
