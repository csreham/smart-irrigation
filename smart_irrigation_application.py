import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import plotly.express as px
import plotly.graph_objects as go

# صفحة الإعدادات
st.set_page_config(
    page_title="نظام الري الذكي للنخيل",
    page_icon="🌴",
    layout="wide",
    initial_sidebar_state="expanded"
)

# تخصيص الأنماط
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Arabic:wght@300;400;500;600;700&display=swap');
    
    * {
        font-family: 'Noto Sans Arabic', sans-serif;
    }
    
    .main-header {
        text-align: center;
        color: #2E8B57;
        padding: 20px;
        background: linear-gradient(135deg, #F5F5DC 0%, #FFF8DC 100%);
        border-radius: 10px;
        margin-bottom: 30px;
        border: 2px solid #DAA520;
    }
    
    .palm-card {
        background: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        border-right: 5px solid #2E8B57;
        margin-bottom: 15px;
    }
    
    .sensor-card {
        background: #f8f9fa;
        padding: 15px;
        border-radius: 10px;
        border-left: 4px solid #007bff;
    }
    
    .alert-card {
        background: #fff3cd;
        padding: 15px;
        border-radius: 10px;
        border-left: 4px solid #ffc107;
    }
    
    .success-card {
        background: #d4edda;
        padding: 15px;
        border-radius: 10px;
        border-left: 4px solid #28a745;
    }
    
    .metric-card {
        text-align: center;
        padding: 20px;
        background: white;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# شريط القائمة الجانبية
with st.sidebar:
    st.markdown("<h2 style='text-align: center; color: #2E8B57;'>🌴 مزرعتي الذكية</h2>", unsafe_allow_html=True)
    
    selected = option_menu(
        menu_title=None,
        options=["🏠 لوحة التحكم", "🌴 النخيل", "💧 نظام الري", "📡 الأجهزة", "📊 التقارير", "⚙️ الإعدادات"],
        icons=["house", "tree", "droplet", "router", "bar-chart", "gear"],
        menu_icon="cast",
        default_index=0,
        orientation="vertical",
        styles={
            "container": {"padding": "0!important", "background-color": "#f8f9fa"},
            "icon": {"color": "#2E8B57", "font-size": "18px"},
            "nav-link": {"font-size": "16px", "text-align": "right", "margin": "0px"},
            "nav-link-selected": {"background-color": "#2E8B57"},
        }
    )

# محاكاة بيانات النخيل
def generate_palm_data(num_palms=50):
    palms = []
    for i in range(1, num_palms + 1):
        palms.append({
            "id": i,
            "name": f"نخلة {i}",
            "type": np.random.choice(["خلاص", "صقعي", "مجهول", "برحي", "سلطان"]),
            "age": np.random.randint(3, 30),
            "moisture": np.random.uniform(15, 65),
            "temperature": np.random.uniform(20, 45),
            "humidity": np.random.uniform(20, 80),
            "battery": np.random.uniform(20, 100),
            "status": np.random.choice(["✅ ممتاز", "⚠️ يحتاج مراقبة", "🚨 عطشان"], p=[0.7, 0.25, 0.05]),
            "last_irrigation": datetime.now() - timedelta(hours=np.random.randint(0, 168)),
            "water_needed": np.random.choice([True, False], p=[0.3, 0.7]),
            "location_x": np.random.uniform(0, 100),
            "location_y": np.random.uniform(0, 100)
        })
    return pd.DataFrame(palms)

# تحميل البيانات
if 'palms_data' not in st.session_state:
    st.session_state.palms_data = generate_palm_data()

# صفحة لوحة التحكم
if selected == "🏠 لوحة التحكم":
    st.markdown("<div class='main-header'><h1>🌴 لوحة التحكم - نظام الري الذكي</h1></div>", unsafe_allow_html=True)
    
    # صف المؤشرات
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class='metric-card'>
            <h3>👑 النخيل</h3>
            <h2 style='color: #2E8B57;'>50</h2>
            <p>إجمالي النخيل في المزرعة</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='metric-card'>
            <h3>💧 توفير المياه</h3>
            <h2 style='color: #007bff;'>85%</h2>
            <p>مقارنة بالري التقليدي</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class='metric-card'>
            <h3>💰 توفير مالي</h3>
            <h2 style='color: #28a745;'>2,100 ريال</h2>
            <p>توفير شهري</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class='metric-card'>
            <h3>⚡ الطاقة</h3>
            <h2 style='color: #ffc107;'>100%</h2>
            <p>طاقة شمسية متجددة</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    # صف الرسوم البيانية
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📈 توزيع رطوبة التربة")
        moisture_data = st.session_state.palms_data['moisture']
        fig = px.histogram(moisture_data, nbins=20, color_discrete_sequence=['#2E8B57'])
        fig.update_layout(xaxis_title="نسبة الرطوبة (%)", yaxis_title="عدد النخيل", showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("🌡️ حرارة التربة الحالية")
        temp_data = st.session_state.palms_data['temperature']
        fig = go.Figure(data=[go.Box(y=temp_data, name="حرارة التربة", marker_color='#DAA520')])
        fig.update_layout(yaxis_title="درجة الحرارة (°C)", showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

# صفحة إدارة النخيل
elif selected == "🌴 النخيل":
    st.markdown("<div class='main-header'><h1>🌴 إدارة النخيل</h1></div>", unsafe_allow_html=True)
    
    # فلترات البحث
    col1, col2, col3 = st.columns(3)
    with col1:
        palm_type = st.selectbox("نوع النخلة", ["جميع الأنواع", "خلاص", "صقعي", "مجهول", "برحي", "سلطان"])
    with col2:
        status_filter = st.selectbox("الحالة", ["جميع الحالات", "✅ ممتاز", "⚠️ يحتاج مراقبة", "🚨 عطشان"])
    with col3:
        min_moisture = st.slider("الحد الأدنى للرطوبة", 0, 100, 0)
    
    st.divider()
    
    # عرض بيانات النخيل
    st.subheader("قائمة النخيل")
    
    # فلترة البيانات
    filtered_data = st.session_state.palms_data.copy()
    if palm_type != "جميع الأنواع":
        filtered_data = filtered_data[filtered_data['type'] == palm_type]
    if status_filter != "جميع الحالات":
        filtered_data = filtered_data[filtered_data['status'] == status_filter]
    filtered_data = filtered_data[filtered_data['moisture'] >= min_moisture]
    
    # عرض البيانات
    for _, palm in filtered_data.iterrows():
        col1, col2, col3 = st.columns([3, 1, 1])
        
        with col1:
            st.markdown(f"""
            <div class='palm-card'>
                <h4>{palm['name']} - {palm['type']}</h4>
                <p>العمر: {palm['age']} سنة | الرطوبة: {palm['moisture']:.1f}%</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            if palm['status'] == "🚨 عطشان":
                st.error(palm['status'])
            elif palm['status'] == "⚠️ يحتاج مراقبة":
                st.warning(palm['status'])
            else:
                st.success(palm['status'])
        
        with col3:
            if palm['water_needed']:
                if st.button(f"💧 ري الآن", key=f"water_{palm['id']}"):
                    st.success(f"تم بدء ري {palm['name']}")
            else:
                st.info("لا يحتاج ري")

# صفحة نظام الري
elif selected == "💧 نظام الري":
    st.markdown("<div class='main-header'><h1>💧 نظام الري الذكي</h1></div>", unsafe_allow_html=True)
    
    # التحكم اليدوي
    st.subheader("🎮 التحكم اليدوي في الري")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        palm_select = st.selectbox("اختر النخلة للري", [f"نخلة {i}" for i in range(1, 51)])
    with col2:
        duration = st.slider("مدة الري (دقيقة)", 1, 120, 30)
    with col3:
        water_volume = st.number_input("كمية المياه (لتر)", 10, 1000, 200)
    
    if st.button("🚿 بدء الري", type="primary"):
        st.success(f"بدأ ري {palm_select} لمدة {duration} دقيقة")

# صفحة الأجهزة
elif selected == "📡 الأجهزة":
    st.markdown("<div class='main-header'><h1>📡 إدارة الأجهزة</h1></div>", unsafe_allow_html=True)
    
    st.subheader("أجهزة النظام")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("أجهزة الاستشعار", "50", "100% نشطة")
    with col2:
        st.metric("البوابات الذكية", "5", "80% نشطة")
    with col3:
        st.metric("طاقة شمسية", "3-10 واط", "لكل جهاز")
    
    st.info("جميع الأجهزة تعمل بالطاقة الشمسية وتتواصل عبر LoRaWAN")

# صفحة التقارير
elif selected == "📊 التقارير":
    st.markdown("<div class='main-header'><h1>📊 التقارير والتحليلات</h1></div>", unsafe_allow_html=True)
    
    # فلتر الفترة الزمنية
    col1, col2 = st.columns(2)
    with col1:
        report_type = st.selectbox("نوع التقرير", ["تقرير شهري", "تقرير أسبوعي", "تقرير يومي"])
    with col2:
        if st.button("📥 تصدير التقرير"):
            st.success("جاري إنشاء التقرير...")
    
    # تبويبات التقارير
    tab1, tab2, tab3, tab4 = st.tabs(["📈 التوفير المائي", "💰 التوفير المالي", "⚡ كفاءة الطاقة", "📋 ملخص شامل"])
    
    with tab1:
        st.subheader("توفير المياه")
        # بيانات وهمية
        dates = pd.date_range('2024-01-01', '2024-12-01', freq='MS')
        water_saving = np.random.uniform(70, 90, len(dates))
        
        fig = px.line(x=dates, y=water_saving, title="توفير المياه الشهري")
        fig.update_layout(xaxis_title="الشهر", yaxis_title="نسبة التوفير %")
        st.plotly_chart(fig, use_container_width=True)
        
        st.metric("متوسط التوفير السنوي", f"{np.mean(water_saving):.1f}%")
    
    with tab2:
        st.subheader("التوفير المالي")
        # بيانات وهمية
        months = ['يناير', 'فبراير', 'مارس', 'أبريل', 'مايو', 'يونيو']
        savings = [1500, 1800, 2100, 1900, 2200, 2400]
        
        fig = px.bar(x=months, y=savings, title="التوفير المالي الشهري")
        fig.update_layout(xaxis_title="الشهر", yaxis_title="التوفير (ريال)")
        st.plotly_chart(fig, use_container_width=True)
        
        st.metric("إجمالي التوفير السنوي", f"{sum(savings):,} ريال")
    
    with tab3:
        st.subheader("كفاءة الطاقة الشمسية")
        # بيانات الطاقة الشمسية
        energy_sources = pd.DataFrame({
            'المصدر': ['الطاقة الشمسية', 'البطاريات', 'الشبكة الكهربائية'],
            'النسبة': [85, 10, 5]
        })
        
        fig = px.pie(energy_sources, values='النسبة', names='المصدر', 
                     title="مصادر الطاقة في النظام")
        st.plotly_chart(fig, use_container_width=True)
        
        st.success("✅ النظام يعتمد بنسبة 85% على الطاقة الشمسية المتجددة")
    
    with tab4:
        st.subheader("ملخص أداء النظام الشامل")
        
        summary_data = {
            'المؤشر': ['توفير المياه', 'التوفير المالي', 'كفاءة الري', 'طاقة شمسية'],
            'القيمة': ['85%', '2,100 ريال/شهر', '95%', '85%'],
            'التقييم': ['ممتاز 🏆', 'ممتاز 🏆', 'ممتاز 🏆', 'ممتاز 🏆']
        }
        
        summary_df = pd.DataFrame(summary_data)
        st.dataframe(summary_df, use_container_width=True, hide_index=True)
        
        st.subheader("💡 توصيات النظام")
        recommendations = [
            "✅ زيادة وقت الري للنخيل في المنطقة الشمالية",
            "⚠️ فحص أجهزة الاستشعار منخفضة البطارية",
            "📈 الوقت الأمثل للري: 5:30 - 6:30 صباحاً",
            "🌱 تعديل جدول الري حسب الطقس"
        ]
        
        for rec in recommendations:
            st.info(rec)

# صفحة الإعدادات
elif selected == "⚙️ الإعدادات":
    st.markdown("<div class='main-header'><h1>⚙️ إعدادات النظام</h1></div>", unsafe_allow_html=True)
    
    st.subheader("الإعدادات العامة")
    
    with st.form("settings_form"):
        col1, col2 = st.columns(2)
        with col1:
            system_name = st.text_input("اسم النظام", "مزرعتي الذكية")
            language = st.selectbox("اللغة", ["العربية", "English"])
        with col2:
            notifications = st.checkbox("تفعيل الإشعارات", True)
            auto_update = st.checkbox("التحديث التلقائي", True)
        
        st.subheader("إعدادات الري")
        irrigation_time = st.time_input("وقت الري الافتراضي", datetime.now().time())
        max_duration = st.slider("الحد الأقصى لمدة الري (دقيقة)", 1, 120, 60)
        
        submitted = st.form_submit_button("💾 حفظ الإعدادات")
        if submitted:
            st.success("تم حفظ الإعدادات بنجاح!")
            st.balloons()

# Footer
st.divider()
st.markdown("""
<div style='text-align: center; color: #666; padding: 20px;'>
    <p>🌴 نظام الري الذكي للنخيل | طاقة شمسية + TinyML + LoRaWAN</p>
    <p>📞 للدعم الفني: 0551234567 | 📧 info@mazraati.sa</p>
</div>
""", unsafe_allow_html=True)