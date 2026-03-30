import streamlit as st
import json
import os

DATA_FILE = "inventory.json"

# 初始化数据
def init_data():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump({}, f, ensure_ascii=False, indent=4)

# 读取数据
def load_data():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

# 保存数据
def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# ======================
# 网页界面开始
# ======================
st.set_page_config(page_title="仓库管理系统", layout="wide")
st.title("📦 仓库库存管理系统")

init_data()
data = load_data()

# 菜单
menu = st.sidebar.radio("功能菜单", ["查看库存", "商品入库", "商品出库"])

if menu == "查看库存":
    st.subheader("当前库存列表")
    if data:
        for name, num in data.items():
            st.write(f"✅ {name}：{num} 件")
    else:
        st.write("暂无库存数据")

elif menu == "商品入库":
    st.subheader("商品入库")
    name = st.text_input("商品名称")
    count = st.number_input("入库数量", min_value=1, step=1)
    
    if st.button("确认入库"):
        if name.strip() == "":
            st.warning("请输入商品名称")
        else:
            if name in data:
                data[name] += count
            else:
                data[name] = count
            save_data(data)
            st.success(f"✅ {name} 入库成功！当前库存：{data[name]}")

elif menu == "商品出库":
    st.subheader("商品出库")
    name = st.text_input("商品名称")
    count = st.number_input("出库数量", min_value=1, step=1)
    
    if st.button("确认出库"):
        if name not in data:
            st.error("❌ 商品不存在")
        elif data[name] < count:
            st.error("❌ 库存不足")
        else:
            data[name] -= count
            save_data(data)
            st.success(f"✅ {name} 出库成功！当前库存：{data[name]}")