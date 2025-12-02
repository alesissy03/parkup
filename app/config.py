"""
Configurația aplicației.

TODO (Task 1):
- Citește config.json (db_url, default_zoom, default_center, etc.)
- Eventual citește și variabile din .env (SECRET_KEY, ENV, etc.)
- Expune o funcție load_config(env) care returnează un dict de configurare
"""

def load_config(env: str = "development") -> dict:
    """
    TODO (Task 1):
    - în funcție de `env`, construiește și întoarce un dict cu setările aplicației:
        - SQLALCHEMY_DATABASE_URI
        - SECRET_KEY
        - DEFAULT_ZOOM
        - DEFAULT_CENTER
        - alte opțiuni (DEBUG, TESTING, etc.)
    """
    config = {}

    # TODO (Task 1): încarcă valori din config.json
    # TODO (Task 1): setează SQLALCHEMY_DATABASE_URI (folosind db_url sau default SQLite)
    # TODO (Task 1): setează SECRET_KEY (temporar hardcodat sau din .env)
    # TODO (Task 1): setează alte opțiuni utile (ex: SQLALCHEMY_TRACK_MODIFICATIONS=False)

    return config
