mkdir -p ~/.steamlit/

echo"\
[general]\n\
email=\"21f1005309@student.onlinedegree.iitm.ac.in\"\n\
"> ~/.streamlit/credentials.toml"

echo"\
[server]\n\
headless = treu\n\
enableCORS = false\n\
port= $PORT\n\
" > ~/.streamlit/credentials.toml"