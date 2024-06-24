import streamlit as st

st.title("Dental Payment Form")

tien_cao_voi = 100_000
tien_tay_trang = 1_200_000
tien_chup_rang = 200_000
total = 0

st.text_input("Tên khách hàng", "")
if st.checkbox("Cạo vôi"):
    first_expense = tien_cao_voi
else:
    first_expense = tien_chup_rang + tien_tay_trang
st.text(body="$"+str(tien_cao_voi))
if st.checkbox("Tẩy trắng"):
    first_expense = tien_tay_trang
else:
    first_expense = tien_cao_voi + tien_chup_rang
st.text(body="$"+str(tien_tay_trang))
if st.checkbox("Chụp hình răng"):
    first_expense = tien_chup_rang
else:
    first_expense = tien_cao_voi + tien_tay_trang
st.text(body="$"+str(tien_chup_rang))

tooth = st.number_input("Trám răng", 0, 20, value=0, step=1)
st.text(body="$"+str(200_000)+"/cái")

tien_tram_rang = tooth*200_000
total = first_expense + tien_tram_rang

if st.button("Thoát"):
    st.experimental_rerun()
if st.button("Tính tiền"):
    st.write(f"Total: {total}")
