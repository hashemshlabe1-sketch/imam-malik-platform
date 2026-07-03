import threading
import time
import logging
from core.webapp import app
from core.bot import main as run_bot

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("MainSystem")

def start_webapp():
    """تشغيل خادم الويب الخاص بالواجهة والـ API"""
    logger.info("جاري تشغيل خادم الويب والواجهات...")
    # تشغيل الفلاسک على المنفذ 5000
    app.run(host='0.0.0.0', port=5000, use_reloader=False, threaded=True)

if __name__ == '__main__':
    # 1. تشغيل خادم الويب في خلفية النظام (Background Thread)
    web_thread = threading.Thread(target=start_webapp)
    web_thread.daemon = True
    web_thread.start()
    
    # إعطاء السيرفر ثانية واحدة ليستقر قبل تشغيل البوت
    time.sleep(1)
    
    # 2. تشغيل محرك البوت الذكي في المسار الرئيسي
    logger.info("جاري تشغيل محرك البوت لتيليجرام...")
    run_bot()
