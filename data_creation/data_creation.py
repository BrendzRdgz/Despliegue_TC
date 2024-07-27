import pandas as pd
import numpy as np

# Configurar el número de muestras
num_samples = 200

# Generar datos sintéticos más realistas
np.random.seed(42)
followers = np.random.lognormal(mean=10, sigma=1, size=num_samples).astype(int)
average_views = (followers * np.random.uniform(0.1, 0.5, size=num_samples)).astype(int)
average_interactions = (average_views * np.random.uniform(0.1, 0.3, size=num_samples)).astype(int)
posting_frequency = np.random.randint(1, 30, size=num_samples)
#content_types = ['Gaming', 'Lifestyle', 'Education']
#content_type = np.random.choice(content_types, size=num_samples)

# Supongamos una fórmula para calcular los ingresos basada en estas características
base_income = 500  # Base de ingresos fija para todos los influencers
income_per_follower = 0.01  # Ingresos por cada seguidor
income_per_view = 0.05  # Ingresos por cada visualización
income_per_interaction = 0.1  # Ingresos por cada interacción
bonus_per_post = 100  # Ingresos adicionales por frecuencia de publicación
#bonus_per_content_type = {'Gaming': 2000, 'Lifestyle': 2500, 'Education': 3000}  # Bonificación según el tipo de contenido

revenue = (base_income +
           income_per_follower * followers +
           income_per_view * average_views +
           income_per_interaction * average_interactions +
           bonus_per_post * posting_frequency).astype(int)
            

# Crear un DataFrame
data = {
    'followers': followers,
    'average_views': average_views,
    'average_interactions': average_interactions,
    'posting_frequency': posting_frequency,
    #'content_type': content_type,
    'revenue': revenue
}
df = pd.DataFrame(data)

# Guardar el DataFrame en un archivo CSV
df.to_csv('revenue.csv', index=False)

# Mostrar las primeras filas del DataFrame para verificar los datos
print(df.head())
