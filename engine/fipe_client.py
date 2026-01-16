import httpx
# biblioteca moderna para fazer requisições web ,usamos porque ela suporta `async`

BASE_URL = "https://fipe.parallelum.com.br/api/v2"


def get_brands(vehicle_type: str):
    """Busca todas as marcas de um tipo de veículo"""
    # Usando httpx.Client() em vez de AsyncClient()
    with httpx.Client() as client:
        try:
            response = client.get(f"{BASE_URL}/{vehicle_type}/brands")
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            return {"error": f"Erro HTTP: {e.response.status_code}", "message": e.response.text}
        except Exception as e:
            return {"error": f"Ocorreu um erro: {e}"}

def get_models(vehicle_type: str, brand_id: int):
    """Busca os modelos de uma marca específica."""
    with httpx.Client() as client:
        try:
            url = f"{BASE_URL}/{vehicle_type}/brands/{brand_id}/models"
            response = client.get(url)
            response.raise_for_status()

            data = response.json()
            
            if isinstance(data, dict):
                return data.get("models", [])
            elif isinstance(data, list):
                return data
            else:
                return []
            
        except httpx.HTTPStatusError as e:
            return {"error": f"Erro HTTP: {e.response.status_code}", "message": e.response.text}
        except Exception as e:
            return {"error": f"Ocorreu um erro: {e}"}

def get_years(vehicle_type: str, brand_id: int, model_id: int):
    """Busca os anos de um modelo específico."""
    with httpx.Client() as client:
        try:
            url = f"{BASE_URL}/{vehicle_type}/brands/{brand_id}/models/{model_id}/years"
            response = client.get(url)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            return {"error": f"Erro HTTP: {e.response.status_code}", "message": e.response.text}
        except Exception as e:
            return {"error": f"Ocorreu um erro: {e}"}

def get_price(vehicle_type: str, brand_id: int, model_id: int, year_id: str):
    """Busca o preço final de um veículo específico."""
    with httpx.Client() as client:
        try:
            url = f"{BASE_URL}/{vehicle_type}/brands/{brand_id}/models/{model_id}/years/{year_id}"
            response = client.get(url)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            return {"error": f"Erro HTTP: {e.response.status_code}", "message": e.response.text}
        except Exception as e:
            return {"error": f"Ocorreu um erro: {e}"}