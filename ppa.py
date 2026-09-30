import streamlit as st
import streamlit.components.v1 as components

# Page Configuration
st.set_page_config(
    page_title="InternPro - Internship Opportunity & Student Application Management System",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit default header, footer, and sidebar to let your pure HTML design shine
hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {padding: 0 !important; max-width: 100% !important;}
    </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

# The Full Original HTML/CSS/JS Code Embedded as-is
html_code = """
<!DOCTYPE html>
<html lang="en" class="h-full">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>InternPro - Internship Opportunity & Student Application Management System</title>
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- FontAwesome Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: { sans: ['Inter', 'sans-serif'] },
                    colors: {
                        brand: {
                            50: '#eef2ff',
                            100: '#e0e7ff',
                            500: '#6366f1',
                            600: '#4f46e5',
                            700: '#4338ca',
                        }
                    }
                }
            }
        }
    </script>
    <style>
        body { font-family: 'Inter', sans-serif; }
        .fade-in { animation: fadeIn 0.25s ease-in-out forwards; }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(4px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>
</head>
<body class="h-full bg-slate-50 text-slate-800 flex flex-col justify-between">

    <header class="bg-white border-b border-slate-200 sticky top-0 z-40 shadow-sm">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
            <div class="flex items-center space-x-3 cursor-pointer" onclick="switchView('home')">
                <div class="w-10 h-10 rounded-xl bg-indigo-600 flex items-center justify-center text-white shadow-md">
                    <i class="fa-solid fa-graduation-cap text-xl"></i>
                </div>
                <div>
                    <span class="text-xl font-bold tracking-tight text-slate-900">Intern<span class="text-indigo-600">Pro</span></span>
                    <span class="hidden sm:inline-block ml-2 text-xs font-medium px-2 py-0.5 bg-indigo-50 text-indigo-700 rounded-full border border-indigo-100">Management System</span>
                </div>
            </div>

            <div class="flex items-center space-x-4">
                <div id="navLinks" class="hidden md:flex items-center space-x-3 text-sm font-medium text-slate-600">
                    <!-- Nav links injected via JS -->
                </div>
                <div id="authNavbarContainer" class="flex items-center space-x-2">
                    <!-- Auth status injected via JS -->
                </div>
            </div>
        </div>
    </header>

    <main class="flex-grow max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-8">
        
        <!-- Toast Notification Container -->
        <div id="toastContainer" class="fixed bottom-5 right-5 z-50 flex flex-col space-y-2 pointer-events-none"></div>

        <!-- VIEW 1: HOME / LANDING & QUICK ROLE SWITCHER -->
        <section id="viewHome" class="view-section fade-in">
            <div class="py-12 md:py-20 text-center max-w-3xl mx-auto">
                <span class="inline-flex items-center px-3 py-1 rounded-full text-xs font-semibold bg-indigo-100 text-indigo-800 mb-6">
                    <i class="fa-solid fa-bolt mr-1.5"></i> Streamlined Career & Placement Platform
                </span>
                <h1 class="text-4xl sm:text-5xl font-extrabold text-slate-900 tracking-tight leading-tight mb-6">
                    Connect Top Student Talent with Industry-Leading Employers.
                </h1>
                <p class="text-lg text-slate-600 mb-10">
                    A comprehensive platform featuring intelligent application pipelines, real-time status tracking, recruiter evaluation dashboards, and administrative oversight.
                </p>

                <!-- Role Quick Switcher Demo Cards -->
                <div class="bg-white p-6 sm:p-8 rounded-2xl shadow-xl border border-slate-200 text-left mb-12">
                    <h3 class="text-lg font-bold text-slate-800 mb-2 flex items-center">
                        <i class="fa-solid fa-user-shield text-indigo-600 mr-2"></i> Role Simulator & Quick Login
                    </h3>
                    <p class="text-sm text-slate-500 mb-6">Select a profile to instantly test the platform from different user roles:</p>
                    
                    <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
                        <button onclick="demoLogin('student')" class="p-4 rounded-xl border border-slate-200 hover:border-indigo-600 hover:bg-indigo-50/50 transition flex flex-col items-center text-center group">
                            <div class="w-12 h-12 rounded-full bg-blue-100 text-blue-600 flex items-center justify-center text-lg mb-3 group-hover:scale-110 transition">
                                <i class="fa-solid fa-user-graduate"></i>
                            </div>
                            <span class="font-bold text-slate-900">Student Portal</span>
                            <span class="text-xs text-slate-500 mt-1">Browse, apply, save & track statuses</span>
                        </button>

                        <button onclick="demoLogin('employer')" class="p-4 rounded-xl border border-slate-200 hover:border-indigo-600 hover:bg-indigo-50/50 transition flex flex-col items-center text-center group">
                            <div class="w-12 h-12 rounded-full bg-purple-100 text-purple-600 flex items-center justify-center text-lg mb-3 group-hover:scale-110 transition">
                                <i class="fa-solid fa-building"></i>
                            </div>
                            <span class="font-bold text-slate-900">Employer Portal</span>
                            <span class="text-xs text-slate-500 mt-1">Post roles, manage & evaluate candidates</span>
                        </button>

                        <button onclick="demoLogin('admin')" class="p-4 rounded-xl border border-slate-200 hover:border-indigo-600 hover:bg-indigo-50/50 transition flex flex-col items-center text-center group">
                            <div class="w-12 h-12 rounded-full bg-amber-100 text-amber-600 flex items-center justify-center text-lg mb-3 group-hover:scale-110 transition">
                                <i class="fa-solid fa-shield-halved"></i>
                            </div>
                            <span class="font-bold text-slate-900">Admin Dashboard</span>
                            <span class="text-xs text-slate-500 mt-1">System analytics & global moderation</span>
                        </button>
                    </div>
                </div>

                <div class="flex justify-center space-x-4">
                    <button onclick="switchView('student')" class="px-6 py-3 bg-indigo-600 hover:bg-indigo-700 text-white font-semibold rounded-xl shadow-md transition flex items-center">
                        <i class="fa-solid fa-magnifying-glass mr-2"></i> Browse All Openings
                    </button>
                    <button onclick="openModal('authModal')" class="px-6 py-3 bg-white hover:bg-slate-50 text-slate-700 font-semibold rounded-xl border border-slate-300 shadow-sm transition">
                        Sign In / Register
                    </button>
                </div>
            </div>
        </section>

        <!-- VIEW 2: STUDENT PORTAL -->
        <section id="viewStudent" class="view-section hidden fade-in">
            <div class="flex flex-col md:flex-row justify-between items-start md:items-center mb-8 gap-4">
                <div>
                    <h1 class="text-2xl sm:text-3xl font-extrabold text-slate-900">Student Career Hub</h1>
                    <p class="text-sm text-slate-500">Discover internships, submit applications, and track your interview pipeline.</p>
                </div>
                <div class="flex items-center space-x-2 bg-white p-1 rounded-xl border border-slate-200 shadow-sm">
                    <button onclick="switchStudentTab('browse')" id="tabBtnBrowse" class="px-4 py-2 text-sm font-semibold rounded-lg bg-indigo-600 text-white transition">Explore Jobs</button>
                    <button onclick="switchStudentTab('applications')" id="tabBtnApps" class="px-4 py-2 text-sm font-semibold rounded-lg text-slate-600 hover:text-slate-900 transition">My Applications</button>
                    <button onclick="switchStudentTab('saved')" id="tabBtnSaved" class="px-4 py-2 text-sm font-semibold rounded-lg text-slate-600 hover:text-slate-900 transition">Saved (<span id="savedCountBadge">0</span>)</button>
                </div>
            </div>

            <!-- Tab 1: Browse & Search -->
            <div id="studentTabBrowse" class="space-y-6">
                <div class="bg-white p-4 rounded-2xl shadow-sm border border-slate-200 grid grid-cols-1 sm:grid-cols-4 gap-3">
                    <div class="relative">
                        <i class="fa-solid fa-magnifying-glass absolute left-3.5 top-3.5 text-slate-400"></i>
                        <input type="text" id="filterKeyword" placeholder="Job title, company, skill..." oninput="renderStudentListings()" class="w-full pl-10 pr-4 py-2.5 rounded-xl border border-slate-300 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm">
                    </div>
                    <div>
                        <select id="filterCategory" onchange="renderStudentListings()" class="w-full px-4 py-2.5 rounded-xl border border-slate-300 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm bg-white">
                            <option value="">All Categories</option>
                            <option value="Software Engineering">Software Engineering</option>
                            <option value="Data Science & AI">Data Science & AI</option>
                            <option value="Product Management">Product Management</option>
                            <option value="UI/UX Design">UI/UX Design</option>
                            <option value="Marketing & Growth">Marketing & Growth</option>
                        </select>
                    </div>
                    <div>
                        <select id="filterLocation" onchange="renderStudentListings()" class="w-full px-4 py-2.5 rounded-xl border border-slate-300 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm bg-white">
                            <option value="">All Locations</option>
                            <option value="Remote">Remote</option>
                            <option value="Hybrid">Hybrid</option>
                            <option value="San Francisco, CA">San Francisco, CA</option>
                            <option value="New York, NY">New York, NY</option>
                            <option value="Austin, TX">Austin, TX</option>
                        </select>
                    </div>
                    <div>
                        <select id="filterStipend" onchange="renderStudentListings()" class="w-full px-4 py-2.5 rounded-xl border border-slate-300 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm bg-white">
                            <option value="">Any Compensation</option>
                            <option value="paid">Paid Only</option>
                        </select>
                    </div>
                </div>

                <div id="studentListingsGrid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6"></div>
            </div>

            <!-- Tab 2: Applications Tracker -->
            <div id="studentTabApps" class="hidden space-y-6">
                <div class="bg-white rounded-2xl shadow-sm border border-slate-200 overflow-hidden">
                    <div class="px-6 py-4 border-b border-slate-200 flex justify-between items-center bg-slate-50/50">
                        <h3 class="font-bold text-slate-800">Submitted Applications Pipeline</h3>
                        <span id="appTrackerStats" class="text-xs font-semibold px-2.5 py-1 bg-indigo-50 text-indigo-700 rounded-full">0 Active</span>
                    </div>
                    <div class="overflow-x-auto">
                        <table class="w-full text-left border-collapse">
                            <thead>
                                <tr class="border-b border-slate-200 text-xs font-semibold text-slate-400 uppercase tracking-wider bg-slate-50">
                                    <th class="px-6 py-3">Internship / Company</th>
                                    <th class="px-6 py-3">Applied Date</th>
                                    <th class="px-6 py-3">Status</th>
                                    <th class="px-6 py-3">Next Action</th>
                                    <th class="px-6 py-3 text-right">Actions</th>
                                </tr>
                            </thead>
                            <tbody id="studentApplicationsTableBody" class="divide-y divide-slate-100 text-sm"></tbody>
                        </table>
                    </div>
                </div>
            </div>

            <!-- Tab 3: Saved Jobs -->
            <div id="studentTabSaved" class="hidden space-y-6">
                <div id="savedListingsGrid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6"></div>
            </div>
        </section>

        <!-- VIEW 3: EMPLOYER PORTAL -->
        <section id="viewEmployer" class="view-section hidden fade-in">
            <div class="flex flex-col md:flex-row justify-between items-start md:items-center mb-8 gap-4">
                <div>
                    <h1 class="text-2xl sm:text-3xl font-extrabold text-slate-900">Employer Dashboard</h1>
                    <p class="text-sm text-slate-500">Post listings, manage active recruitment pipeline, and evaluate candidates.</p>
                </div>
                <div class="flex items-center space-x-3">
                    <button onclick="openModal('postJobModal')" class="px-5 py-2.5 bg-indigo-600 hover:bg-indigo-700 text-white font-semibold rounded-xl shadow-sm transition flex items-center text-sm">
                        <i class="fa-solid fa-plus mr-2"></i> Post New Internship
                    </button>
                </div>
            </div>

            <!-- Employer Metrics Bar -->
            <div class="grid grid-cols-1 sm:grid-cols-3 gap-6 mb-8">
                <div class="bg-white p-6 rounded-2xl shadow-sm border border-slate-200 flex items-center justify-between">
                    <div>
                        <p class="text-xs font-semibold uppercase text-slate-400 mb-1">Active Postings</p>
                        <h3 id="empMetricJobs" class="text-3xl font-extrabold text-slate-900">0</h3>
                    </div>
                    <div class="w-12 h-12 rounded-xl bg-indigo-50 text-indigo-600 flex items-center justify-center text-xl"><i class="fa-solid fa-briefcase"></i></div>
                </div>
                <div class="bg-white p-6 rounded-2xl shadow-sm border border-slate-200 flex items-center justify-between">
                    <div>
                        <p class="text-xs font-semibold uppercase text-slate-400 mb-1">Total Applicants</p>
                        <h3 id="empMetricApplicants" class="text-3xl font-extrabold text-slate-900">0</h3>
                    </div>
                    <div class="w-12 h-12 rounded-xl bg-blue-50 text-blue-600 flex items-center justify-center text-xl"><i class="fa-solid fa-users"></i></div>
                </div>
                <div class="bg-white p-6 rounded-2xl shadow-sm border border-slate-200 flex items-center justify-between">
                    <div>
                        <p class="text-xs font-semibold uppercase text-slate-400 mb-1">Shortlisted / Interview</p>
                        <h3 id="empMetricShortlisted" class="text-3xl font-extrabold text-slate-900">0</h3>
                    </div>
                    <div class="w-12 h-12 rounded-xl bg-emerald-50 text-emerald-600 flex items-center justify-center text-xl"><i class="fa-solid fa-user-check"></i></div>
                </div>
            </div>

            <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
                <div class="lg:col-span-1 space-y-4">
                    <h3 class="font-bold text-slate-800 text-lg">Your Postings</h3>
                    <div id="employerJobsList" class="space-y-3"></div>
                </div>
                <div class="lg:col-span-2 space-y-4">
                    <div class="flex justify-between items-center">
                        <h3 id="selectedJobTitleHeader" class="font-bold text-slate-800 text-lg">Select a posting to review applicants</h3>
                    </div>
                    <div class="bg-white rounded-2xl shadow-sm border border-slate-200 overflow-hidden">
                        <div class="overflow-x-auto">
                            <table class="w-full text-left border-collapse">
                                <thead>
                                    <tr class="border-b border-slate-200 text-xs font-semibold text-slate-400 uppercase tracking-wider bg-slate-50">
                                        <th class="px-6 py-3">Candidate</th>
                                        <th class="px-6 py-3">Applied</th>
                                        <th class="px-6 py-3">Status</th>
                                        <th class="px-6 py-3 text-right">Actions</th>
                                    </tr>
                                </thead>
                                <tbody id="employerApplicantsTableBody" class="divide-y divide-slate-100 text-sm">
                                    <tr><td colspan="4" class="px-6 py-8 text-center text-slate-400">Please choose an internship listing on the left.</td></tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- VIEW 4: ADMIN DASHBOARD -->
        <section id="viewAdmin" class="view-section hidden fade-in">
            <div class="flex flex-col md:flex-row justify-between items-start md:items-center mb-8 gap-4">
                <div>
                    <h1 class="text-2xl sm:text-3xl font-extrabold text-slate-900">Admin Control Center</h1>
                    <p class="text-sm text-slate-500">System analytics, user management, and global job posting moderation.</p>
                </div>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
                <div class="bg-white p-6 rounded-2xl shadow-sm border border-slate-200">
                    <p class="text-xs font-semibold uppercase text-slate-400 mb-1">Total Users</p>
                    <h3 id="adminStatUsers" class="text-3xl font-extrabold text-slate-900">0</h3>
                </div>
                <div class="bg-white p-6 rounded-2xl shadow-sm border border-slate-200">
                    <p class="text-xs font-semibold uppercase text-slate-400 mb-1">Total Job Postings</p>
                    <h3 id="adminStatJobs" class="text-3xl font-extrabold text-slate-900">0</h3>
                </div>
                <div class="bg-white p-6 rounded-2xl shadow-sm border border-slate-200">
                    <p class="text-xs font-semibold uppercase text-slate-400 mb-1">Total Applications</p>
                    <h3 id="adminStatApps" class="text-3xl font-extrabold text-slate-900">0</h3>
                </div>
                <div class="bg-white p-6 rounded-2xl shadow-sm border border-slate-200">
                    <p class="text-xs font-semibold uppercase text-slate-400 mb-1">Active Companies</p>
                    <h3 id="adminStatCompanies" class="text-3xl font-extrabold text-slate-900">0</h3>
                </div>
            </div>

            <div class="space-y-8">
                <div class="bg-white rounded-2xl shadow-sm border border-slate-200 overflow-hidden">
                    <div class="px-6 py-4 border-b border-slate-200 flex justify-between items-center bg-slate-50/50">
                        <h3 class="font-bold text-slate-800">User Accounts Management</h3>
                    </div>
                    <div class="overflow-x-auto">
                        <table class="w-full text-left border-collapse">
                            <thead>
                                <tr class="border-b border-slate-200 text-xs font-semibold text-slate-400 uppercase tracking-wider bg-slate-50">
                                    <th class="px-6 py-3">User ID & Name</th>
                                    <th class="px-6 py-3">Email</th>
                                    <th class="px-6 py-3">Role</th>
                                    <th class="px-6 py-3 text-right">Actions</th>
                                </tr>
                            </thead>
                            <tbody id="adminUsersTableBody" class="divide-y divide-slate-100 text-sm"></tbody>
                        </table>
                    </div>
                </div>

                <div class="bg-white rounded-2xl shadow-sm border border-slate-200 overflow-hidden">
                    <div class="px-6 py-4 border-b border-slate-200 flex justify-between items-center bg-slate-50/50">
                        <h3 class="font-bold text-slate-800">Global Internship Moderation</h3>
                    </div>
                    <div class="overflow-x-auto">
                        <table class="w-full text-left border-collapse">
                            <thead>
                                <tr class="border-b border-slate-200 text-xs font-semibold text-slate-400 uppercase tracking-wider bg-slate-50">
                                    <th class="px-6 py-3">Job Title & Company</th>
                                    <th class="px-6 py-3">Category</th>
                                    <th class="px-6 py-3">Location</th>
                                    <th class="px-6 py-3 text-right">Actions</th>
                                </tr>
                            </thead>
                            <tbody id="adminJobsTableBody" class="divide-y divide-slate-100 text-sm"></tbody>
                        </table>
                    </div>
                </div>
            </div>
        </section>

    </main>

    <!-- 1. JOB DETAIL MODAL -->
    <div id="jobDetailModal" class="fixed inset-0 z-50 flex items-center justify-center bg-slate-900/50 backdrop-blur-sm hidden">
        <div class="bg-white rounded-2xl shadow-2xl max-w-2xl w-full mx-4 overflow-hidden max-h-[90vh] flex flex-col fade-in">
            <div class="px-6 py-4 border-b border-slate-200 flex justify-between items-center bg-slate-50">
                <div>
                    <span id="modalJobCategory" class="text-xs font-semibold px-2.5 py-1 bg-indigo-50 text-indigo-700 rounded-full">Category</span>
                    <h2 id="modalJobTitle" class="text-xl font-bold text-slate-900 mt-1">Job Title</h2>
                </div>
                <button onclick="closeModal('jobDetailModal')" class="w-8 h-8 rounded-full bg-slate-200 hover:bg-slate-300 flex items-center justify-center text-slate-600 transition"><i class="fa-solid fa-xmark"></i></button>
            </div>
            <div class="p-6 overflow-y-auto space-y-6 flex-grow">
                <div class="flex flex-wrap gap-4 text-sm text-slate-600">
                    <div class="flex items-center"><i class="fa-solid fa-building text-slate-400 mr-2"></i><span id="modalJobCompany">Company</span></div>
                    <div class="flex items-center"><i class="fa-solid fa-location-dot text-slate-400 mr-2"></i><span id="modalJobLocation">Location</span></div>
                    <div class="flex items-center"><i class="fa-solid fa-wallet text-slate-400 mr-2"></i><span id="modalJobStipend">Stipend</span></div>
                    <div class="flex items-center"><i class="fa-regular fa-calendar text-slate-400 mr-2"></i>Deadline: <span id="modalJobDeadline" class="ml-1 font-medium">Date</span></div>
                </div>
                <div>
                    <h4 class="font-bold text-slate-800 mb-2">Description</h4>
                    <p id="modalJobDescription" class="text-sm text-slate-600 whitespace-pre-line leading-relaxed"></p>
                </div>
                <div>
                    <h4 class="font-bold text-slate-800 mb-2">Requirements & Skills</h4>
                    <p id="modalJobRequirements" class="text-sm text-slate-600 whitespace-pre-line leading-relaxed"></p>
                </div>
            </div>
            <div class="px-6 py-4 border-t border-slate-200 bg-slate-50 flex justify-end space-x-3">
                <button onclick="closeModal('jobDetailModal')" class="px-4 py-2 border border-slate-300 text-slate-700 font-semibold rounded-xl text-sm hover:bg-slate-100 transition">Close</button>
                <button id="modalApplyBtn" onclick="" class="px-5 py-2 bg-indigo-600 hover:bg-indigo-700 text-white font-semibold rounded-xl text-sm shadow-sm transition">Apply Now</button>
            </div>
        </div>
    </div>

    <!-- 2. APPLY FORM MODAL -->
    <div id="applyModal" class="fixed inset-0 z-50 flex items-center justify-center bg-slate-900/50 backdrop-blur-sm hidden">
        <div class="bg-white rounded-2xl shadow-2xl max-w-lg w-full mx-4 overflow-hidden fade-in">
            <div class="px-6 py-4 border-b border-slate-200 flex justify-between items-center bg-slate-50">
                <h3 class="font-bold text-slate-900">Submit Application</h3>
                <button onclick="closeModal('applyModal')" class="w-8 h-8 rounded-full bg-slate-200 hover:bg-slate-300 flex items-center justify-center text-slate-600 transition"><i class="fa-solid fa-xmark"></i></button>
            </div>
            <form id="applyForm" onsubmit="submitApplicationHandler(event)" class="p-6 space-y-4">
                <input type="hidden" id="applyJobId">
                <div>
                    <label class="block text-xs font-semibold text-slate-600 uppercase mb-1">Full Name</label>
                    <input type="text" id="applicantName" required class="w-full px-4 py-2.5 rounded-xl border border-slate-300 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm">
                </div>
                <div>
                    <label class="block text-xs font-semibold text-slate-600 uppercase mb-1">Email Address</label>
                    <input type="email" id="applicantEmail" required class="w-full px-4 py-2.5 rounded-xl border border-slate-300 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm">
                </div>
                <div>
                    <label class="block text-xs font-semibold text-slate-600 uppercase mb-1">Cover Letter & Motivation</label>
                    <textarea id="applicantCoverLetter" rows="4" placeholder="Briefly explain why you are a great fit..." required class="w-full px-4 py-2.5 rounded-xl border border-slate-300 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm"></textarea>
                </div>
                <div>
                    <label class="block text-xs font-semibold text-slate-600 uppercase mb-1">Simulated Resume Upload</label>
                    <input type="file" id="applicantResumeFile" class="w-full text-sm text-slate-500 file:mr-4 file:py-2 file:px-4 file:rounded-xl file:border-0 file:text-sm file:font-semibold file:bg-indigo-50 file:text-indigo-700 hover:file:bg-indigo-100 transition">
                </div>
                <div class="pt-4 flex justify-end space-x-3">
                    <button type="button" onclick="closeModal('applyModal')" class="px-4 py-2 border border-slate-300 text-slate-700 font-semibold rounded-xl text-sm hover:bg-slate-100 transition">Cancel</button>
                    <button type="submit" class="px-5 py-2 bg-indigo-600 hover:bg-indigo-700 text-white font-semibold rounded-xl text-sm shadow-sm transition">Submit Application</button>
                </div>
            </form>
        </div>
    </div>

    <!-- 3. POST INTERNSHIP MODAL -->
    <div id="postJobModal" class="fixed inset-0 z-50 flex items-center justify-center bg-slate-900/50 backdrop-blur-sm hidden">
        <div class="bg-white rounded-2xl shadow-2xl max-w-2xl w-full mx-4 overflow-hidden max-h-[90vh] flex flex-col fade-in">
            <div class="px-6 py-4 border-b border-slate-200 flex justify-between items-center bg-slate-50">
                <h3 class="font-bold text-slate-900">Post New Internship Opportunity</h3>
                <button onclick="closeModal('postJobModal')" class="w-8 h-8 rounded-full bg-slate-200 hover:bg-slate-300 flex items-center justify-center text-slate-600 transition"><i class="fa-solid fa-xmark"></i></button>
            </div>
            <form id="postJobForm" onsubmit="postJobHandler(event)" class="p-6 overflow-y-auto space-y-4 flex-grow">
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    <div>
                        <label class="block text-xs font-semibold text-slate-600 uppercase mb-1">Internship Title</label>
                        <input type="text" id="newJobTitle" placeholder="e.g. Frontend Intern" required class="w-full px-4 py-2.5 rounded-xl border border-slate-300 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm">
                    </div>
                    <div>
                        <label class="block text-xs font-semibold text-slate-600 uppercase mb-1">Company Name</label>
                        <input type="text" id="newJobCompany" placeholder="e.g. Acme Corp" required class="w-full px-4 py-2.5 rounded-xl border border-slate-300 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm">
                    </div>
                </div>
                <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
                    <div>
                        <label class="block text-xs font-semibold text-slate-600 uppercase mb-1">Category</label>
                        <select id="newJobCategory" class="w-full px-4 py-2.5 rounded-xl border border-slate-300 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm bg-white">
                            <option value="Software Engineering">Software Engineering</option>
                            <option value="Data Science & AI">Data Science & AI</option>
                            <option value="Product Management">Product Management</option>
                            <option value="UI/UX Design">UI/UX Design</option>
                            <option value="Marketing & Growth">Marketing & Growth</option>
                        </select>
                    </div>
                    <div>
                        <label class="block text-xs font-semibold text-slate-600 uppercase mb-1">Location</label>
                        <select id="newJobLocation" class="w-full px-4 py-2.5 rounded-xl border border-slate-300 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm bg-white">
                            <option value="Remote">Remote</option>
                            <option value="Hybrid">Hybrid</option>
                            <option value="San Francisco, CA">San Francisco, CA</option>
                            <option value="New York, NY">New York, NY</option>
                            <option value="Austin, TX">Austin, TX</option>
                        </select>
                    </div>
                    <div>
                        <label class="block text-xs font-semibold text-slate-600 uppercase mb-1">Stipend / Comp</label>
                        <input type="text" id="newJobStipend" placeholder="e.g. $3,500 / mo" required class="w-full px-4 py-2.5 rounded-xl border border-slate-300 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm">
                    </div>
                </div>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    <div>
                        <label class="block text-xs font-semibold text-slate-600 uppercase mb-1">Application Deadline</label>
                        <input type="date" id="newJobDeadline" required class="w-full px-4 py-2.5 rounded-xl border border-slate-300 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm">
                    </div>
                </div>
                <div>
                    <label class="block text-xs font-semibold text-slate-600 uppercase mb-1">Full Description</label>
                    <textarea id="newJobDescription" rows="3" required class="w-full px-4 py-2.5 rounded-xl border border-slate-300 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm"></textarea>
                </div>
                <div>
                    <label class="block text-xs font-semibold text-slate-600 uppercase mb-1">Requirements & Skills</label>
                    <textarea id="newJobRequirements" rows="3" required class="w-full px-4 py-2.5 rounded-xl border border-slate-300 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm"></textarea>
                </div>
                <div class="pt-4 flex justify-end space-x-3">
                    <button type="button" onclick="closeModal('postJobModal')" class="px-4 py-2 border border-slate-300 text-slate-700 font-semibold rounded-xl text-sm hover:bg-slate-100 transition">Cancel</button>
                    <button type="submit" class="px-5 py-2 bg-indigo-600 hover:bg-indigo-700 text-white font-semibold rounded-xl text-sm shadow-sm transition">Publish Posting</button>
                </div>
            </form>
        </div>
    </div>

    <!-- 4. AUTH MODAL (SIGN IN / REGISTER) -->
    <div id="authModal" class="fixed inset-0 z-50 flex items-center justify-center bg-slate-900/50 backdrop-blur-sm hidden">
        <div class="bg-white rounded-2xl shadow-2xl max-w-md w-full mx-4 overflow-hidden fade-in">
            <div class="px-6 py-4 border-b border-slate-200 flex justify-between items-center bg-slate-50">
                <h3 id="authModalTitle" class="font-bold text-slate-900">Sign In to InternPro</h3>
                <button onclick="closeModal('authModal')" class="w-8 h-8 rounded-full bg-slate-200 hover:bg-slate-300 flex items-center justify-center text-slate-600 transition"><i class="fa-solid fa-xmark"></i></button>
            </div>
            <form id="authForm" onsubmit="authFormHandler(event)" class="p-6 space-y-4">
                <div id="authNameFieldContainer" class="hidden">
                    <label class="block text-xs font-semibold text-slate-600 uppercase mb-1">Full Name</label>
                    <input type="text" id="authNameInput" class="w-full px-4 py-2.5 rounded-xl border border-slate-300 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm">
                </div>
                <div>
                    <label class="block text-xs font-semibold text-slate-600 uppercase mb-1">Email Address</label>
                    <input type="email" id="authEmailInput" required class="w-full px-4 py-2.5 rounded-xl border border-slate-300 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm">
                </div>
                <div>
                    <label class="block text-xs font-semibold text-slate-600 uppercase mb-1">Password</label>
                    <input type="password" id="authPasswordInput" required class="w-full px-4 py-2.5 rounded-xl border border-slate-300 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm">
                </div>
                <div id="authRoleFieldContainer" class="hidden">
                    <label class="block text-xs font-semibold text-slate-600 uppercase mb-1">Select Role</label>
                    <select id="authRoleSelect" class="w-full px-4 py-2.5 rounded-xl border border-slate-300 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm bg-white">
                        <option value="student">Student</option>
                        <option value="employer">Employer</option>
                    </select>
                </div>
                <div class="pt-2">
                    <button type="submit" id="authSubmitBtn" class="w-full py-3 bg-indigo-600 hover:bg-indigo-700 text-white font-semibold rounded-xl text-sm shadow-sm transition">Sign In</button>
                </div>
                <div class="text-center pt-2">
                    <button type="button" onclick="toggleAuthMode()" id="authSwitchModeBtn" class="text-xs text-indigo-600 hover:underline font-medium">Don't have an account? Register</button>
                </div>
            </form>
        </div>
    </div>

    <!-- MAIN CLIENT APP JAVASCRIPT LOGIC -->
    <script>
        // State Management
        let currentView = 'home';
        let studentActiveTab = 'browse';
        let currentUser = null; // { name, email, role }
        let selectedEmployerJobId = null;

        let listings = [
            { id: 1, title: 'Frontend Software Intern', company: 'Acme Corp', category: 'Software Engineering', location: 'Remote', stipend: '$3,500 / mo', deadline: '2026-11-30', description: 'Build high-performance accessible web interfaces using modern JS frameworks and Tailwind CSS.', requirements: 'Proficiency in JavaScript/TypeScript, HTML/CSS, and React fundamentals.', status: 'Active' },
            { id: 2, title: 'Data Science & AI Intern', company: 'NeuralMetrics', category: 'Data Science & AI', location: 'San Francisco, CA', stipend: '$4,200 / mo', deadline: '2026-12-15', description: 'Assist our core ML engineering team in training and evaluating custom language models.', requirements: 'Strong Python skills, experience with Pandas, Scikit-Learn, or PyTorch.', status: 'Active' },
            { id: 3, title: 'Product Management Intern', company: 'Veloce Inc.', category: 'Product Management', location: 'New York, NY', stipend: '$3,000 / mo', deadline: '2026-11-20', description: 'Gather product requirements, draft user stories, and coordinate cross-functional sprints.', requirements: 'Excellent communication skills, technical aptitude, and user-first mindset.', status: 'Active' }
        ];

        let applications = [
            { id: 101, job_id: 1, job_title: 'Frontend Software Intern', company: 'Acme Corp', applicant_name: 'Alex Johnson', email: 'alex@student.com', cover_letter: 'I have built several React apps and love clean UI design.', applied_date: '2026-09-10', status: 'Interview', next_action: 'Technical Screen on Oct 5' }
        ];

        let savedJobIds = [2];

        let users = [
            { id: 1, name: 'Alex Johnson', email: 'alex@student.com', role: 'student' },
            { id: 2, name: 'Sarah Recruiter', email: 'sarah@acme.com', role: 'employer' },
            { id: 3, name: 'Admin Master', email: 'admin@internpro.com', role: 'admin' }
        ];

        let isRegisterMode = false;

        // Initialization
        window.addEventListener('DOMContentLoaded', () => {
            switchView('home');
        });

        function showToast(message, type = 'success') {
            const container = document.getElementById('toastContainer');
            const toast = document.createElement('div');
            const bgColor = type === 'success' ? 'bg-slate-900 text-white' : 'bg-red-600 text-white';
            toast.className = `${bgColor} px-4 py-3 rounded-xl shadow-lg text-sm font-medium flex items-center justify-between space-x-4 pointer-events-auto fade-in`;
            toast.innerHTML = `<span>${message}</span><button onclick="this.parentElement.remove()" class="text-white/80 hover:text-white"><i class="fa-solid fa-xmark"></i></button>`;
            container.appendChild(toast);
            setTimeout(() => toast.remove(), 4000);
        }

        function switchView(viewName) {
            currentView = viewName;
            document.querySelectorAll('.view-section').forEach(sec => sec.classList.add('hidden'));
            
            if (viewName === 'home') document.getElementById('viewHome').classList.remove('hidden');
            if (viewName === 'student') {
                document.getElementById('viewStudent').classList.remove('hidden');
                renderStudentListings();
                renderStudentApplications();
                renderSavedListings();
            }
            if (viewName === 'employer') {
                document.getElementById('viewEmployer').classList.remove('hidden');
                renderEmployerDashboard();
            }
            if (viewName === 'admin') {
                document.getElementById('viewAdmin').classList.remove('hidden');
                renderAdminDashboard();
            }
            renderNavbar();
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }

        function renderNavbar() {
            const navLinks = document.getElementById('navLinks');
            const authContainer = document.getElementById('authNavbarContainer');

            let htmlLinks = '';
            if (currentUser) {
                if (currentUser.role === 'student') htmlLinks += `<button onclick="switchView('student')" class="hover:text-indigo-600 transition">Student Hub</button>`;
                if (currentUser.role === 'employer') htmlLinks += `<button onclick="switchView('employer')" class="hover:text-indigo-600 transition">Employer Portal</button>`;
                if (currentUser.role === 'admin') htmlLinks += `<button onclick="switchView('admin')" class="hover:text-indigo-600 transition">Admin Center</button>`;
            } else {
                htmlLinks += `<button onclick="switchView('student')" class="hover:text-indigo-600 transition">Explore Jobs</button>`;
            }
            navLinks.innerHTML = htmlLinks;

            if (currentUser) {
                authContainer.innerHTML = `
                    <div class="flex items-center space-x-3">
                        <span class="text-xs font-semibold px-3 py-1.5 bg-slate-100 rounded-xl text-slate-700">👤 ${currentUser.name} (${currentUser.role})</span>
                        <button onclick="logout()" class="px-3 py-1.5 bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-semibold rounded-xl transition">Sign Out</button>
                    </div>
                `;
            } else {
                authContainer.innerHTML = `
                    <button onclick="openModal('authModal')" class="px-4 py-2 bg-indigo-600 hover:bg-indigo-700 text-white text-sm font-semibold rounded-xl shadow-sm transition">Sign In</button>
                `;
            }
        }

        function demoLogin(roleType) {
            if (roleType === 'student') currentUser = users[0];
            if (roleType === 'employer') currentUser = users[1];
            if (roleType === 'admin') currentUser = users[2];
            showToast(`Logged in successfully as ${currentUser.name} (${roleType})`);
            switchView(roleType);
        }

        function logout() {
            currentUser = null;
            showToast('Signed out successfully');
            switchView('home');
        }

        // Student Tab Switching & Listings Rendering
        function switchStudentTab(tabName) {
            studentActiveTab = tabName;
            document.getElementById('studentTabBrowse').classList.add('hidden');
            document.getElementById('studentTabApps').classList.add('hidden');
            document.getElementById('studentTabSaved').classList.add('hidden');

            document.getElementById('tabBtnBrowse').className = "px-4 py-2 text-sm font-semibold rounded-lg text-slate-600 hover:text-slate-900 transition";
            document.getElementById('tabBtnApps').className = "px-4 py-2 text-sm font-semibold rounded-lg text-slate-600 hover:text-slate-900 transition";
            document.getElementById('tabBtnSaved').className = "px-4 py-2 text-sm font-semibold rounded-lg text-slate-600 hover:text-slate-900 transition";

            if (tabName === 'browse') {
                document.getElementById('studentTabBrowse').classList.remove('hidden');
                document.getElementById('tabBtnBrowse').className = "px-4 py-2 text-sm font-semibold rounded-lg bg-indigo-600 text-white transition";
            } else if (tabName === 'applications') {
                document.getElementById('studentTabApps').classList.remove('hidden');
                document.getElementById('tabBtnApps').className = "px-4 py-2 text-sm font-semibold rounded-lg bg-indigo-600 text-white transition";
                renderStudentApplications();
            } else if (tabName === 'saved') {
                document.getElementById('studentTabSaved').classList.remove('hidden');
                document.getElementById('tabBtnSaved').className = "px-4 py-2 text-sm font-semibold rounded-lg bg-indigo-600 text-white transition";
                renderSavedListings();
            }
            document.getElementById('savedCountBadge').innerText = savedJobIds.length;
        }

        function renderStudentListings() {
            const keyword = document.getElementById('filterKeyword').value.toLowerCase();
            const category = document.getElementById('filterCategory').value;
            const location = document.getElementById('filterLocation').value;
            const stipendOnly = document.getElementById('filterStipend').value;

            const grid = document.getElementById('studentListingsGrid');
            let filtered = listings.filter(j => j.status === 'Active');

            if (keyword) {
                filtered = filtered.filter(j => j.title.toLowerCase().includes(keyword) || j.company.toLowerCase().includes(keyword) || j.requirements.toLowerCase().includes(keyword));
            }
            if (category) filtered = filtered.filter(j => j.category === category);
            if (location) filtered = filtered.filter(j => j.location === location);

            if (filtered.length === 0) {
                grid.innerHTML = `<div class="col-span-full py-12 text-center text-slate-400">No active internship opportunities match your filter criteria.</div>`;
                return;
            }

            grid.innerHTML = filtered.map(job => {
                const isSaved = savedJobIds.includes(job.id);
                return `
                    <div class="bg-white p-6 rounded-2xl shadow-sm border border-slate-200 flex flex-col justify-between hover:border-indigo-300 transition">
                        <div>
                            <div class="flex justify-between items-start mb-3">
                                <span class="text-xs font-semibold px-2.5 py-1 bg-indigo-50 text-indigo-700 rounded-full">${job.category}</span>
                                <button onclick="toggleSaveJob(${job.id})" class="text-lg ${isSaved ? 'text-red-500' : 'text-slate-300 hover:text-slate-500'} transition"><i class="fa-${isSaved ? 'solid' : 'regular'} fa-heart"></i></button>
                            </div>
                            <h3 class="font-bold text-slate-900 text-lg mb-1">${job.title}</h3>
                            <p class="text-sm font-medium text-slate-600 mb-4"><i class="fa-solid fa-building text-slate-400 mr-1.5"></i>${job.company}</p>
                            <div class="space-y-1.5 text-xs text-slate-500 mb-4">
                                <div><i class="fa-solid fa-location-dot text-slate-400 mr-1.5 w-4"></i>${job.location}</div>
                                <div><i class="fa-solid fa-wallet text-slate-400 mr-1.5 w-4"></i>${job.stipend}</div>
                                <div><i class="fa-regular fa-calendar text-slate-400 mr-1.5 w-4"></i>Deadline: ${job.deadline}</div>
                            </div>
                            <p class="text-sm text-slate-600 line-clamp-2 mb-6">${job.description}</p>
                        </div>
                        <div class="flex items-center space-x-2 pt-4 border-t border-slate-100">
                            <button onclick="openJobDetail(${job.id})" class="flex-1 px-4 py-2 bg-slate-100 hover:bg-slate-200 text-slate-700 font-semibold rounded-xl text-xs transition">View Details</button>
                            <button onclick="openApplyModal(${job.id})" class="flex-1 px-4 py-2 bg-indigo-600 hover:bg-indigo-700 text-white font-semibold rounded-xl text-xs shadow-sm transition">Apply Now</button>
                        </div>
                    </div>
                `;
            }).join('');
            document.getElementById('savedCountBadge').innerText = savedJobIds.length;
        }

        function toggleSaveJob(jobId) {
            if (savedJobIds.includes(jobId)) {
                savedJobIds = savedJobIds.filter(id => id !== jobId);
                showToast('Removed from saved bookmarks', 'info');
            } else {
                savedJobIds.push(jobId);
                showToast('Added to saved bookmarks');
            }
            renderStudentListings();
            if (studentActiveTab === 'saved') renderSavedListings();
        }

        function renderStudentApplications() {
            const tbody = document.getElementById('studentApplicationsTableBody');
            document.getElementById('appTrackerStats').innerText = `${applications.length} Active`;

            if (applications.length === 0) {
                tbody.innerHTML = `<tr><td colspan="5" class="px-6 py-8 text-center text-slate-400">You have not submitted any applications yet.</td></tr>`;
                return;
            }

            tbody.innerHTML = applications.map(app => `
                <tr class="hover:bg-slate-50/50 transition">
                    <td class="px-6 py-4">
                        <div class="font-bold text-slate-900">${app.job_title}</div>
                        <div class="text-xs text-slate-500">${app.company}</div>
                    </td>
                    <td class="px-6 py-4 text-slate-600">${app.applied_date}</td>
                    <td class="px-6 py-4">
                        <span class="px-2.5 py-1 text-xs font-semibold rounded-full bg-indigo-50 text-indigo-700">${app.status}</span>
                    </td>
                    <td class="px-6 py-4 text-slate-600 font-medium">${app.next_action}</td>
                    <td class="px-6 py-4 text-right">
                        <button onclick="showToast('Withdrawal feature simulated')" class="text-red-500 hover:text-red-700 text-xs font-semibold">Withdraw</button>
                    </td>
                </tr>
            `).join('');
        }

        function renderSavedListings() {
            const grid = document.getElementById('savedListingsGrid');
            const savedJobs = listings.filter(j => savedJobIds.includes(j.id));

            if (savedJobs.length === 0) {
                grid.innerHTML = `<div class="col-span-full py-12 text-center text-slate-400">You have not saved any internship bookmarks yet.</div>`;
                return;
            }

            grid.innerHTML = savedJobs.map(job => `
                <div class="bg-white p-6 rounded-2xl shadow-sm border border-slate-200 flex flex-col justify-between">
                    <div>
                        <span class="text-xs font-semibold px-2.5 py-1 bg-indigo-50 text-indigo-700 rounded-full">${job.category}</span>
                        <h3 class="font-bold text-slate-900 text-lg mt-2 mb-1">${job.title}</h3>
                        <p class="text-sm font-medium text-slate-600 mb-4">${job.company} • ${job.location}</p>
                        <p class="text-sm text-slate-600 line-clamp-2 mb-6">${job.description}</p>
                    </div>
                    <div class="flex space-x-2 pt-4 border-t border-slate-100">
                        <button onclick="openJobDetail(${job.id})" class="flex-1 px-4 py-2 bg-slate-100 hover:bg-slate-200 text-slate-700 font-semibold rounded-xl text-xs">View Details</button>
                        <button onclick="openApplyModal(${job.id})" class="flex-1 px-4 py-2 bg-indigo-600 text-white font-semibold rounded-xl text-xs">Apply Now</button>
                    </div>
                </div>
            `).join('');
        }

        // Employer Portal Logic
        function renderEmployerDashboard() {
            document.getElementById('empMetricJobs').innerText = listings.length;
            document.getElementById('empMetricApplicants').innerText = applications.length;
            document.getElementById('empMetricShortlisted').innerText = applications.filter(a => a.status === 'Shortlisted' || a.status === 'Interview').length;

            const jobsList = document.getElementById('employerJobsList');
            jobsList.innerHTML = listings.map(job => `
                <div onclick="selectEmployerJob(${job.id})" class="p-4 rounded-xl border ${selectedEmployerJobId === job.id ? 'border-indigo-600 bg-indigo-50/50' : 'border-slate-200 bg-white hover:border-slate-300'} cursor-pointer transition">
                    <div class="font-bold text-slate-900 text-sm">${job.title}</div>
                    <div class="text-xs text-slate-500 mt-0.5">${job.company} • ${job.location}</div>
                </div>
            `).join('');

            if (!selectedEmployerJobId && listings.length > 0) {
                selectEmployerJob(listings[0].id);
            }
        }

        function selectEmployerJob(jobId) {
            selectedEmployerJobId = jobId;
            const job = listings.find(j => j.id === jobId);
            document.getElementById('selectedJobTitleHeader').innerText = `Applicants for: ${job.title}`;

            const tbody = document.getElementById('employerApplicantsTableBody');
            const jobApps = applications.filter(a => a.job_id === jobId);

            if (jobApps.length === 0) {
                tbody.innerHTML = `<tr><td colspan="4" class="px-6 py-8 text-center text-slate-400">No candidates have applied for this posting yet.</td></tr>`;
                renderEmployerDashboard();
                return;
            }

            tbody.innerHTML = jobApps.map(app => `
                <tr class="hover:bg-slate-50/50 transition">
                    <td class="px-6 py-4">
                        <div class="font-bold text-slate-900">${app.applicant_name}</div>
                        <div class="text-xs text-slate-500">${app.email}</div>
                    </td>
                    <td class="px-6 py-4 text-slate-600">${app.applied_date}</td>
                    <td class="px-6 py-4"><span class="px-2.5 py-1 text-xs font-semibold rounded-full bg-indigo-50 text-indigo-700">${app.status}</span></td>
                    <td class="px-6 py-4 text-right space-x-2">
                        <button onclick="updateAppStatus(${app.id}, 'Shortlisted')" class="px-3 py-1 bg-emerald-50 text-emerald-700 hover:bg-emerald-100 rounded-lg text-xs font-semibold">Shortlist</button>
                        <button onclick="updateAppStatus(${app.id}, 'Rejected')" class="px-3 py-1 bg-red-50 text-red-700 hover:bg-red-100 rounded-lg text-xs font-semibold">Reject</button>
                    </td>
                </tr>
            `).join('');
            renderEmployerDashboard();
        }

        function updateAppStatus(appId, newStatus) {
            const app = applications.find(a => a.id === appId);
            if (app) {
                app.status = newStatus;
                app.next_action = newStatus === 'Shortlisted' ? 'Interview Scheduled' : 'Archived';
                showToast(`Application status updated to ${newStatus}`);
                selectEmployerJob(selectedEmployerJobId);
            }
        }

        // Admin Dashboard Logic
        function renderAdminDashboard() {
            document.getElementById('adminStatUsers').innerText = users.length;
            document.getElementById('adminStatJobs').innerText = listings.length;
            document.getElementById('adminStatApps').innerText = applications.length;
            document.getElementById('adminStatCompanies').innerText = new Set(listings.map(j => j.company)).size;

            const usersTbody = document.getElementById('adminUsersTableBody');
            usersTbody.innerHTML = users.map(u => `
                <tr class="hover:bg-slate-50/50">
                    <td class="px-6 py-4 font-bold text-slate-900">#${u.id} - ${u.name}</td>
                    <td class="px-6 py-4 text-slate-600">${u.email}</td>
                    <td class="px-6 py-4"><span class="px-2.5 py-1 text-xs font-semibold rounded-full bg-indigo-50 text-indigo-700">${u.role}</span></td>
                    <td class="px-6 py-4 text-right"><button onclick="deleteUser(${u.id})" class="text-red-500 hover:text-red-700 font-semibold text-xs">Delete</button></td>
                </tr>
            `).join('');

            const jobsTbody = document.getElementById('adminJobsTableBody');
            jobsTbody.innerHTML = listings.map(j => `
                <tr class="hover:bg-slate-50/50">
                    <td class="px-6 py-4"><div class="font-bold text-slate-900">${j.title}</div><div class="text-xs text-slate-500">${j.company}</div></td>
                    <td class="px-6 py-4 text-slate-600">${j.category}</td>
                    <td class="px-6 py-4 text-slate-600">${j.location}</td>
                    <td class="px-6 py-4 text-right"><button onclick="deleteJob(${j.id})" class="text-red-500 hover:text-red-700 font-semibold text-xs">Remove</button></td>
                </tr>
            `).join('');
        }

        function deleteUser(id) {
            users = users.filter(u => u.id !== id);
            showToast('User account deleted');
            renderAdminDashboard();
        }

        function deleteJob(id) {
            listings = listings.filter(j => j.id !== id);
            showToast('Job posting removed');
            renderAdminDashboard();
        }

        // Modals & Handlers
        function openModal(modalId) {
            document.getElementById(modalId).classList.remove('hidden');
        }

        function closeModal(modalId) {
            document.getElementById(modalId).classList.add('hidden');
        }

        function openJobDetail(jobId) {
            const job = listings.find(j => j.id === jobId);
            document.getElementById('modalJobCategory').innerText = job.category;
            document.getElementById('modalJobTitle').innerText = job.title;
            document.getElementById('modalJobCompany').innerText = job.company;
            document.getElementById('modalJobLocation').innerText = job.location;
            document.getElementById('modalJobStipend').innerText = job.stipend;
            document.getElementById('modalJobDeadline').innerText = job.deadline;
            document.getElementById('modalJobDescription').innerText = job.description;
            document.getElementById('modalJobRequirements').innerText = job.requirements;
            document.getElementById('modalApplyBtn').setAttribute('onclick', `closeModal('jobDetailModal'); openApplyModal(${job.id})`);
            openModal('jobDetailModal');
        }

        function openApplyModal(jobId) {
            document.getElementById('applyJobId').value = jobId;
            if (currentUser) {
                document.getElementById('applicantName').value = currentUser.name;
                document.getElementById('applicantEmail').value = currentUser.email;
            }
            openModal('applyModal');
        }

        function submitApplicationHandler(event) {
            event.preventDefault();
            const jobId = parseInt(document.getElementById('applyJobId').value);
            const job = listings.find(j => j.id === jobId);
            const name = document.getElementById('applicantName').value;
            const email = document.getElementById('applicantEmail').value;
            const cover = document.getElementById('applicantCoverLetter').value;

            applications.push({
                id: Date.now(),
                job_id: jobId,
                job_title: job.title,
                company: job.company,
                applicant_name: name,
                email: email,
                cover_letter: cover,
                applied_date: new Date().toISOString().split('T')[0],
                status: 'Submitted',
                next_action: 'Under Recruiter Review'
            });

            closeModal('applyModal');
            showToast('Application submitted successfully!');
            document.getElementById('applyForm').reset();
            switchStudentTab('applications');
        }

        function postJobHandler(event) {
            event.preventDefault();
            const newJob = {
                id: Date.now(),
                title: document.getElementById('newJobTitle').value,
                company: document.getElementById('newJobCompany').value,
                category: document.getElementById('newJobCategory').value,
                location: document.getElementById('newJobLocation').value,
                stipend: document.getElementById('newJobStipend').value,
                deadline: document.getElementById('newJobDeadline').value,
                description: document.getElementById('newJobDescription').value,
                requirements: document.getElementById('newJobRequirements').value,
                status: 'Active'
            };
            listings.push(newJob);
            closeModal('postJobModal');
            showToast('New internship posted successfully!');
            document.getElementById('postJobForm').reset();
            renderEmployerDashboard();
        }

        function toggleAuthMode() {
            isRegisterMode = !isRegisterMode;
            document.getElementById('authModalTitle').innerText = isRegisterMode ? 'Register New Account' : 'Sign In to InternPro';
            document.getElementById('authSubmitBtn').innerText = isRegisterMode ? 'Create Account' : 'Sign In';
            document.getElementById('authSwitchModeBtn').innerText = isRegisterMode ? 'Already have an account? Sign In' : "Don't have an account? Register";
            document.getElementById('authNameFieldContainer').classList.toggle('hidden', !isRegisterMode);
            document.getElementById('authRoleFieldContainer').classList.toggle('hidden', !isRegisterMode);
        }

        function authFormHandler(event) {
            event.preventDefault();
            const email = document.getElementById('authEmailInput').value;
            const nameInput = document.getElementById('authNameInput').value;
            const roleInput = document.getElementById('authRoleSelect').value;

            if (isRegisterMode) {
                const newUser = { id: users.length + 1, name: nameInput || 'New User', email: email, role: roleInput };
                users.push(newUser);
                currentUser = newUser;
                showToast('Account created and logged in!');
            } else {
                const found = users.find(u => u.email === email);
                if (found) {
                    currentUser = found;
                    showToast(`Welcome back, ${found.name}!`);
                } else {
                    currentUser = { id: users.length + 1, name: 'Guest User', email: email, role: 'student' };
                    users.push(currentUser);
                    showToast('Signed in successfully');
                }
            }
            closeModal('authModal');
            switchView(currentUser.role);
        }
    </script>
</body>
</html>
"""

# Render the complete original HTML/JS app inside Streamlit with a responsive height
components.html(html_code, height=950, scrolling=True)
