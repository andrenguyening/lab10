import streamlit as st
import sqlite3
from jinja2 import Template

# Function to fetch poems from the database
def fetch_poems():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT title, author, text FROM poems')
    poems = cursor.fetchall()
    conn.close()
    return poems

# Render poem template with Jinja2
def render_poem_template(poem):
    template_str = '''
    <h2>{{ poem.title }}</h2>
    <p><em>By {{ poem.author }}</em></p>
    <pre>{{ poem.text }}</pre>
    '''
    template = Template(template_str)
    return template.render(poem=poem)

# Main Streamlit app
def main():
    st.title('Poems Display App')
    
    # Fetch poems from the database
    poems = fetch_poems()

    # Display each poem
    for idx, poem in enumerate(poems, start=1):
        st.markdown(render_poem_template({'title': poem[0], 'author': poem[1], 'text': poem[2]}), unsafe_allow_html=True)
        if idx < len(poems):
            st.write('---')

if __name__ == '__main__':
    main()
