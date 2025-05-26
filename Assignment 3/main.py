import streamlit as st

st.set_page_config(page_title=" Personal Library Manager", layout="centered")

if "library" not in st.session_state:
    st.session_state.library = []

st.title("📚 Personal Library Manager")

st.header("➕ Add a New Book")

with st.form("book_form", clear_on_submit=True):
    title = st.text_input("Book Title", max_chars=100)
    author = st.text_input("Author", max_chars=100)
    genre = st.text_input("Genre", max_chars=50)
    year = st.number_input("Publication Year", min_value=0, max_value=2100, step=1)
    submitted = st.form_submit_button("Add Book")

    if submitted:
        if title and author:
            new_book = {
                "Title": title,
                "Author": author,
                "Genre": genre,
                "Year": int(year)
            }
            st.session_state.library.append(new_book)
            st.success(f" Book '{title}' added to your library.")
        else:
            st.error(" Title and Author are required!")

st.header(" Your Book Collection")

search = st.text_input(" Search by title or author")

filtered_books = [
    book for book in st.session_state.library
    if search.lower() in book["Title"].lower() or search.lower() in book["Author"].lower()
]

if filtered_books:
    for i, book in enumerate(filtered_books):
        st.markdown(f"**{book['Title']}** by *{book['Author']}* ({book['Year']}) — {book['Genre']}")
        if st.button(" Remove", key=f"remove_{i}"):
            st.session_state.library.remove(book)
            st.experimental_rerun()
else:
    st.info("No books found. Try adding some or refine your search.")

if st.session_state.library:
    if st.button(" Clear Entire Library"):
        st.session_state.library.clear()
        st.success("All books removed.")
