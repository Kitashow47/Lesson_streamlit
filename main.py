import streamlit as st
import time

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.01)

'Done!!!!!!'


left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')

expander1 = st.expander('問い合わせ')
expander1.write('問い合わせ内容を書く')
expander2 = st.expander('問い合わせ')
expander2.write('問い合わせ内容を書く')
expander3 = st.expander('問い合わせ')
expander3.write('問い合わせ内容を書く')
expander4 = st.expander('問い合わせ')
expander4.write('問い合わせ内容を書く')



# if st.checkbox('Show Image'):
#     img = Image.open('sample.png')
#     st.image(img, caption='Sample', use_column_width=True)

# text = st.text_input('あなたの趣味を教えて下さい')
# condition = st.slider('あなたの今の調子は？', 0, 100, 50)

# 'あなたの趣味は、', text
# 'コンディション:', condition


