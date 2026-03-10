# 🏭 Inventory Extraction Pipeline (Phase 1)

هذا المشروع عبارة عن نظام أتمتة لاستخراج تقارير المخزون من قاعدة بيانات **SQL Server** باستخدام **Python** و **SQLAlchemy**. صُمم النظام ليكون مرناً، آمناً، ومنظماً وفق أفضل ممارسات هندسة البيانات.

## 🌟 ميزات المشروع (Key Features)
*   **Decoupled Architecture:** فصل الإعدادات (`config.py`) عن الدوال المساعدة (`utils.py`) عن الكود التنفيذي (`extract.py`).
*   **Secure Authentication:** إدارة كاملة للبيانات الحساسة عبر ملفات `.env` لضمان عدم تسريب كلمات المرور.
*   **Smart WSL Connectivity:** التعرف التلقائي على IP المضيف عند التشغيل داخل بيئة WSL.
*   **Professional Logging:** نظام تتبع كامل للعمليات والأخطاء مع دعم للغة العربية (UTF-8).
*   **Data Validation:** التحقق من وجود جميع المتغيرات والبيانات قبل بدء المعالجة.

---

## 🏗️ هيكلية المشروع (Project Structure)
```text
├── config.py          # إدارة الإعدادات والـ Logging
├── utils.py           # وظائف مساعدة (مثل جلب الـ IP)
├── extract.py         # الكود الرئيسي لاستخراج البيانات وتصديرها
├── requirements.txt   # المكتبات المطلوبة للتشغيل
├── .env.example       # نموذج لملف الإعدادات السرية
└── .gitignore         # استبعاد الملفات غير الضرورية والحساسة

---

🛠️ كيف تبدأ (Getting Started)
1. المتطلبات (Prerequisites)
    ● تثبيت Python 3.10+
    ● تثبيت ODBC Driver 18 for SQL Server.
    ● قاعدة بيانات SQL Server تحتوي على جداول Sales.Products و Sales.Inventory.

2. التثبيت (Installation)
    1.قم بتحميل المستودع:
    git clone [https://github.com/yourusername/inventory-extraction.git](https://github.com/yourusername/inventory-extraction.git)
    cd inventory-extraction

    2.قم بإنشاء بيئة افتراضية وتفعيلها:
    python -m venv venv
    source venv/bin/activate  # لـ Linux/WSL

    3.تثبيت المكتبات:
    pip install -r requirements.txt

3. الإعداد (Configuration)
قم بإنشاء ملف .env بناءً على .env.example وأضف بيانات الاتصال الخاصة بك.

🚀 التشغيل (Usage)
لتشغيل عملية الاستخراج وتوليد تقرير الإكسل:
python extract.py
ستجد التقرير الناتج في مجلد output/ والسجلات في data/app.log.

🎯 خريطة الطريق للمستقبل (Future Roadmap - Phase 2)
    ● [ ] تحويل المشروع بالكامل إلى حاوية Docker.
    ● [ ] إضافة اختبارات وحدات (Unit Tests) لضمان جودة البيانات.
    ● [ ] دعم قواعد بيانات سحابية (مثل PostgreSQL على AWS/Azure).
    ● [ ] أتمتة التشغيل (Scheduling) باستخدام Airflow أو Cron Jobs.

🤝 المساهمة
المشروع مفتوح للمساهمات! لا تتردد في فتح Issue أو تقديم Pull Request.