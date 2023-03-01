import streamlit as st
from pathlib import Path
from PIL import Image

dir_atual = Path.cwd()
curriculo = dir_atual / "files/CV Guilherme China - Jovem aprendiz.pdf"

css_file = dir_atual / "styles" / "style.css"
foto_perfil = dir_atual / "files/pic_oficial.png"

foto = Image.open(foto_perfil)

redes_sociais = {"Linkedin": "https://www.linkedin.com/in/guilherme-china-03b23b268/",
                 "Github": "https://github.com/Chininha"}

projetos = {"Dashboards Gasômetros - Relatório geral por consulta API": "https://metricas-ici2023.streamlit.app/",
            "Medalhista na AIMO (Asia International Olympiad Union) – setembro de 2020": 
            "https://mail.google.com/mail/u/0?ui=2&ik=d60f0435d4&attid=0.2&permmsgid=msg-a:r368174390206690353&th=182b290424692707&view=att&disp=inline&realattid=f_l6zgspy12",
            "Projeto FEBRACE - Experimento digital para determinação de constantes elástica": "https://mail.google.com/mail/u/0?ui=2&ik=d60f0435d4&attid=0.1&permmsgid=msg-a:r7975429503004726762&th=1869d482be3b2e98&view=att&disp=inline&realattid=f_lepoyxaf0"}

cursos = {"Hashtag Treinamentos": "Curso Python Impressionador",
          "Curso em Vídeo": "Curso de fundamentos do Python",
          "English Yourself": "Curso de inglês online - 2020"}

hard_skills = {"- 👩‍💻 Programming": "Python (Pandas, Numpy, Streamlit), SQL",
"- 📊 Data Visulization": "Plotly, Matplotlib, Seaborn",
"- 🗄️ Databases": "MySQL, Oracle SQL Developer, Oracle Data Modeler"}

with open(curriculo, "rb") as curriculo_pdf:
    arquivo = curriculo_pdf.read()

st.set_page_config(
    page_title="Digital CV | Guilherme China",
    layout="centered"
)

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)


col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(foto, width=230)

with col2:
    st.title("Guilherme China")
    st.write("Graduando de Ciência de Dados, auxiliar de escritório focado em manipulação de dados e tomada de decisões")
    st.download_button(label=":memo: Download resume",
                       data=arquivo,
                       file_name=curriculo.name,
                       mime="application/octet-stream")
    st.write("📫 Echina725@gmail.com")
    st.write(":telephone_receiver: (55) 119499-40557")
    for indice, (rede, link) in enumerate(redes_sociais.items()):
        st.write(f":computer: [{rede}]({link})")
    


# ------------ REDES SOCIAIS ------------------
colunas_redes = st.columns(len(redes_sociais) + 2, gap="small")
# for indice, (rede, link) in enumerate(redes_sociais.items()):
#     colunas_redes[indice].write(f"| [{rede}]({link})")

# ----------- Qualificações -----------------
st.write("#")
st.subheader("Experiências & Qualificações")
st.write("---")
st.write(
    """
- ✔️ Ensino Médio completo
\n- ✔️ Cursando Ciência de Dados na FIAP
\n- ✔️ Inglês avançado
""")

# ----------- skills ---------------------------
st.markdown("#")
st.subheader("Hard Skills")
st.write("---")

for skill, nome in hard_skills.items():
    st.write(f"{skill} - {nome}")

st.markdown("#")
st.subheader("Cursos")
st.write("---")
for curso, nome in cursos.items():
    st.write(f"- :pencil2: {curso} - {nome}")

st.markdown("#")
st.subheader("Projetos")
st.write("---")
for projeto, link in projetos.items():
    st.write(f"- :trophy: [{projeto}]({link})")

