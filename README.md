# 1. Tạo môi trường ảo tên kiemtra
python3 -m venv kiemtra

# 2. Kích hoạt môi trường ảo
source kiemtra/bin/activate

# 3. Cài đặt các thư viện cần thiết (Streamlit và Matplotlib)
pip install streamlit matplotlib

nano app.py

# chạy trên cổng 5175
streamlit run app.py --server.port 5175

# Kích hoạt môi trường ảo kiemtra (nếu bạn mới mở lại terminal/VS Code):

source kiemtra/bin/activate
Chạy ứng dụng Web trên cổng 5175:

streamlit run app.py --server.port 5175

# flask 
pip install flask matplotlib

python app.py

# git

git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:Quanh2le5/kiemtra.git
git push -u origin main