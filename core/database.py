import sqlite3
from datetime import datetime

# اسم ملف قاعدة البيانات الذي سيتم إنشاؤه تلقائياً
DB_NAME = "platform_database.db"

def get_db_connection():
    """إنشاء اتصال آمن مع قاعدة البيانات وتفعيل قراءة البيانات كـ Dictionary"""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """إنشاء جدول الفوائد (كناشة المتفقه) عند تشغيل النظام لأول مرة"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS benefits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL,         -- معرف التليجرام الخاص بالطالب لضمان خصوصيته
            benefit_type TEXT NOT NULL,    -- نوع الفائدة (فقهية، حديث، لغة، إلخ)
            benefit_text TEXT NOT NULL,    -- نص الفائدة المكتوب
            created_at TEXT NOT NULL       -- وقت وتاريخ التقييد لترتيب الفوائد زمنيًا
        )
    ''')
    
    conn.commit()
    conn.close()

def add_benefit(user_id, benefit_type, benefit_text):
    """إضافة فائدة جديدة للكناشة"""
    conn = get_db_connection()
    cursor = conn.cursor()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    cursor.execute('''
        INSERT INTO benefits (user_id, benefit_type, benefit_text, created_at)
        VALUES (?, ?, ?, ?)
    ''', (str(user_id), benefit_type, benefit_text, now))
    
    conn.commit()
    conn.close()

def get_user_benefits(user_id):
    """جلب جميع الفوائد الخاصة بطالب معين مرتبة من الأحدث للأقدم"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT * FROM benefits WHERE user_id = ? ORDER BY id DESC
    ''', (str(user_id),))
    
    rows = cursor.fetchall()
    conn.close()
    
    # تحويل البيانات إلى قائمة ديكشنري لسهولة إرسالها للـ Mini App
    return [dict(row) for row in rows]

def delete_benefit(benefit_id, user_id):
    """حذف فائدة معينة والتأكد من أن الحاذف هو صاحب الفائدة لضمان الأمان"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        DELETE FROM benefits WHERE id = ? AND user_id = ?
    ''', (benefit_id, str(user_id)))
    
    conn.commit()
    conn.close()
