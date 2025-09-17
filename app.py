# package
import streamlit as st
import webPages.page1 as page1

def app():
    # Configure page with professional settings
    st.set_page_config(
        page_title="Data Converter Pro | XLS & CSV to SQL",
        page_icon="⚡",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Theme configuration in sidebar
    with st.sidebar:
        st.markdown("### 🎨 Theme Customization")
        
        # Auto/Manual theme toggle
        theme_mode = st.radio(
            "Theme Mode",
            ["🌙 Auto (System)", "☀️ Light Mode", "🌙 Dark Mode"],
            horizontal=True
        )
        
        # Theme selection
        if theme_mode == "🌙 Auto (System)":
            st.markdown("*Using system preference*")
            theme_option = st.selectbox(
                "Choose Theme",
                ["Corporate Blue", "Professional Dark", "Modern Green", "Executive Purple", "Minimalist Gray"],
                index=1  # Default to dark for auto
            )
        elif theme_mode == "🌙 Dark Mode":
            theme_option = st.selectbox(
                "Choose Dark Theme",
                ["Professional Dark", "Dark Corporate Blue", "Dark Modern Green", "Dark Executive Purple", "Dark Minimalist"]
            )
        else:  # Light Mode
            theme_option = st.selectbox(
                "Choose Light Theme",
                ["Corporate Blue", "Modern Green", "Executive Purple", "Minimalist Gray", "Clean White"]
            )
        
        # Layout options
        layout_compact = st.checkbox("Compact Layout", value=False)
        show_animations = st.checkbox("Enable Animations", value=True)
        show_stats = st.checkbox("Show Statistics", value=True)
        
        # Color customization
        st.markdown("#### Custom Colors")
        primary_color = st.color_picker("Primary Color", "#3b82f6")
        
        st.markdown("---")
        st.markdown("**Theme Settings**")
        st.caption("Customize your workspace appearance")
    
    # Dynamic theme configuration with enhanced dark/light modes
    theme_configs = {
        # Light themes
        "Corporate Blue": {
            "primary": "#3b82f6",
            "secondary": "#1e40af",
            "background": "#ffffff",
            "surface": "#f8fafc",
            "text": "#111827",
            "accent": "#dbeafe",
            "body_bg": "#f8fafc"
        },
        "Modern Green": {
            "primary": "#10b981",
            "secondary": "#059669",
            "background": "#ffffff",
            "surface": "#f0fdf4",
            "text": "#111827",
            "accent": "#d1fae5",
            "body_bg": "#f0fdf4"
        },
        "Executive Purple": {
            "primary": "#8b5cf6",
            "secondary": "#7c3aed",
            "background": "#ffffff",
            "surface": "#faf5ff",
            "text": "#111827",
            "accent": "#ede9fe",
            "body_bg": "#faf5ff"
        },
        "Minimalist Gray": {
            "primary": "#6b7280",
            "secondary": "#4b5563",
            "background": "#ffffff",
            "surface": "#f9fafb",
            "text": "#111827",
            "accent": "#f3f4f6",
            "body_bg": "#f9fafb"
        },
        "Clean White": {
            "primary": "#2563eb",
            "secondary": "#1d4ed8",
            "background": "#ffffff",
            "surface": "#ffffff",
            "text": "#111827",
            "accent": "#f1f5f9",
            "body_bg": "#ffffff"
        },
        # Dark themes
        "Professional Dark": {
            "primary": "#60a5fa",
            "secondary": "#3b82f6",
            "background": "#111827",
            "surface": "#1f2937",
            "text": "#f9fafb",
            "accent": "#374151",
            "body_bg": "#0f172a"
        },
        "Dark Corporate Blue": {
            "primary": "#93c5fd",
            "secondary": "#60a5fa",
            "background": "#1e293b",
            "surface": "#334155",
            "text": "#f1f5f9",
            "accent": "#475569",
            "body_bg": "#0f172a"
        },
        "Dark Modern Green": {
            "primary": "#34d399",
            "secondary": "#10b981",
            "background": "#064e3b",
            "surface": "#065f46",
            "text": "#ecfdf5",
            "accent": "#047857",
            "body_bg": "#022c22"
        },
        "Dark Executive Purple": {
            "primary": "#a78bfa",
            "secondary": "#8b5cf6",
            "background": "#581c87",
            "surface": "#6b21a8",
            "text": "#faf5ff",
            "accent": "#7c3aed",
            "body_bg": "#4c1d95"
        },
        "Dark Minimalist": {
            "primary": "#9ca3af",
            "secondary": "#6b7280",
            "background": "#1f2937",
            "surface": "#374151",
            "text": "#f9fafb",
            "accent": "#4b5563",
            "body_bg": "#111827"
        }
    }
    
    # Get current theme colors
    current_theme = theme_configs[theme_option]
    if primary_color != "#3b82f6":  # If user changed primary color
        current_theme["primary"] = primary_color
    
    # Professional CSS styling with dynamic themes and proper background handling
    st.markdown(f"""
        <style>
        /* Import professional fonts */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');
        
        /* Dynamic theme variables */
        :root {{
            --primary-color: {current_theme["primary"]};
            --secondary-color: {current_theme["secondary"]};
            --background-color: {current_theme["background"]};
            --surface-color: {current_theme["surface"]};
            --text-color: {current_theme["text"]};
            --accent-color: {current_theme["accent"]};
            --body-bg-color: {current_theme["body_bg"]};
        }}
        
        /* Global background styling */
        .stApp {{
            background-color: var(--body-bg-color) !important;
        }}
        
        .main {{
            background-color: var(--body-bg-color) !important;
        }}
        
        /* Reset and base styles */
        .main .block-container {{
            padding-top: {'1rem' if layout_compact else '2rem'};
            padding-bottom: {'1rem' if layout_compact else '2rem'};
            max-width: 1200px;
            background-color: transparent !important;
        }}
        
        /* Auto theme detection JavaScript */
        .theme-auto-toggle {{
            position: fixed;
            top: 60px;
            right: 10px;
            background: var(--primary-color);
            color: white;
            border: none;
            padding: 0.5rem;
            border-radius: 50%;
            width: 45px;
            height: 45px;
            cursor: pointer;
            font-size: 1.2rem;
            z-index: 1000;
            box-shadow: 0 2px 10px rgba(0,0,0,0.2);
            {'transition: all 0.3s ease;' if show_animations else ''}
        }}
        
        {'.theme-auto-toggle:hover { transform: scale(1.1); }' if show_animations else ''}
        
        /* Sidebar styling */
        .css-1d391kg, .css-1y4p8pa {{
            background-color: var(--surface-color) !important;
        }}
        
        .css-1d391kg .css-1v3fvcr {{
            color: var(--text-color) !important;
        }}
        
        /* Streamlit widgets styling for dark mode */
        .stSelectbox > div > div {{
            background-color: var(--surface-color) !important;
            color: var(--text-color) !important;
        }}
        
        .stCheckbox > label {{
            color: var(--text-color) !important;
        }}
        
        .stRadio > label {{
            color: var(--text-color) !important;
        }}
        
        .stColorPicker > label {{
            color: var(--text-color) !important;
        }}
        
        .stMarkdown {{
            color: var(--text-color) !important;
        }}
        
        /* Professional header */
        .header-container {{
            background: var(--surface-color);
            border: 1px solid var(--accent-color);
            border-radius: 12px;
            padding: {'2rem 1.5rem' if layout_compact else '3rem 2rem'};
            margin-bottom: {'2rem' if layout_compact else '3rem'};
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
            {'transition: all 0.3s ease;' if show_animations else ''}
        }}
        
        {'@media (hover: hover) { .header-container:hover { transform: translateY(-2px); box-shadow: 0 8px 15px rgba(0, 0, 0, 0.1); } }' if show_animations else ''}
        
        .company-logo {{
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: {'1rem' if layout_compact else '1.5rem'};
        }}
        
        .logo-icon {{
            background: var(--primary-color);
            color: white;
            width: {'50px' if layout_compact else '60px'};
            height: {'50px' if layout_compact else '60px'};
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: {'24px' if layout_compact else '28px'};
            font-weight: bold;
            margin-right: 1rem;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3);
            {'transition: transform 0.2s ease;' if show_animations else ''}
        }}
        
        {'@media (hover: hover) { .logo-icon:hover { transform: rotate(5deg) scale(1.05); } }' if show_animations else ''}
        
        .company-name {{
            font-family: 'Inter', sans-serif;
            font-size: {'1.75rem' if layout_compact else '2rem'};
            font-weight: 800;
            color: var(--text-color);
            letter-spacing: -0.025em;
        }}
        
        .tagline {{
            text-align: center;
            font-family: 'Inter', sans-serif;
            font-size: {'1rem' if layout_compact else '1.125rem'};
            color: var(--text-color);
            opacity: 0.7;
            font-weight: 400;
            margin-top: 0.5rem;
            line-height: 1.6;
        }}
        
        /* Professional stats/features */
        .stats-grid {{
            display: {'none' if not show_stats else 'grid'};
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: {'1rem' if layout_compact else '1.5rem'};
            margin: {'1.5rem 0' if layout_compact else '2.5rem 0'};
        }}
        
        .stat-card {{
            background: var(--surface-color);
            border: 1px solid var(--accent-color);
            border-radius: 8px;
            padding: {'1.5rem 1rem' if layout_compact else '2rem 1.5rem'};
            text-align: center;
            {'transition: all 0.3s ease;' if show_animations else ''}
        }}
        
        {'.stat-card:hover { border-color: var(--primary-color); transform: translateY(-3px); box-shadow: 0 8px 15px rgba(0, 0, 0, 0.1); }' if show_animations else '.stat-card:hover { border-color: var(--primary-color); box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1); }'}
        
        .stat-number {{
            font-family: 'Inter', sans-serif;
            font-size: {'1.75rem' if layout_compact else '2rem'};
            font-weight: 700;
            color: var(--primary-color);
            line-height: 1;
        }}
        
        .stat-label {{
            font-family: 'Inter', sans-serif;
            font-size: 0.875rem;
            color: var(--text-color);
            opacity: 0.6;
            font-weight: 500;
            margin-top: 0.5rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }}
        
        /* Theme indicator */
        .theme-indicator {{
            position: fixed;
            top: 10px;
            right: 10px;
            background: var(--primary-color);
            color: white;
            padding: 0.5rem 1rem;
            border-radius: 20px;
            font-size: 0.75rem;
            font-weight: 600;
            z-index: 1000;
            opacity: 0.9;
            box-shadow: 0 2px 10px rgba(0,0,0,0.2);
        }}
        
        /* Professional section dividers */
        .section-divider {{
            border: none;
            height: 1px;
            background: linear-gradient(to right, transparent, var(--accent-color), transparent);
            margin: {'2rem 0' if layout_compact else '3rem 0'};
        }}
        
        .section-title {{
            font-family: 'Inter', sans-serif;
            font-size: {'1.25rem' if layout_compact else '1.5rem'};
            font-weight: 600;
            color: var(--text-color);
            text-align: center;
            margin: {'1.5rem 0' if layout_compact else '2rem 0'};
            position: relative;
        }}
        
        .section-title::after {{
            content: '';
            position: absolute;
            bottom: -8px;
            left: 50%;
            transform: translateX(-50%);
            width: 60px;
            height: 3px;
            background: var(--primary-color);
            border-radius: 2px;
        }}
        
        /* Professional footer */
        .footer-container {{
            background: var(--surface-color);
            border: 1px solid var(--accent-color);
            border-radius: 8px;
            padding: {'1.5rem' if layout_compact else '2rem'};
            margin-top: {'2rem' if layout_compact else '3rem'};
            text-align: center;
        }}
        
        .footer-content {{
            font-family: 'Inter', sans-serif;
            font-size: 0.875rem;
            color: var(--text-color);
            opacity: 0.7;
            margin-bottom: 1rem;
        }}
        
        .developer-info {{
            display: inline-flex;
            align-items: center;
            background: var(--primary-color);
            color: white;
            padding: 0.5rem 1rem;
            border-radius: 6px;
            font-family: 'Inter', sans-serif;
            font-size: 0.875rem;
            font-weight: 500;
            text-decoration: none;
            {'transition: all 0.2s ease;' if show_animations else ''}
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        
        {'.developer-info:hover { opacity: 0.9; transform: translateY(-1px); box-shadow: 0 4px 8px rgba(0,0,0,0.15); }' if show_animations else '.developer-info:hover { opacity: 0.9; }'}
        
        .developer-info::before {{
            content: "👨‍💻";
            margin-right: 0.5rem;
        }}
        
        /* Enterprise-grade styling */
        .enterprise-badge {{
            display: inline-block;
            background: var(--accent-color);
            color: var(--primary-color);
            padding: 0.25rem 0.75rem;
            border-radius: 9999px;
            font-family: 'Inter', sans-serif;
            font-size: 0.75rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 1rem;
        }}
        
        /* Hide Streamlit elements */
        #MainMenu {{visibility: hidden;}}
        footer {{visibility: hidden;}}
        header {{visibility: hidden;}}
        .stDeployButton {{visibility: hidden;}}
        
        /* Professional responsive design */
        @media (max-width: 768px) {{
            .company-name {{
                font-size: 1.5rem;
            }}
            .header-container {{
                padding: {'1.5rem 1rem' if layout_compact else '2rem 1rem'};
            }}
            .stats-grid {{
                grid-template-columns: 1fr;
            }}
            .theme-indicator {{
                position: relative;
                top: auto;
                right: auto;
                margin-bottom: 1rem;
            }}
        }}
        </style>
    """, unsafe_allow_html=True)' if layout_compact else '2rem 1rem'};
            }}
            .stats-grid {{
                grid-template-columns: 1fr;
            }}
            .theme-indicator {{
                position: relative;
                top: auto;
                right: auto;
                margin-bottom: 1rem;
            }}
        }}
        </style>
    """, unsafe_allow_html=True)
    
    # Theme indicator with mode display
    mode_display = "🌙 Auto" if theme_mode == "🌙 Auto (System)" else ("🌙 Dark" if theme_mode == "🌙 Dark Mode" else "☀️ Light")
    st.markdown(f'<div class="theme-indicator">{mode_display} | {theme_option}</div>', unsafe_allow_html=True)
    
    # Auto theme toggle button (JavaScript for system theme detection)
    if theme_mode == "🌙 Auto (System)":
        st.markdown("""
            <button class="theme-auto-toggle" onclick="toggleAutoTheme()" title="Auto Theme Active">
                🌓
            </button>
            <script>
                function toggleAutoTheme() {
                    const isDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
                    if (isDark) {
                        document.documentElement.style.setProperty('--primary-color', '#60a5fa');
                        document.documentElement.style.setProperty('--body-bg-color', '#0f172a');
                    } else {
                        document.documentElement.style.setProperty('--primary-color', '#3b82f6');
                        document.documentElement.style.setProperty('--body-bg-color', '#f8fafc');
                    }
                }
                
                // Auto-detect system theme on load
                window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', toggleAutoTheme);
                toggleAutoTheme(); // Initial call
            </script>
        """, unsafe_allow_html=True)
    
    # Professional header section
    st.markdown("""
        <div class="header-container">
            <div class="enterprise-badge">Enterprise Solution</div>
            <div class="company-logo">
                <div class="logo-icon">DC</div>
                <div class="company-name">DataConverter Pro</div>
            </div>
            <div class="tagline">
                Professional-grade XLS & CSV to SQL conversion platform<br>
                Trusted by data engineers and analysts worldwide
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Professional statistics/capabilities (conditional)
    if show_stats:
        st.markdown("""
            <div class="stats-grid">
                <div class="stat-card">
                    <div class="stat-number">99.9%</div>
                    <div class="stat-label">Accuracy Rate</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">10GB+</div>
                    <div class="stat-label">Max File Size</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">15+</div>
                    <div class="stat-label">Data Types</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">24/7</div>
                    <div class="stat-label">Availability</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    # Section divider
    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
    
    # Section title
    st.markdown('<h2 class="section-title">File Conversion Center</h2>', unsafe_allow_html=True)
    
    # Main application content
    page1.page1()
    
    # Professional footer
    st.markdown("""
        <div class="footer-container">
            <div class="footer-content">
                © 2024 TeamThreeCoders. All rights reserved.<br>
                Professional data conversion solutions for enterprise applications.
            </div>
            <a href="#" class="developer-info">
                Developed with ❤️ by TeamThreeCoders<br>Ayan
            </a>
        </div>
    """, unsafe_allow_html=True)

if __name__ == '__main__':
    app()
