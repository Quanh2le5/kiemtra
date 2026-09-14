import streamlit as st
import matplotlib.pyplot as plt

st.title("Quản lý & Thống kê Sinh viên Nam/Nữ")

# Form nhập liệu
st.header("Nhập số lượng sinh viên trong lớp")
nam = st.number_input("Số lượng sinh viên Nam:", min_value=0, value=25, step=1)
nu = st.number_input("Số lượng sinh viên Nữ:", min_value=0, value=15, step=1)

# Nút hiển thị biểu đồ
if st.button("Hiển thị biểu đồ"):
    tong = nam + nu
    st.write(f"**Tổng số sinh viên:** {tong}")
    
    # Vẽ biểu đồ cột
    fig, ax = plt.subplots(figsize=(6, 4))
    gioi_tinh = ['Nam', 'Nữ']
    so_luong = [nam, nu]
    colors = ['#1f77b4', '#e377c2']
    
    bars = ax.bar(gioi_tinh, so_luong, color=colors, width=0.4)
    ax.set_ylabel('Số lượng')
    ax.set_title('Biểu đồ so sánh số lượng Nam và Nữ trong lớp')
    ax.set_ylim(0, max(so_luong) + 5 if max(so_luong) > 0 else 10)
    
    # Hiển thị số liệu trên đỉnh mỗi cột
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval + 0.5, int(yval), ha='center', va='bottom', fontweight='bold')
    
    # Hiển thị biểu đồ lên giao diện Web Streamlit
    st.pyplot(fig)
