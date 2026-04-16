import streamlit as st
import datetime
import pandas as pd

# 1. PAGE CONFIGURATION
st.set_page_config(page_title="CERV-2026: PAYTRANS-EU MASTERPLAN", layout="wide")

# 2. ADVANCED CSS STYLING (Institutional EU Theme)
st.markdown("""
    <style>
    .main { background-color: #f4f7f9; }
    .ue-header { background-color: #003399; color: #ffffff; padding: 30px; border-radius: 10px; text-align: center; margin-bottom: 25px; }
    .tag-box { background-color: #e9ecef; color: #495057; padding: 4px 10px; border-radius: 5px; font-family: monospace; font-size: 0.85em; border: 1px solid #ced4da; }
    .task-card { background-color: #ffffff; border-left: 5px solid #003399; padding: 20px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 15px; }
    .input-req { color: #d32f2f; font-weight: bold; background-color: #fff8f8; padding: 10px; border-radius: 5px; border: 1px dashed #d32f2f; margin-top: 10px; }
    .kpi-metric { background-color: #ffffff; padding: 15px; border-radius: 10px; text-align: center; border: 1px solid #e0e0e0; }
    .deadline-sidebar { background-color: #d32f2f; color: white; padding: 15px; border-radius: 8px; text-align: center; font-weight: bold; font-size: 1.1em; }
    </style>
    """, unsafe_allow_html=True)

# 3. SIDEBAR: CRITICAL CONTROLS & COMPLIANCE
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/b/b7/Flag_of_Europe.svg", width=100)
st.sidebar.markdown("<h2 style='color: #003399;'>PayTrans-EU</h2>", unsafe_allow_html=True)
st.sidebar.write("**Coordinator:** Regione Molise (Italy)")
st.sidebar.divider()

# Countdown Logic
deadline_date = datetime.datetime(2026, 4, 28, 17, 0, 0)
days_to_go = (deadline_date - datetime.datetime.now()).days
st.sidebar.markdown(f"""
    <div class="deadline-sidebar">
        🚨 CALL DEADLINE: 28/04/2026<br>
        {max(0, days_to_go)} Days to Submission
    </div>
    """, unsafe_allow_html=True)

st.sidebar.divider()
st.sidebar.warning("**📄 PART B LIMIT: 45 PAGES**")
st.sidebar.info("Excess pages are automatically truncated by the EU portal.")
st.sidebar.success("**💎 PUBLIC BODY STATUS**")
st.sidebar.write("Regione Molise provides FCA Exemption for the whole consortium.")

# 4. MAIN HEADER
st.markdown('<div class="ue-header"><h1>PayTrans-EU: Comprehensive Masterplan</h1><p>Strategic Roadmap for EU Pay Transparency Directive 2023/970 (18 Months)</p></div>', unsafe_allow_html=True)

# 5. TABS
tabs = st.tabs([
    "🎯 Relevance & Needs", 
    "👥 Consortium Setup", 
    "📂 Work Plan & Tasks", 
    "📅 18-Month Timetable", 
    "🛠️ Admin & Compliance"
])

# --- TAB 1: RELEVANCE, NEEDS & OBJECTIVES ---
with tabs[0]:
    st.markdown("### 1.1 Background & 1.2 Needs Analysis <span class='tag-box'>#§PRJ-OBJ-PO§#</span>", unsafe_allow_html=True)
    
    col_bg, col_needs = st.columns(2)
    with col_bg:
        st.subheader("Project Background")
        st.write("""
        The project addresses the urgent transposition of **Directive (EU) 2023/970**. 
        There is a critical "readiness gap" between legal obligations and the operational capacity of SMEs.
        """)
        st.info("**European Added Value:** Involvement of EURES Advisors to ensure cross-border transparency standards.")
    
    with col_needs:
        st.subheader("Needs Analysis (Evidence-Based)")
        st.markdown("""
        * **Macro Level:** Italy's overall gender earnings gap is **43%**. **82% of SMEs** lack gender-neutral systems.
        * **Local Level:** **65% of employers** are unaware of the salary history ban.
        * **Intersectional:** Motherhood penalty results in a **12% wage contraction**.
        """)

    st.divider()
    st.subheader("Specific Objectives (SO) & Target KPIs")
    kpi_col1, kpi_col2, kpi_col3 = st.columns(3)
    
    with kpi_col1:
        st.markdown('<div class="kpi-metric">', unsafe_allow_html=True)
        st.metric("SO1: SMEs Involved", "150 SMEs", "Target M12")
        st.write("90% reduction of unexplained gap < 5%")
        st.markdown('</div>', unsafe_allow_html=True)

    with kpi_col2:
        st.markdown('<div class="kpi-metric">', unsafe_allow_html=True)
        st.metric("SO2: HR Managers", "500 Certified", "Target M18")
        st.write("+40% increase in HR skills")
        st.markdown('</div>', unsafe_allow_html=True)

    with kpi_col3:
        st.markdown('<div class="kpi-metric">', unsafe_allow_html=True)
        st.metric("SO3: Awareness", "5,000 Workers", "Target M18")
        st.write("60% increase in negotiation confidence")
        st.markdown('</div>', unsafe_allow_html=True)

# --- TAB 2: CONSORTIUM SETUP ---
with tabs[1]:
    st.markdown("### 2.2 Consortium Set-up <span class='tag-box'>#§CON-SOR-TUM§#</span>", unsafe_allow_html=True)
    
    partner_data = [
        {"Country": "🇮🇹 IT", "Organization": "Regione Molise", "Role": "Coordinator / WP1 Lead"},
        {"Country": "🇮🇹 IT", "Organization": "Veneto Lavoro", "Role": "Partner / WP2 Lead"},
        {"Country": "🇮🇹 IT", "Organization": "Manpower Italia", "Role": "Partner / WP3 Lead"},
        {"Country": "🇮🇹 IT", "Organization": "AIDP", "Role": "Partner / WP4 Lead"},
        {"Country": "🇫🇷 FR", "Organization": "PWN France", "Role": "Partner / WP5 Co-Lead"},
        {"Country": "🇫🇷 FR", "Organization": "Manpower France", "Role": "Partner / WP4"},
        {"Country": "🇬🇷 GR", "Organization": "KMOP", "Role": "Partner / WP5 Co-Lead"},
        {"Country": "🇮🇪 IE", "Organization": "Matrix Internet", "Role": "Partner / WP5 Lead"},
        {"Country": "🇪🇺 EU", "Organization": "Municipalities", "Role": "Associated/Partners"}
    ]
    st.table(pd.DataFrame(partner_data))

# --- TAB 3: WORK PACKAGES, TASKS & DELIVERABLES ---
with tabs[2]:
    st.markdown("### 4. Work Packages & Activities <span class='tag-box'>#§WRK-PLA-WP§#</span>", unsafe_allow_html=True)
    
    with st.expander("WP1: Management and Coordination (Regione Molise)", expanded=True):
        st.markdown("""
        * **T1.1 General Coordination:** Steering Committees, quality monitoring.
        * **T1.2 Financial Management:** Lump Sum budget coordination.
        * **Deliverables:** D1.1 Consortium Agreement (M2), D1.2 Final Technical Report (M18).
        """)

    with st.expander("WP2: State of Play Analysis (Veneto Lavoro)"):
        st.markdown("""
        * **T2.1 Data Collection:** Legal readiness gap analysis.
        * **T2.2 Best Practice Mapping:** Systematizing the Triveneto model.
        * **Deliverables:** D2.1 Comparative Readiness Gap Report (M5).
        """)

    with st.expander("WP3: Toolkit Development (Manpower Italia)"):
        st.markdown("""
        * **T3.1 Parameters Design:** Gender-neutral job evaluation criteria.
        * **T3.2 IT Development:** Software build and Beta testing.
        * **Deliverables:** D3.1 Dashboard (M10), D3.2 User Manual (M10).
        """)

    with st.expander("WP4: Pilot Implementation (AIDP)"):
        st.markdown("""
        * **T4.1 Territorial Adaptation:** Localizing with EURES Advisor support.
        * **T4.2 Pilots:** Testing in 150 SMEs across IT, FR, GR.
        * **T4.3 HR Training:** Training 500 managers.
        * **Deliverables:** D4.1 HR Training Toolkit (M14), D4.2 Pilot Validation Report (M18).
        """)

    with st.expander("WP5: Awareness & Replicability (Matrix Internet)"):
        st.markdown("""
        * **T5.1 Digital Campaign:** Reaching 5,000 workers.
        * **T5.2 Stakeholder Dialogue:** Policy webinars and events.
        * **T5.3 Impact Evaluation:** KMOP analysis and EU Replicability Roadmap.
        * **Deliverables:** D5.1 Website (M3), D5.2 Replicability Roadmap (M18).
        """)

# --- TAB 4: TIMETABLE ---
with tabs[3]:
    st.markdown("### 4.3 Timetable <span class='tag-box'>#§TIM-ET-ABL§#</span>", unsafe_allow_html=True)
    months = [f"M{i}" for i in range(1, 19)]
    tasks = ["WP1 Management", "WP2 Analysis", "WP3 Dashboard", "WP4 Pilot & HR", "WP5 Awareness"]
    
    df_time = pd.DataFrame(index=tasks, columns=months)
    df_time.loc["WP1 Management", :] = "X"
    df_time.loc["WP2 Analysis", "M1":"M5"] = "X"
    df_time.loc["WP3 Dashboard", "M4":"M10"] = "X"
    df_time.loc["WP4 Pilot & HR", "M9":"M18"] = "X"
    df_time.loc["WP5 Awareness", :] = "X"
    st.dataframe(df_time.fillna(""), width="stretch")

# --- TAB 5: ADMIN & COMPLIANCE ---
with tabs[4]:
    st.header("Administrative Tasks & Compliance")
    col_adm1, col_adm2 = st.columns(2)
    
    with col_adm1:
        st.subheader("1. Registration & Forms")
        st.markdown("""
        * **PIC Code:** Mandatory 9-digit ID.
        * **LEAR:** Legal representative appointment.
        * **Part B:** Narrative proposal (**Max 45 Pages**).
        """)

    with col_adm2:
        st.subheader("2. Financial & Annexes")
        st.markdown("""
        * **Lump Sum:** Budget based on payroll.
        * **Annexes:** CVs, List of Previous Projects.
        """)
        st.success("**COORD ADVANTAGE:** Regione Molise (Public Body) = No Financial Capacity Check (FCA).")

st.divider()
st.caption("PayTrans-EU Coordination Office | Regione Molise | 2026")
