# package
import streamlit as st
import webPages.page1 as page1

def app():
    # Configure page with better settings
    st.set_page_config(
        page_title="XLS & CSV to SQL Converter",
        page_icon="🔄",  # Using emoji as fallback, keep your custom icon if preferred
        layout="wide",  # Changed to wide for better space utilization
        initial_sidebar_state="collapsed"
    )
    
    # Custom CSS for enhanced styling
    st.markdown("""
        <style>
        /* Import Google Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        
        /* Main app styling */
        .main-header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 2rem 0;
            margin: -1rem -1rem 2rem -1rem;
            border-radius: 0 0 20px 20px;
            text-align: center;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        }
        
        .main-title {
            color: white;
            font-family: 'Inter', sans-serif;
            font-size: 2.5rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
        }
        
        .main-subtitle {
            color: rgba(255, 255, 255, 0.9);
            font-family: 'Inter', sans-serif;
            font-size: 1.2rem;
            font-weight: 300;
            margin-bottom: 0;
        }
        
        /* Feature highlights */
        .feature-container {
            display: flex;
            justify-content: space-around;
            margin: 2rem 0;
            gap: 1rem;
        }
        
        .feature-card {
            background: linear-gradient(145deg, #ffffff, #f0f2f6);
            padding: 1.5rem;
            border-radius: 15px;
            text-align: center;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
            border: 1px solid rgba(255, 255, 255, 0.2);
            transition: transform 0.3s ease;
            flex: 1;
            max-width: 300px;
        }
        
        .feature-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
        }
        
        .feature-icon {
            font-size: 2.5rem;
            margin-bottom: 1rem;
        }
        
        .feature-title {
            font-family: 'Inter', sans-serif;
            font-weight: 600;
            font-size: 1.1rem;
            color: #2c3e50;
            margin-bottom: 0.5rem;
        }
        
        .feature-desc {
            font-family: 'Inter', sans-serif;
            font-size: 0.9rem;
            color: #7f8c8d;
            line-height: 1.4;
        }
        
        /* Footer styling */
        .footer {
            margin-top: 3rem;
            padding: 2rem 0;
            background: linear-gradient(90deg, #f8f9fa, #e9ecef);
            border-radius: 15px;
            text-align: center;
            border: 1px solid #dee2e6;
        }
        
        .footer-content {
            font-family: 'Inter', sans-serif;
            font-size: 1rem;
            color: #6c757d;
            font-weight: 500;
        }
        
        .author-badge {
            display: inline-flex;
            align-items: center;
            background: linear-gradient(135deg, #ff6b6b, #ee5a24);
            color: white;
            padding: 0.5rem 1rem;
            border-radius: 25px;
            font-weight: 600;
            text-decoration: none;
            margin-top: 0.5rem;
            box-shadow: 0 4px 15px rgba(238, 90, 36, 0.3);
            transition: all 0.3s ease;
        }
        
        .author-badge:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(238, 90, 36, 0.4);
        }
        
        /* Custom divider */
        .custom-divider {
            height: 2px;
            background: linear-gradient(90deg, transparent, #667eea, transparent);
            border: none;
            margin: 2rem 0;
        }
        
        /* Hide Streamlit branding */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* Responsive design */
        @media (max-width: 768px) {
            .main-title {
                font-size: 2rem;
            }
            .feature-container {
                flex-direction: column;
                align-items: center;
            }
            .feature-card {
                max-width: 100%;
                margin-bottom: 1rem;
            }
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Enhanced header
    st.markdown("""
        <div class="main-header">
            <h1 class="main-title">🔄 XLS & CSV to SQL Converter</h1>
            <p class="main-subtitle">Transform your data files into powerful SQL statements with ease</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Feature highlights
    st.markdown("""
        <div class="feature-container">
            <div class="feature-card">
                <div class="feature-icon">📊</div>
                <div class="feature-title">Multiple Formats</div>
                <div class="feature-desc">Support for XLS, XLSX, and CSV files</div>
            </div>
            <div class="feature-card">
                <div class="feature-icon">⚡</div>
                <div class="feature-title">Fast Processing</div>
                <div class="feature-desc">Quick conversion to DDL and DML statements</div>
            </div>
            <div class="feature-card">
                <div class="feature-icon">🎯</div>
                <div class="feature-title">Accurate Results</div>
                <div class="feature-desc">Precise data type detection and mapping</div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Custom divider
    st.markdown('<hr class="custom-divider">', unsafe_allow_html=True)
    
    # Main content
    page1.page1()
    
    # Enhanced footer
    st.markdown("""
        <div class="footer">
            <div class="footer-content">
                Made with passion and precision
                <br>
                <a href="#" class="author-badge">
                    ❤️ Developed by Ayan
                </a>
            </div>
        </div>
    """, unsafe_allow_html=True)

if __name__ == '__main__':
    app()
