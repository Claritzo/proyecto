import streamlit as st
import pandas as pd

# Agregar una barra lateral al diseño
st.sidebar.title('Menú')

# Agregar elementos al menú como botones o selectores
opcion = st.sidebar.selectbox('Selecciona una opción', ['Consultas', 'Sistema de recomendacion'])

# Basado en la opción seleccionada, mostrar diferentes resultados en el cuerpo principal de la aplicación
if opcion == 'Consultas':
    st.title('CONSULTAS')
    st.write('Esta es la opción Consultas')




    df= pd.read_csv('./pelicula_etl.csv', sep=';')

    #**********************************************************************#
    # 1.                      Películas por Mes                            #
    #**********************************************************************#

    def peliculas_mes(mes):
        '''
            Se ingresa el mes y la funcion retorna la cantidad de peliculas que se estrenaron ese mes
        '''
        # Transformar el nombre del mes en su número correspondiente
        mes_n = mes
        
        if mes_n == 'Mes no válido':
            return 'Mes no válido'
        else:
            # Convertir la columna 'release_date' a tipo datetime
            df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
            
            # Filtrar por el mes dado y luego contar
            respuesta = df[df['release_date'].dt.month == mes_n]['title'].count()
            return {'mes': mes, 'cantidad': respuesta}

    # Interfaz de Streamlit
    st.title('1. Consulta de películas por mes')

    # Meses predefinidos
    meses = {'Enero': 1, 'Febrero': 2, 'Marzo': 3, 'Abril': 4, 'Mayo': 5, 'Junio': 6, 'Julio': 7,
            'Agosto': 8, 'Septiembre': 9, 'Octubre': 10, 'Noviembre': 11, 'Diciembre': 12}

    # Obtener el mes seleccionado por el usuario
    mes_seleccionado = st.selectbox('Seleccione un mes:', list(meses.keys()))

    # Llamar a la función peliculas_mes y mostrar el resultado

    resultado = peliculas_mes(meses[mes_seleccionado])
    #mes1 = (list(meses.keys())==resultado)
    if resultado == 'Mes no válido':
        st.error('Mes no válido. Por favor, seleccione un mes válido.')
    else:
        #
        if resultado['mes'] == 1:
            result1 = ' Enero'
        elif resultado['mes'] == 2:
            result1 = ' Febrero'
        elif resultado['mes'] == 3:
            result1 = ' Marzo'
        elif resultado['mes'] == 4:
            result1 = ' Abril'
        elif resultado['mes'] == 5:
            result1 = ' Mayo'
        elif resultado['mes'] == 6:
            result1 = ' Junio'
        elif resultado['mes'] == 7:
            result1 = ' Julio'
        elif resultado['mes'] == 8:
            result1 = ' Agosto'
        elif resultado['mes'] == 9:
            result1 = ' Septiembre'
        elif resultado['mes'] == 10:
            result1 = ' Octubre'
        elif resultado['mes'] == 11:
            result1 = ' Noviembre'
        elif resultado['mes'] == 12:
            result1 = ' Diciembre'
        else:
            result1 = 'Mes No Valido'
                
        st.write('Mes:', result1)
        st.write('Estrenos de Películas:', resultado['cantidad'])
            


    #**********************************************************************#
    #2.                 Películas por Día de la Semana                     #
    #**********************************************************************#

    def peliculas_dia(dia):
        '''
            Se ingresa el dia y la funcion retorna la cantidad de peliculas que se estrenaron ese dia.
        '''
        # Transformar el nombre del día en su número correspondiente
        dia_n = dia
        
        if dia_n == 'Día no válido':
            return 'Día no válido'
        else:
            # Convertir la columna 'release_date' a tipo datetime
            df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
            
            # Filtrar por el día dado y luego contar
            respuesta = df[df['release_date'].dt.dayofweek == dia_n]['title'].count()
            return {'dia': dia, 'cantidad': respuesta}

    # Interfaz de Streamlit
    st.title('2. Consulta de películas por día de la semana')

    # Días de la semana predefinidos
    dias = {'Lunes': 0, 'Martes': 1, 'Miércoles': 2, 'Jueves': 3, 'Viernes': 4, 'Sábado': 5, 'Domingo': 6}

    # Obtener el día seleccionado por el usuario
    dia_seleccionado = st.selectbox('Seleccione un día de la semana:', list(dias.keys()))

    # Llamar a la función peliculas_dia y mostrar el resultado

    resultado = peliculas_dia(dias[dia_seleccionado])
    if resultado == 'Día no válido':
        st.error('Día no válido. Por favor, seleccione un día válido.')
    else:
        result1 = 'Domingo'
        if resultado['dia'] == 0:
            result1 = 'Lunes'
        elif resultado['dia'] == 1:
            result1 = 'Martes'
        elif resultado['dia'] == 2:
            result1 = 'Miercoles'
        elif resultado['dia'] == 3:
            result1 = 'Jueves'
        elif resultado['dia'] == 4:
            result1 = 'Viernes'
        elif resultado['dia'] == 5:
            result1 = 'Sábado'
        else:
            result1 = 'Domingo'
        st.write('Día:', result1)
        st.write('Estrenos de Películas:', resultado['cantidad'])
            
    #**********************************************************************#
    #3.                    Películas por Franquicias                       #
    #**********************************************************************#

    def franquicia(franquicia):
        '''
            Se ingresa la franquicia, retornando la cantidad de peliculas, ganancia total y promedio
        '''
        # Nombres de las colecciones
        collection_names = df['belongs_to_collection'].unique()
        
        # Verificar si la franquicia es una entrada válida
        if franquicia in collection_names:
            franquicia = franquicia
        elif (franquicia + ' Collection') in collection_names:
            franquicia = (franquicia + ' Collection')
        else:
            return 'Colección no encontrada'
        
        # Calcular los resultados
        n_pelis = df[df['belongs_to_collection'] == franquicia]['title'].count()
        ganancia_total = df[df['belongs_to_collection'] == franquicia]['revenue'].sum()
        ganancia_promedio = df[df['belongs_to_collection'] == franquicia]['revenue'].mean()
        
        return {'franquicia': franquicia, 'cantidad': n_pelis, 'ganancia_total': round(ganancia_total, 0), 'ganancia_promedio': round(ganancia_promedio, 0)}

    # Interfaz de Streamlit
    st.title('3. Consulta de franquicias de películas')

    # Colecciones disponibles
    collection_names = df['belongs_to_collection'].unique()

    # Obtener la franquicia seleccionada por el usuario
    franquicia_seleccionada = st.selectbox('Seleccione una franquicia:', collection_names)

    # Llamar a la función franquicia y mostrar el resultado

    resultado = franquicia(franquicia_seleccionada)
    if resultado == 'Colección no encontrada':
        st.error('Colección no encontrada. Por favor, seleccione una franquicia válida.')
    else:
        st.write('Franquicia:', resultado['franquicia']) 
        st.write('Cantidad de películas:', resultado['cantidad'])
        st.write('Ganancia total:', resultado['ganancia_total'])
        st.write('Ganancia promedio:', resultado['ganancia_promedio'])


    #**********************************************************************#
    # 4.                     Películas por País                            #
    #**********************************************************************#

    # Obtiene la lista de países únicos de la columna "production_countries"

    df= pd.read_csv('./peliculas_etl.csv')
    # Crear un conjunto vacío para almacenar los países únicos
    unique_country = set()

    # Iterar sobre cada fila en la columna con listas
    for row in df['production_countries']:
        # Convertir los caracteres individuales en una lista de países
        countries = [c.lower() for c in eval(row)]
        # Actualizar el conjunto con los países únicos
        unique_country.update(set(countries))

    # Define la función para obtener la cantidad de películas producidas en un país
    def peliculas_pais(pais):
        pais_low = pais.lower()
        # Validar la entrada
        if pais_low in unique_country:
            # Crear una máscara booleana que sea Verdadera para las filas donde aparece pais en 'production_countries_name'
            mask = df['production_countries'].apply(lambda x: pais_low in [c.lower() for c in eval(x)])
            # Utilizar la máscara booleana para filtrar el dataframe
            n_films = df[mask]['title'].count()
            return {'pais': pais, 'cantidad': n_films}
        else:
            return 'País no válido'

    # Crea una interfaz de usuario en Streamlit
    st.title("4. Contador de películas por país")

    pais = st.selectbox("Selecciona un país:", list(unique_country))


    resultado = peliculas_pais(pais)

    if resultado == 'País no válido':
        st.write(resultado)
    else:
        st.write("En", resultado["pais"], "se han producido", resultado["cantidad"], "películas.")









    #**********************************************************************#
    #5.         Ganancia y cantidad de Películas por productora            #
    #**********************************************************************#

    # Función que retorna la ganancia total y la cantidad de peliculas de una productora.

    # Crear un conjunto vacío para almacenar las compañías únicas
    unique_company = set()

    # Iterar sobre cada fila en la columna con listas
    for row in df['production_companies']:
        # Convertir los caracteres individuales en una lista de compañías
        company = [c.lower() for c in eval(row)]
        # Actualizar el conjunto con las compañías únicas
        unique_company.update(set(company))

    # Convertir el conjunto nuevamente a una lista y establecer los nombres en minúsculas
    unique_company = [company.lower() for company in list(unique_company)]

    st.title('5. Consulta de productora')
    # Crear un SelectBox para seleccionar la productora
    selected_productora = st.selectbox('Selecciona una productora', unique_company, index=0)

    def productoras(productora):
        '''
        La función recibe como entrada el nombre de la productora y devuelve las ganancias totales y la cantidad de películas producidas por esa productora.
        '''
        productora_low = productora.lower()
        # Validar la entrada
        if productora_low in unique_company:
            # Crear una máscara booleana que es Verdadera para las filas donde productora aparece en 'production_companies_name'
            mask = df['production_companies'].apply(lambda x: productora_low in [p.lower() for p in eval(x)])
            # Usar la máscara booleana para filtrar el dataframe
            n_films = df[mask]['title'].count()
            total_revenue = df[mask]['revenue'].sum()
            return {'productora': productora, 'ganancia_total': total_revenue, 'cantidad': n_films}
        else:
            return 'Productora no válida'

    # Llamar a la función con la productora seleccionada
    result = productoras(selected_productora)

    # Interfaz de Streamlit

    # Mostrar el resultado
    if isinstance(result, str):
        st.write(result)
    else:
        st.write('Productora:', result['productora'])
        st.write('Ganancia total:', result['ganancia_total'])
        st.write('Cantidad de películas:', result['cantidad'])




    #**********************************************************************#
    #6.                Retorno de detalle de Películas                     #
    #**********************************************************************#

    def retorno(pelicula):
        '''
            Ingresas la pelicula, retornando la inversion, la ganancia, el retorno y el año en el que se lanzo.
        '''
        try:
            peli_low = pelicula.lower()
            indx = df[df['title'].apply(lambda x: x.lower()) == peli_low].index
            inversion = int(df.loc[indx,'budget'])
            ganancia = int(df.loc[indx,'revenue'])
            retorno = int(df.loc[indx,'return'])
            anio = int(df.loc[indx,'release_year'])
            return {'pelicula':pelicula, 'inversion':inversion, 'ganancia':ganancia, 'retorno':retorno, 'anio':anio}
        except:
            return 'Película no válida'

    # Interfaz de Streamlit
    st.title('6. Consulta informacion de películas')

    # Get the list of movie titles
    movie_titles = df['title'].tolist()

    # Create a SelectBox for selecting the movie
    selected_movie = st.selectbox('Selecciona una película', movie_titles)

    # Llamar a la función peliculas_dia y mostrar el resultado

    result = retorno(selected_movie)

    # Mostrar resultados
    if isinstance(result, str):
        st.write(result)
    else:
        st.write('Película:', result['pelicula'])
        st.write('Inversión:', result['inversion'])
        st.write('Ganancia:', result['ganancia'])
        st.write('Retorno:', result['retorno'])
        st.write('Año de lanzamiento:', result['anio'])

elif opcion == 'Sistema de recomendacion':
    st.title('SISTEMA DE RECOMENDACION DE PELICULAS')
    st.write('Esta es la opción Sistema de recomendacion')

    from PIL import Image

    # Cargar la imagen desde un archivo local
    image = Image.open('./top5.jpg')

        # Definir el ancho deseado de la imagen
    image_width = 3000

    # Redimensionar la imagen al ancho especificado
    image = image.resize((image_width, image.size[1]))

    # Mostrar la imagen en la aplicación Streamlit
    st.image(image, caption='Descripción de la imagen', use_column_width=True)

    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
    import pandas as pd

    df= pd.read_csv('./pelicula_etl.csv', sep=';')
    # Crear una instancia de TfidfVectorizer con stop words en inglés
    tfidf = TfidfVectorizer(stop_words='english')

    # Rellenar los valores faltantes en la columna 'overview' con una cadena vacía
    df['overview'] = df['overview'].fillna('')
    dff = df.sample(n=10000, random_state=42)

    # Aplicar la transformación TF-IDF a la columna 'overview'
    tfidf_matrix = tfidf.fit_transform(dff['overview'])

    # Calcular la similitud del coseno entre los documentos
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

    # Crear un diccionario de índices de películas basado en los títulos
    indices = pd.Series(dff.index, index=dff['title']).drop_duplicates()


    def get_recommendations1(title, cosine_sim=cosine_sim, top_n=5):
        # Obtener el índice de la película según el título ingresado
        idx = indices[title]

        # Obtener los puntajes de similitud de la película con todas las demás películas
        sim_scores = list(enumerate(cosine_sim[idx]))

        # Ordenar los puntajes de similitud en orden descendente
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        # Filtrar las películas similares para evitar recomendaciones duplicadas o poco relevantes
        sim_scores = [x for x in sim_scores if x[1] > 0.0][:top_n]

        # Obtener los índices de las películas recomendadas
        movie_indices = [i[0] for i in sim_scores]

        # Devolver los títulos de las películas recomendadas
        return dff['title'].iloc[movie_indices]


    # Crear una interfaz de usuario en Streamlit
    st.title("Recomendador de películas")

    # Componente de entrada de texto para el título de la película
    input_title = st.text_input("Ingresa el título de la película:")

    # Verificar si se ingresó un título de película
    if input_title:
        # Obtener las recomendaciones para el título de la película ingresado
        recommendations = get_recommendations1(input_title)

        # Mostrar las películas recomendadas
        if not recommendations.empty:
            st.write("Películas recomendadas:")
            for movie_title in recommendations:
                st.write("- " + movie_title)
        else:
            st.write("No se encontraron recomendaciones para la película ingresada.")