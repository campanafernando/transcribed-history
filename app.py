import streamlit as st

st.title("Transcribed History 📚📑")

st.markdown("<h3>Fim da República Oligárquica e o Estado Novo: Transições Políticas e Consolidação do Poder no Brasil</h3>", unsafe_allow_html=True)

st.info("R")

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
    ["Introdução", 
     "República Oligárquica", 
     "Revolução de 1930", 
     "Caminho para o Estado Novo", 
     "Estado Novo", 
     "Consequências e Fim"])

with tab1:
    st.markdown("<h3>Introdução</h3>", unsafe_allow_html=True)
    st.write("""
        A transição da República Oligárquica (1889-1930) para o Estado Novo (1937-1945) marcou um ponto de virada na história política brasileira. O primeiro período foi caracterizado pelo domínio das oligarquias estaduais, especialmente de São Paulo e Minas Gerais, que controlavam o poder por meio da política do “café com leite”. O fim dessa era, com a Revolução de 1930, levou à ascensão de Getúlio Vargas e à consolidação de um regime autoritário durante o Estado Novo. Este artigo visa analisar as principais características dessa transição, bem como as mudanças estruturais no Estado brasileiro.
    """)

    st.image('oligarquica-7.jpg', caption="A imagem critica o coronelismo durante a República Oligárquica (1889-1930), destacando o controle das oligarquias sobre as eleições, simbolizado pelo voto de cabresto, onde o eleitor era coagido a votar conforme os interesses dos poderosos regionais")

with tab2:
    st.markdown("<h3>A República Oligárquica: Características e Declínio</h3>", unsafe_allow_html=True)
    st.write("""
        A República Oligárquica foi marcada por um sistema de poder baseado na aliança entre as elites estaduais. Essa forma de governo favorecia a manutenção dos interesses agrários, particularmente o setor cafeeiro, que exercia enorme influência econômica e política. O poder central era enfraquecido, e o federalismo permitia que os estados mais ricos controlassem suas políticas internas.

        No entanto, com a crise do café e a crescente industrialização, houve uma mudança no equilíbrio de poder. A urbanização e o crescimento de uma classe média e operária trouxeram novas demandas políticas e sociais. O movimento tenentista, que criticava a corrupção e a falta de participação popular, juntamente com o descontentamento das classes urbanas e setores militares, desestabilizou o poder oligárquico.

        A crise econômica de 1929, desencadeada pela quebra da Bolsa de Nova York, intensificou esses problemas ao reduzir drasticamente o preço do café, principal produto de exportação brasileiro. Como resultado, as oligarquias enfrentaram maior oposição, o que abriu caminho para a Revolução de 1930.
    """)

    st.image('oligarquica-2.jpg', caption="A imagem satiriza o coronelismo durante a República Oligárquica, com o coronel usando uma chibata para forçar o eleitor a votar.")

with tab3:
    st.markdown("<h3>Revolução de 1930 e Ascensão de Getúlio Vargas</h3>", unsafe_allow_html=True)
    st.write("""
        A Revolução de 1930 foi o marco do fim da República Oligárquica. O movimento foi liderado por elites dissidentes, especialmente do Rio Grande do Sul, Minas Gerais e Paraíba, além de setores militares e civis descontentes com o domínio paulista. Após o fracasso da candidatura de Getúlio Vargas à presidência em 1930, contra o candidato apoiado pelos paulistas, Júlio Prestes, o descontentamento culminou em um golpe que depôs o então presidente Washington Luís.

        Com a deposição, Getúlio Vargas assumiu a presidência, inicialmente como líder provisório, e deu início a um processo de reestruturação do Estado brasileiro. Sua liderança buscava modernizar o Brasil, promovendo reformas trabalhistas e industriais, ao mesmo tempo em que consolidava seu poder político.
    """)

    st.image('oligarquica-3.jpg', caption="A imagem retrata uma manifestação popular durante a Revolução de 1930, com faixas de apoio à Aliança Liberal e ao movimento que culminou na ascensão de Getúlio Vargas.")

with tab4:
    st.markdown("<h3>O Caminho para o Estado Novo</h3>", unsafe_allow_html=True)
    st.write("""
        O período entre 1930 e 1937 foi marcado por tentativas de consolidação do poder varguista. Em 1934, uma nova Constituição foi promulgada, a qual estabelecia um regime de maior controle central, mas ainda mantinha alguns mecanismos democráticos. No entanto, o contexto internacional de ascensão de regimes totalitários, como o fascismo na Itália e o nazismo na Alemanha, influenciou Vargas a adotar uma postura mais autoritária.

        A ameaça do comunismo no Brasil, manifestada pela Revolta Comunista de 1935, foi usada como justificativa para o endurecimento do governo. Em 1937, Vargas alegou a descoberta de um suposto plano comunista, o Plano Cohen, para justificar um golpe que instaurou o Estado Novo.
    """)

    st.image('oligarquica-4.jpg', caption="A imagem mostra uma aglomeração de pessoas em uma manifestação de apoio a Getúlio Vargas, com faixas destacando a aprovação das políticas sociais do governo.")

with tab5:
    st.markdown("<h3>O Estado Novo: Autoritarismo e Centralização</h3>", unsafe_allow_html=True)
    st.write("""
        O Estado Novo foi um regime fortemente centralizador, marcado pela suspensão das liberdades civis e pela censura. Vargas fechou o Congresso, aboliu os partidos políticos e governou por meio de decretos. O regime utilizou a propaganda como uma ferramenta de controle social, exaltando a figura de Vargas como o “pai dos pobres” e defensor dos interesses nacionais.

        No plano econômico, o Estado Novo promoveu o desenvolvimento industrial, com destaque para a criação da Companhia Siderúrgica Nacional (CSN) em 1941, um dos marcos da industrialização brasileira. A política trabalhista de Vargas também teve um papel importante na sua legitimação junto às massas urbanas, por meio da consolidação das leis trabalhistas (CLT) e da criação de instituições de assistência social.
    """)

    st.image('oligarquica-5.jpg', caption="A imagem é uma forte crítica à censura e ao autoritarismo do Estado Novo. Mostra uma figura com uma mordaça em forma de cassetete, simbolizando a repressão à liberdade de expressão.")

with tab6:
    st.markdown("<h3>Consequências e Fim do Estado Novo</h3>", unsafe_allow_html=True)
    st.write("""
    O Estado Novo durou até 1945, quando o contexto internacional, marcado pelo fim da Segunda Guerra Mundial e o enfraquecimento dos regimes autoritários na Europa, pressionou Vargas a ceder o poder. A abertura política começou com o retorno das eleições e a formação de novos partidos. Vargas renunciou ao poder em outubro de 1945, sendo substituído por José Linhares, presidente do Supremo Tribunal Federal, até a realização de novas eleições.

O fim do Estado Novo deixou como legado uma estrutura política mais centralizada e um estado mais intervencionista, mas também marcou o início de um período de maior participação democrática no Brasil, com o retorno das eleições e da pluralidade partidária.
    """)

    st.image('oligarquica-6.jpg', caption='A imagem mostra uma manifestação de apoio a Getúlio Vargas no final do Estado Novo, com faixas pedindo sua permanência no poder, "com ou sem constituinte".')

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.caption('Isabella Campana')

with col2:
    st.caption('Gabriella Guerreiro')

with col3:
    st.caption('Ana Cecília ferreira')

with col4:
    st.caption('Ana Cecília Maldonado')

