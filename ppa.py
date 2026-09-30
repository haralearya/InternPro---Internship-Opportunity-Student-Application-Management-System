import streamlit as st
import pandas as pd
from datetime import datetime

# Page Configuration
st.set_page_config(
    page_title="InternPro - Internship & Application Management",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling & Tailwind-like clean appearance
st.markdown("""
    <style>
    .main { background-color: #f8fafc; }
    .stButton>button { border-radius: 10px; font-weight: 600; }
    .card { background-color: white; padding: 20px; border-radius: 12px; border: 1px solid #e2e8f0; margin-bottom: 16px; box-shadow: 0 1px 3px rgba(0,0,0,0.05); }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# INITIALIZE SESSION STATE DATA
# ---------------------------------------------------------
if "role" not in st.session_state:
    st.session_state.role = "home"  # Options: home, student, employer, admin

if "user_email" not in st.session_state:
    st.session_state.user_email = "student@internpro.com"

if "listings" not in st.session_state:
    st.session_state.listings = [
        {
            "id": 1,
            "title": "Frontend Software Intern",
            "company": "Acme Corp",
            "category": "Software Engineering",
            "location": "Remote",
            "stipend": "$3,500 / mo",
            "deadline": "2026-11-30",
            "description": "Build high-performance accessible web interfaces using modern JS frameworks and Tailwind CSS.",
            "requirements": "Proficiency in JavaScript/TypeScript, HTML/CSS, and React fundamentals.",
            "status": "Active"
        },
        {
            "id": 2,
            "title": "Data Science & AI Intern",
            "company": "NeuralMetrics",
            "category": "Data Science & AI",
            "location": "San Francisco, CA",
            "stipend": "$4,200 / mo",
            "deadline": "2026-12-15",
            "description": "Assist our core ML engineering team in training and evaluating custom language models.",
            "requirements": "Strong Python skills, experience with Pandas, Scikit-Learn, or PyTorch.",
            "status": "Active"
        },
        {
            "id": 3,
            "title": "Product Management Intern",
            "company": "Veloce Inc.",
            "category": "Product Management",
            "location": "New York, NY",
            "stipend": "$3,000 / mo",
            "deadline": "2026-11-20",
            "description": "Gather product requirements, draft user stories, and coordinate cross-functional sprints.",
            "requirements": "Excellent communication skills, technical aptitude, and user-first mindset.",
            "status": "Active"
        }
    ]

if "applications" not in st.session_state:
    st.session_state.applications = [
        {
            "id": 101,
            "job_id": 1,
            "job_title": "Frontend Software Intern",
            "company": "Acme Corp",
            "applicant_name": "Alex Johnson",
            "email": "alex@student.com",
            "cover_letter": "I have built several React apps and love clean UI design.",
            "applied_date": "2026-09-10",
            "status": "Interview",
            "next_action": "Technical Screen on Oct 5"
        }
    ]

if "saved_jobs" not in st.session_state:
    st.session_state.saved_jobs = [2]

if "users" not in st.session_state:
    st.session_state.users = [
        {"id": 1, "name": "Alex Johnson", "email": "alex@student.com", "role": "Student"},
        {"id": 2, "name": "Sarah Recruiter", "email": "sarah@acme.com", "role": "Employer"},
        {"id": 3, "name": "Admin Master", "email": "admin@internpro.com", "role": "Admin"}
    ]

if "selected_employer_job" not in st.session_state:
    st.session_state.selected_employer_job = None


# ---------------------------------------------------------
# HEADER / NAVIGATION BAR
# ---------------------------------------------------------
st.markdown("### 🎓 Intern<span style='color:#6366f1;'>Pro</span> Management System", unsafe_allow_html=True)
nav_col1, nav_col2, nav_col3, nav_col4, nav_col5 = st.columns([2, 1, 1, 1, 1])

with nav_col2:
    if st.button("🏠 Home / Role Select", use_container_width=True):
        st.session_state.role = "home"
        st.rerun()
with nav_col3:
    if st.button("👨‍🎓 Student Portal", use_container_width=True):
        st.session_state.role = "student"
        st.rerun()
with nav_col4:
    if st.button("🏢 Employer Hub", use_container_width=True):
        st.session_state.role = "employer"
        st.rerun()
with nav_col5:
    if st.button("🛡️ Admin Center", use_container_width=True):
        st.session_state.role = "admin"
        st.rerun()

st.markdown("---")


# =========================================================
# VIEW 1: HOME / ROLE SELECTOR
# =========================================================
if st.session_state.role == "home":
    st.markdown("<div style='text-align: center; padding: 20px 0;'>", unsafe_allow_html=True)
    st.markdown("### Connect Top Student Talent with Industry-Leading Employers.")
    st.write("A comprehensive platform featuring intelligent application pipelines, real-time status tracking, and recruiter dashboards.")
    st.markdown("</div>")

    st.markdown("#### ⚡ Role Simulator & Quick Switcher")
    st.write("Select a profile to instantly test the platform from different user perspectives:")

    sim_col1, sim_col2, sim_col3 = st.columns(3)
    with sim_col1:
        if st.button("🎓 Student Portal\nBrowse, apply, save & track statuses", use_container_width=True):
            st.session_state.role = "student"
            st.rerun()
    with sim_col2:
        if st.button("🏢 Employer Portal\nPost roles & evaluate candidates", use_container_width=True):
            st.session_state.role = "employer"
            st.rerun()
    with sim_col3:
        if st.button("🛡️ Admin Dashboard\nSystem analytics & moderation", use_container_width=True):
            st.session_state.role = "admin"
            st.rerun()


# =========================================================
# VIEW 2: STUDENT PORTAL
# =========================================================
elif st.session_state.role == "student":
    st.subheader("Student Career Hub")
    st.write("Discover internships, submit applications, and track your interview pipeline.")

    student_tab = st.radio(
        "Navigation Tabs",
        ["Explore Openings", f"My Applications ({len(st.session_state.applications)})", f"Saved Jobs ({len(st.session_state.saved_jobs)})"],
        horizontal=True,
        label_visibility="collapsed"
    )

    st.markdown("---")

    # --- TAB 1: BROWSE & SEARCH ---
    if student_tab == "Explore Openings":
        f_col1, f_col2, f_col3 = st.columns(3)
        with f_col1:
            keyword = st.text_input("🔍 Search Keyword", placeholder="Job title, company, skill...")
        with f_col2:
            categories = ["All Categories"] + list(set([j["category"] for j in st.session_state.listings]))
            selected_cat = st.selectbox("Category Filter", categories)
        with f_col3:
            locations = ["All Locations"] + list(set([j["location"] for j in st.session_state.listings]))
            selected_loc = st.selectbox("Location Filter", locations)

        # Filter active listings
        active_listings = [j for j in st.session_state.listings if j.get("status", "Active") == "Active"]
        if keyword:
            active_listings = [j for j in active_listings if keyword.lower() in j["title"].lower() or keyword.lower() in j["company"].lower()]
        if selected_cat != "All Categories":
            active_listings = [j for j in active_listings if j["category"] == selected_cat]
        if selected_loc != "All Locations":
            active_listings = [j for j in active_listings if j["location"] == selected_loc]

        if not active_listings:
            st.info("No matching internship opportunities found.")
        else:
            for job in active_listings:
                with st.container():
                    st.markdown(f"""
                    <div class='card'>
                        <span style='background-color: #eef2ff; color: #4338ca; padding: 3px 8px; border-radius: 12px; font-size: 11px; font-weight: 600;'>{job['category']}</span>
                        <h4 style='margin-top: 8px; margin-bottom: 4px;'>{job['title']}</h4>
                        <p style='color: #64748b; font-size: 13px; margin-bottom: 8px;'>🏢 {job['company']} &nbsp;|&nbsp; 📍 {job['location']} &nbsp;|&nbsp; 💰 {job['stipend']}</p>
                        <p style='font-size: 14px;'>{job['description']}</p>
                    </div>
                    """, unsafe_allow_html=True)

                    btn_col1, btn_col2, _ = st.columns([1, 1, 3])
                    with btn_col1:
                        is_saved = job["id"] in st.session_state.saved_jobs
                        save_label = "❤️ Saved" if is_saved else "🤍 Save Job"
                        if st.button(save_label, key=f"save_{job['id']}"):
                            if is_saved:
                                st.session_state.saved_jobs.remove(job["id"])
                            else:
                                st.session_state.saved_jobs.append(job["id"])
                            st.rerun()

                    with btn_col2:
                        if st.button("🚀 Apply Now", key=f"apply_btn_{job['id']}"):
                            st.session_state[f"modal_apply_{job['id']}"] = True

                    # Application Form Expander/Modal simulation
                    if st.session_state.get(f"modal_apply_{job['id']}", False):
                        with st.form(key=f"form_apply_{job['id']}"):
                            st.markdown(f"**Applying for {job['title']} at {job['company']}**")
                            app_name = st.text_input("Full Name", value="Alex Johnson")
                            app_email = st.text_input("Email Address", value="alex@student.com")
                            cover = st.text_area("Cover Letter & Motivation", placeholder="Briefly explain why you're a great fit...")
                            
                            sub_col1, sub_col2 = st.columns(2)
                            with sub_col1:
                                submitted = st.form_submit_button("Submit Application")
                            with sub_col2:
                                cancelled = st.form_submit_button("Cancel")

                            if submitted:
                                new_app = {
                                    "id": len(st.session_state.applications) + 1,
                                    "job_id": job["id"],
                                    "job_title": job["title"],
                                    "company": job["company"],
                                    "applicant_name": app_name,
                                    "email": app_email,
                                    "cover_letter": cover,
                                    "applied_date": datetime.now().strftime("%Y-%m-%d"),
                                    "status": "Submitted",
                                    "next_action": "Under Recruiter Review"
                                }
                                st.session_state.applications.append(new_app)
                                st.session_state[f"modal_apply_{job['id']}"] = False
                                st.success("Application submitted successfully!")
                                st.rerun()
                            if cancelled:
                                st.session_state[f"modal_apply_{job['id']}"] = False
                                st.rerun()

    # --- TAB 2: APPLICATIONS TRACKER ---
    elif student_tab.startswith("My Applications"):
        st.markdown("#### Submitted Applications Pipeline")
        if not st.session_state.applications:
            st.info("You haven't submitted any applications yet.")
        else:
            app_df = pd.DataFrame(st.session_state.applications)
            for idx, row in app_df.iterrows():
                st.markdown(f"""
                <div class='card'>
                    <b>{row['job_title']}</b> @ {row['company']}<br>
                    <span style='font-size: 12px; color: #64748b;'>Applied Date: {row['applied_date']} &nbsp;|&nbsp; Status: <b>{row['status']}</b></span><br>
                    <span style='font-size: 13px; color: #4338ca;'>Next Action: {row['next_action']}</span>
                </div>
                """, unsafe_allow_html=True)

    # --- TAB 3: SAVED JOBS ---
    elif student_tab.startswith("Saved Jobs"):
        st.markdown("#### Saved Internship Bookmarks")
        saved_list = [j for j in st.session_state.listings if j["id"] in st.session_state.saved_jobs]
        if not saved_list:
            st.info("No saved internships found.")
        else:
            for job in saved_list:
                st.markdown(f"""
                <div class='card'>
                    <h4>{job['title']}</h4>
                    <p style='color: #64748b; font-size: 13px;'>🏢 {job['company']} &nbsp;|&nbsp; 📍 {job['location']} &nbsp;|&nbsp; 💰 {job['stipend']}</p>
                    <p style='font-size: 14px;'>{job['description']}</p>
                </div>
                """, unsafe_allow_html=True)


# =========================================================
# VIEW 3: EMPLOYER PORTAL
# =========================================================
elif st.session_state.role == "employer":
    st.subheader("Employer Dashboard")
    st.write("Post listings, manage active recruitment pipeline, and evaluate candidates.")

    # Metrics Summary
    emp_jobs = st.session_state.listings
    total_apps = len(st.session_state.applications)
    shortlisted_apps = len([a for a in st.session_state.applications if a["status"] in ["Shortlisted", "Interview"]])

    m_col1, m_col2, m_col3 = st.columns(3)
    with m_col1:
        st.metric("Active Postings", len(emp_jobs))
    with m_col2:
        st.metric("Total Applicants", total_apps)
    with m_col3:
        st.metric("Shortlisted / Interview", shortlisted_apps)

    st.markdown("---")

    col_left, col_right = st.columns([1, 2])

    with col_left:
        st.markdown("#### Your Postings")
        if st.button("➕ Post New Internship"):
            st.session_state.show_post_form = True

        for job in emp_jobs:
            if st.button(f"{job['title']} ({job['company']})", key=f"emp_job_{job['id']}", use_container_width=True):
                st.session_state.selected_employer_job = job["id"]

        # Post Job Form Expander
        if st.session_state.get("show_post_form", False):
            with st.form("new_job_form"):
                st.markdown("**Create Internship Posting**")
                nj_title = st.text_input("Internship Title")
                nj_company = st.text_input("Company Name")
                nj_cat = st.selectbox("Category", ["Software Engineering", "Data Science & AI", "Product Management", "UI/UX Design", "Marketing & Growth"])
                nj_loc = st.selectbox("Location", ["Remote", "Hybrid", "San Francisco, CA", "New York, NY", "Austin, TX"])
                nj_stipend = st.text_input("Stipend", value="$3,000 / mo")
                nj_desc = st.text_area("Description")
                nj_req = st.text_area("Requirements")

                sub_c1, sub_c2 = st.columns(2)
                with sub_c1:
                    posted = st.form_submit_button("Publish Posting")
                with sub_c2:
                    cancelled = st.form_submit_button("Cancel")

                if posted and nj_title and nj_company:
                    new_listing = {
                        "id": len(st.session_state.listings) + 1,
                        "title": nj_title,
                        "company": nj_company,
                        "category": nj_cat,
                        "location": nj_loc,
                        "stipend": nj_stipend,
                        "deadline": "2026-12-31",
                        "description": nj_desc,
                        "requirements": nj_req,
                        "status": "Active"
                    }
                    st.session_state.listings.append(new_listing)
                    st.session_state.show_post_form = False
                    st.success("New internship posted successfully!")
                    st.rerun()
                elif cancelled:
                    st.session_state.show_post_form = False
                    st.rerun()

    with col_right:
        selected_id = st.session_state.get("selected_employer_job")
        if not selected_id:
            st.info("Select an internship posting on the left to review applicants.")
        else:
            current_job = next((j for j in st.session_state.listings if j["id"] == selected_id), None)
            if current_job:
                st.markdown(f"#### Applicants for: {current_job['title']}")
                job_apps = [a for a in st.session_state.applications if a["job_id"] == selected_id]

                if not job_apps:
                    st.write("No candidates have applied to this posting yet.")
                else:
                    for app in job_apps:
                        with st.container():
                            st.markdown(f"""
                            <div class='card'>
                                <b>Candidate:</b> {app['applicant_name']} ({app['email']})<br>
                                <b>Cover Letter:</b> {app['cover_letter']}<br>
                                <b>Status:</b> <span style='color: #4338ca; font-weight: 600;'>{app['status']}</span>
                            </div>
                            """, unsafe_allow_html=True)

                            act_c1, act_c2 = st.columns(2)
                            with act_c1:
                                if st.button("✅ Shortlist Candidate", key=f"short_{app['id']}"):
                                    app["status"] = "Shortlisted"
                                    app["next_action"] = "Scheduled for Initial Screen"
                                    st.success(f"Shortlisted {app['applicant_name']}")
                                    st.rerun()
                            with act_c2:
                                if st.button("❌ Reject", key=f"rej_{app['id']}"):
                                    app["status"] = "Rejected"
                                    app["next_action"] = "Archived"
                                    st.rerun()


# =========================================================
# VIEW 4: ADMIN DASHBOARD
# =========================================================
elif st.session_state.role == "admin":
    st.subheader("Admin Control Center")
    st.write("System analytics, user management, and global job posting moderation.")

    # Analytics Cards
    a_col1, a_col2, a_col3, a_col4 = st.columns(4)
    with a_col1:
        st.metric("Total Users", len(st.session_state.users))
    with a_col2:
        st.metric("Total Job Postings", len(st.session_state.listings))
    with a_col3:
        st.metric("Total Applications", len(st.session_state.applications))
    with a_col4:
        active_companies = len(set([j["company"] for j in st.session_state.listings]))
        st.metric("Active Companies", active_companies)

    st.markdown("---")

    st.markdown("#### User Accounts Management")
    for user in st.session_state.users:
        col_u1, col_u2, col_u3 = st.columns([3, 2, 1])
        with col_u1:
            st.write(f"**{user['name']}** ({user['email']})")
        with col_u2:
            st.write(f"Role: {user['role']}")
        with col_u3:
            if st.button("🗑️ Delete", key=f"del_user_{user['id']}"):
                st.session_state.users = [u for u in st.session_state.users if u["id"] != user["id"]]
                st.rerun()

    st.markdown("---")
    st.markdown("#### Global Internship Moderation")
    for job in st.session_state.listings:
        col_j1, col_j2, col_j3 = st.columns([3, 2, 1])
        with col_j1:
            st.write(f"**{job['title']}** at {job['company']}")
        with col_j2:
            st.write(f"Category: {job['category']}")
        with col_j3:
            if st.button("🚫 Remove", key=f"mod_job_{job['id']}"):
                st.session_state.listings = [j for j in st.session_state.listings if j["id"] != job["id"]]
                st.rerun()