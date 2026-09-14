from flask import Flask, request, render_template_string
import matplotlib
matplotlib.use('Agg')  # Sử dụng backend không hiển thị GUI để tránh lỗi trên server
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Thống Kê Sinh Viên</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background-color: #f4f6f9; }
        .container { max-width: 500px; margin: 0 auto; padding: 20px; background: white; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
        .form-group { margin-bottom: 15px; }
        label { display: block; margin-bottom: 5px; font-weight: bold; }
        input[type="number"] { width: 95%; padding: 8px; border: 1px solid #ccc; border-radius: 4px; }
        button { width: 100%; padding: 10px; background-color: #007bff; color: white; border: none; border-radius: 4px; cursor: pointer; font-size: 16px; margin-top: 10px; }
        button:hover { background-color: #0056b3; }
        .result { margin-top: 20px; text-align: center; }
        img { max-width: 100%; height: auto; margin-top: 15px; border-radius: 4px; }
    </style>
</head>
<body>
    <div class="container">
        <h2>Nhập Số Lượng Sinh Viên</h2>
        <form method="POST">
            <div class="form-group">
                <label for="nam">Số sinh viên Nam:</label>
                <input type="number" id="nam" name="nam" min="0" value="{{ nam|default(25) }}" required>
            </div>
            <div class="form-group">
                <label for="nu">Số sinh viên Nữ:</label>
                <input type="number" id="nu" name="nu" min="0" value="{{ nu|default(15) }}" required>
            </div>
            <button type="submit">Vẽ Biểu Đồ</button>
        </form>

        {% if chart_url %}
            <div class="result">
                <h3>Kết Quả Thống Kê</h3>
                <p><strong>Tổng số sinh viên:</strong> {{ tong }}</p>
                <img src="data:image/png;base64,{{ chart_url }}" alt="Biểu đồ Nam Nữ">
            </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    chart_url = None
    tong = 0
    nam = 25
    nu = 15

    if request.method == 'POST':
        nam = int(request.form.get('nam', 0))
        nu = int(request.form.get('nu', 0))
        tong = nam + nu

        # Vẽ biểu đồ bằng Matplotlib
        fig, ax = plt.subplots(figsize=(6, 4))
        categories = ['Nam', 'Nữ']
        counts = [nam, nu]
        colors = ['#007bff', '#e83e8c']

        bars = ax.bar(categories, counts, color=colors, width=0.4)
        ax.set_ylabel('Số lượng')
        ax.set_title('Biểu đồ Nam / Nữ trong lớp')
        ax.set_ylim(0, max(counts) + 5 if max(counts) > 0 else 10)

        for bar in bars:
            yval = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, yval + 0.3, int(yval), ha='center', va='bottom', fontweight='bold')

        # Chuyển đổi biểu đồ thành chuỗi hình ảnh Base64 để hiển thị trực tiếp lên HTML
        img = io.BytesIO()
        plt.savefig(img, format='png', bbox_inches='tight')
        img.seek(0)
        chart_url = base64.b64encode(img.getvalue()).decode('utf8')
        plt.close()

    return render_template_string(HTML_TEMPLATE, chart_url=chart_url, tong=tong, nam=nam, nu=nu)

if __name__ == '__main__':
    # Đổi cổng dễ dàng tại thông số port (ví dụ: port=5175)
    app.run(host='0.0.0.0', port=5173, debug=True)