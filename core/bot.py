import logging
import asyncio
from telegram import Update, WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes
import config

# تفعيل تسجيل الأخطاء (Logs) لمراقبة الأداء
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """أمر البدء /start لإرسال رسالة ترحيبية أنيقة مع زر تشغيل المنصة"""
    user_name = update.effective_user.first_name
    
    welcome_message = (
        f"مرحباً بك يا شيخ {user_name} في **منصة الإمام مالك التعليمية** 🏛️\n\n"
        "المرجع التعليمي والدليل الشامل لطلاب الكلية داخل تيليجرام.\n"
        "يمكنك الآن تصفح القنوات الرسمية، المجموعات، وتقييد فوائدك العلمية عبر الكناشة الذكية."
    )
    
    # ربط البوت برابط الـ Mini Web App الخاص بنا من ملف الإعدادات
    keyboard = [
        [
            InlineKeyboardButton(
                text="🏛️ فتح منصة الإمام مالك", 
                web_app=WebAppInfo(url=config.WEBAPP_URL)
            )
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(welcome_message, reply_markup=reply_markup, parse_mode="Markdown")

def main() -> None:
    """تشغيل ومراقبة البوت باستمرار بشكل متوافق مع خوادم الويب"""
    if config.BOT_TOKEN == "ضع_توكن_البوت_هنا_لاحقاً":
        logger.warning("برجاء وضع BOT_TOKEN الحقيقي في ملف config.py أولاً لكي يعمل البوت!")
        return

    # بناء التطبيق وإدخل التوكن الخاص بنا
    application = Application.builder().token(config.BOT_TOKEN).build()

    # تسجيل الأوامر
    application.add_handler(CommandHandler("start", start))

    # التعديل الاحترافي للتشغيل المتوازي الآمن داخل خلفية النظام (Thread) منعاً للتوقف
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        logger.info("بدء استقبال تحديثات تيليجرام بنجاح...")
        application.run_polling(allowed_updates=Update.ALL_TYPES, close_loop=False)
    except Exception as e:
        logger.error(f"حدث خطأ أثناء تشغيل البوت: {e}")

if __name__ == '__main__':
    main()
