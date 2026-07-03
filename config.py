import os

# إعدادات البوت الأساسية (سيتم جلبها بشكل آمن من البيئة المحيطة أو كتابتها هنا)
BOT_TOKEN = os.getenv("BOT_TOKEN", "ضع_توكن_البوت_هنا_لاحقاً")
WEBAPP_URL = os.getenv("WEBAPP_URL", "ضع_رابط_المنصة_المستضافة_هنا_لاحقاً")

# الداتا المهيكلة للقنوات والمجموعات لتسهيل الصيانة والتحديث مستقبلاً
PLATFORM_DATA = {
    "college": [
        {"name": "قناة الإعلانات الخاصة بالكلية", "url": "https://t.me/MALIKIST_0", "icon": "fa-bullhorn"},
        {"name": "قناة كناشة المتفقه (الفقه المالكي)", "url": "https://t.me/KONASHA_42", "icon": "fa-book-open"},
        {"name": "قناة أصول الفقه", "url": "https://t.me/atafaseelat42", "icon": "fa-gavel"},
        {"name": "قناة تسهيل البيان", "url": "https://t.me/tasheelalbyan_42", "icon": "fa-pen-nib"},
        {"name": "قناة العقيدة", "url": "https://t.me/AQIDIST_3", "icon": "fa-mosque"},
        {"name": "قناة النحو", "url": "https://t.me/NAHWIST_2", "icon": "fa-language"},
        {"name": "قناة مكتبة الإمام مالك", "url": "https://t.me/MALIKBOOKS", "icon": "fa-book"}
    ],
    "useful": [
        {"name": "قناة امتحان إجازة القرآن الكريم", "url": "https://t.me/AletQan24", "icon": "fa-star-and-crescent"},
        {"name": "قناة تائبون وتائبات", "url": "https://t.me/TAWBAH_03", "icon": "fa-heart"},
        {"name": "قناة توعية دينية", "url": "https://t.me/QALBSLEM", "icon": "fa-hand-holding-heart"},
        {"name": "قناة دعم رشد لدعم القنوات السلفية", "url": "https://t.me/M_AX_S42", "icon": "fa-circle-nodes"}
    ],
    "groups": [
        {"name": "مجموعة الطلاب", "url": "https://t.me/+x3KFvbe9YFg4MWM0", "icon": "fa-circle-user"},
        {"name": "مجموعة الطالبات", "url": "https://t.me/+nevPJP3AGjhhYTNk", "icon": "fa-circle-user"}
    ]
}
