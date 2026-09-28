import matplotlib.pyplot as plt
import streamlit as st

# ==========================================
# 1. CẤU HÌNH TRANG & CSS (VIẾT TRỰC TIẾP IN-FILE)
# ==========================================
st.set_page_config(
    page_title="Thống kê sinh viên",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Gộp toàn bộ CSS vào chuỗi biến này
CUSTOM_CSS = """
<style>
    /* Nền trang chính */
    .stApp {
        background-color: #0e1117;
        font-family: 'Segoe UI', Roboto, sans-serif;
    }

    /* Kiểu dáng cho Tiêu đề */
    h1 {
        color: #00d2ff;
        text-align: center;
        font-weight: 700;
        padding-bottom: 15px;
    }

    /* Đổi kiểu cho ô nhập liệu */
    div[data-baseweb="input"] {
        border-radius: 8px;
    }

    /* Nút bấm nổi bật */
    div.stButton > button {
        width: 100%;
        background-color: #00d2ff;
        color: #000000;
        font-weight: bold;
        border-radius: 8px;
        border: none;
        padding: 10px 0;
        transition: all 0.3s ease;
    }

    div.stButton > button:hover {
        background-color: #00a8cc;
        color: #ffffff;
        transform: translateY(-2px);
    }
</style>
"""

# Nhúng CSS vào giao diện Streamlit
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


# ==========================================
# 2. HÀM XỬ LÝ V VẼ BIỂU ĐỒ (LOGIC RIÊNG)
# ==========================================
def ve_bieu_do_sinh_vien(so_nam, so_nu):
    """Hàm tách biệt chuyên dùng để vẽ biểu đồ"""
    gioi_tinh = ['Nam', 'Nữ']
    so_luong = [so_nam, so_nu]
    mau_sac = ['#3498db', '#e74c3c']

    # Cấu hình giao diện biểu đồ tối (Dark Mode)
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(6, 4))
    fig.patch.set_facecolor('#0e1117')
    ax.set_facecolor('#0e1117')

    # Vẽ cột
    cot = ax.bar(gioi_tinh, so_luong, color=mau_sac, width=0.4)

    # Hiển thị số lượng lên đỉnh cột
    for c in cot:
        yval = c.get_height()
        ax.text(
            c.get_x() + c.get_width() / 2, 
            yval + 0.3, 
            f'{int(yval)}', 
            ha='center', 
            va='bottom',
            color='white',
            fontweight='bold'
        )

    # Trang trí trục & Đường lưới
    ax.set_ylabel('Số lượng (sinh viên)', color='#cccccc')
    ax.set_ylim(0, max(so_luong) + 5 if max(so_luong) > 0 else 10)
    ax.grid(axis='y', linestyle='--', alpha=0.2)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    return fig


# ==========================================
# 3. GIAO DIỆN CHÍNH (UI LOGIC)
# ==========================================
st.title("Thống kê số lượng sinh viên Nam - Nữ")

# Chia cột nhập liệu
col1, col2 = st.columns(2)
with col1:
    so_nam = st.number_input("Nhập số sinh viên Nam:", min_value=0, value=20, step=1)
with col2:
    so_nu = st.number_input("Nhập số sinh viên Nữ:", min_value=0, value=10, step=1)

# Nút bấm và vẽ
if st.button("Vẽ biểu đồ"):
    fig = ve_bieu_do_sinh_vien(so_nam, so_nu)
    st.pyplot(fig)