import streamlit as st

if 'posts' not in st.session_state:
    st.session_state.posts = []
st.title('シバ犬')

post_content = st.text_input('にゅ～～りょく')

if st.button('send'):
    if post_content:
        st.success('success')
        st.session_state.posts.append(post_content)
    else:
        st.error('text is null')
for post in st.session_state.posts:
    st.text_area('投稿内容',post)


#実行文
#python -m streamlit run X.py