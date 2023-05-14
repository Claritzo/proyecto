from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title='Proyecto 1 de Henry',
              description= 'Estamos realizando un proyecto de Películas para la cursada del primer modulo',
              version='1.0.1')


@app.get("/mes/{mes}")
async def peliculas_mes(mes: str):
    '''
        Se ingresa el mes y la funcion retorna la cantidad de peliculas que se estrenaron ese mes
    '''
    mes = mes.capitalize()
    cantidad = movies.loc[movies['release_month'] == mes, 'title'].count()
    return {'Mes':mes, 'Cantidad de Peliculas':cantidad}

@app.get("/dia/{dia}")
async def peliculas_dia(dia: str):
    '''
        Se ingresa el dia y la funcion retorna la cantidad de peliculas que se estrenaron ese dia
    '''
    dia = dia.capitalize()
    cantidad = movies.loc[movies['release_day'] == dia, 'title'].count()
    return {'Día':dia, 'Cantidad de Peliculas':cantidad}
    
    
@app.get("/franquicia/{franquicia}")
async def peliculas_franquicia(franquicia: str):
    '''
        Se ingresa la franquicia, retornando la cantidad de peliculas, ganancia total y promedio
    '''
    peliculas = (movies[movies['belongs_to_collection'] == franquicia]) 
    cantidad = peliculas.shape[0]
    ganancia_total = peliculas['revenue'].sum()
    ganancia_promedio = peliculas['revenue'].mean()
    return {'Franquicia': franquicia, 'cantidad':cantidad, 'ganancia_total':ganancia_total, 'Ganancia_Promedio':ganancia_promedio}


@app.get("/pais/{pais}")
async def peliculas_pais(pais: str):
    '''
        Ingresas el pais, retornando la cantidad de peliculas producidas en el mismo
    '''
    pais = pais.lower()
    cantidad = movies[movies['production_countries'].apply(lambda x:pais in [p.lower() for p in x])]['title'].count()
    return {'País': pais, 'Cantidad de Peliculas': cantidad}
    
    
'''
@app.get("/productora/{productora}")

    '''
        Ingresas la productora, retornando la ganancia total y la cantidad de peliculas que produjeron
    '''
    unique_company = set()

# itera sobre cada fila en la columna de las compañias
    for row in movies['production_companies']:
        unique_company.update(set(row))

    # convierte nuevamente el conjunto en una lista
    unique_company = [company.lower() for company in list(unique_company)]

async def peliculas_productora(productora: str):
        productora_low = productora.lower()
        if productora_low in unique_company:
            # crear mascara
            peli = movies['production_companies'].apply(lambda x: productora_low in [p.lower() for p in x])
            # se usa la mascara para filtrar el datasets
            cantidad = movies[peli]['title'].count()
            ganancia = movies[peli]['revenue'].sum()
            return {'Productora':productora, 'Ganancia_total':ganancia, 'Cantidad':cantidad}
        else:
            return 'Productora no válida'
'''
@app.get("/retorno/{pelicula}")
async def retorno(pelicula: str):
    '''
        Ingresas la pelicula, retornando la inversion, la ganancia, el retorno y el año en el que se lanzo
    '''
    mv = movies[movies['title'] == pelicula]
    inversion = mv['budget'].sum()
    ganancia = mv['revenue'].sum()-mv['budget'].sum()
    retorno = mv['return'].sum()
    anio = mv['release_year'].sum()
    
    return {'pelicula':pelicula, 'inversion':inversion, 'ganacia':ganancia,'retorno':retorno, 'año':anio}

