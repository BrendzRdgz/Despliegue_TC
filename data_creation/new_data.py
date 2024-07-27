import pandas as pd
import numpy as np
import os

# Configurar el número de nuevas muestras
num_new_samples = 100

# Generar nuevos datos sintéticos
np.random.seed(43)  # Cambiar la semilla para obtener nuevos datos
new_followers = np.random.lognormal(mean=10, sigma=1, size=num_new_samples).astype(int)
new_average_views = (new_followers * np.random.uniform(0.1, 0.5, size=num_new_samples)).astype(int)
new_average_interactions = (new_average_views * np.random.uniform(0.1, 0.3, size=num_new_samples)).astype(int)
new_posting_frequency = np.random.randint(1, 30, size=num_new_samples)
#content_types = ['Gaming', 'Lifestyle', 'Education']
#new_content_type = np.random.choice(content_types, size=num_new_samples)

# Supongamos una fórmula para calcular los ingresos basada en estas características
base_income = 500  # Base de ingresos fija para todos los influencers
income_per_follower = 0.01  # Ingresos por cada seguidor
income_per_view = 0.05  # Ingresos por cada visualización
income_per_interaction = 0.1  # Ingresos por cada interacción
bonus_per_post = 100  # Ingresos adicionales por frecuencia de publicación
#bonus_per_content_type = {'Gaming': 2000, 'Lifestyle': 2500, 'Education': 3000}  # Bonificación según el tipo de contenido

new_revenue = (base_income +
               income_per_follower * new_followers +
               income_per_view * new_average_views +
               income_per_interaction * new_average_interactions +
               bonus_per_post * new_posting_frequency).astype(int)

# Crear un DataFrame con los nuevos datos
new_data = {
    'followers': new_followers,
    'average_views': new_average_views,
    'average_interactions': new_average_interactions,
    'posting_frequency': new_posting_frequency,
    #'content_type': new_content_type,
    'revenue': new_revenue
}
new_df = pd.DataFrame(new_data)

# Construir la ruta del archivo existente
base_dir = os.path.dirname(os.path.abspath(__file__))
existing_file_path = os.path.join(base_dir, '../data/revenue.csv')

# Leer el CSV existente
existing_df = pd.read_csv(existing_file_path)

# Combinar el DataFrame existente con el nuevo DataFrame
combined_df = pd.concat([existing_df, new_df], ignore_index=True)

# Construir la ruta para guardar el archivo combinado
updated_file_path = os.path.join(base_dir, '../data/revenue_updated.csv')

# Guardar el DataFrame combinado en un nuevo archivo CSV o sobrescribir el existente
combined_df.to_csv(updated_file_path, index=False)

# Mostrar las primeras filas del DataFrame combinado para verificar los datos
print(combined_df.head())
print(f"Total number of samples: {len(combined_df)}")