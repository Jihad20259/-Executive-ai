# Weather Dashboard

Weather Dashboard هو تطبيق ويب يعرض بيانات الطقس الحية لأي مدينة أو موقع عالمي.

## التقنيات المستخدمة
- **الواجهة الخلفية**: Python (FastAPI)
- **الواجهة الأمامية**: React
- **API الطقس**: OpenWeatherMap

## الميزات:
- البحث عن الطقس باستخدام اسم المدينة
- عرض درجة الحرارة، الرطوبة، حالة السماء، وسرعة الرياح
- واجهة استخدام بسيطة وحديثة
- فصل تام بين الواجهة الأمامية والخلفية

## التشغيل المحلي

### 1. إعداد الواجهة الخلفية (FastAPI)
```bash
cd backend
pip install -r requirements.txt
cp .env.example .env # أضف مفتاح OpenWeatherMap في .env
uvicorn main:app --reload
```

### 2. إعداد الواجهة الأمامية (React)
```bash
cd frontend
npm install
npm start
```

واجهة الويب متوفرة على http://localhost:3000
واجهة الـ API متوفرة على http://localhost:8000

