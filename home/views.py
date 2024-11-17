from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .download_script import download_media
import os
import json
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_protect
import logging
import subprocess
import shutil

# Configurar o logging
logger = logging.getLogger(__name__)

class IndexView(TemplateView):
    template_name = 'modelo.html'

class appView(TemplateView):
    template_name = 'index.html'

@csrf_protect
def download_video(request):
    if request.method == 'POST':
        try:
            # Tenta decodificar os dados da requisição
            data = json.loads(request.body)
            logger.debug(f"Dados JSON decodificados: {data}")
            
            url = data.get('url')
            format_choice = data.get('format', 'mp4').lower()
            output_folder = data.get('output_folder')

            # Validação de tipo para garantir que 'url' e 'output_folder' são strings
            if not isinstance(url, str) or not isinstance(output_folder, str):
                return JsonResponse({'status': 'error', 'message': 'Parâmetros inválidos.'}, status=400)

            # Validação da URL e do diretório de destino
            if not url or not output_folder:
                return JsonResponse({'status': 'error', 'message': 'Faltando parâmetros necessários.'}, status=400)

            if not os.path.isdir(os.path.dirname(output_folder)):
                return JsonResponse({'status': 'error', 'message': 'Pasta de destino inválida.'}, status=400)

            # Define o caminho base para o download
            base_download_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'media', 'downloads')
            os.makedirs(base_download_path, exist_ok=True)
            output_folder = os.path.join(base_download_path, output_folder)

            # Inicia o download
            download_media(url, output_folder, format_choice)
            return JsonResponse({'status': 'success', 'message': 'Download iniciado.'})

        except json.JSONDecodeError as e:
            logger.error(f"Erro ao processar o JSON: {e}")
            return JsonResponse({'status': 'error', 'message': 'Erro ao processar dados da requisição.'}, status=400)
        
        except subprocess.CalledProcessError as e:
            logger.error(f"Erro no processo de download: {e}")
            return JsonResponse({'status': 'error', 'message': f"Erro ao executar o download: {e}"}, status=500)

        except FileNotFoundError as e:
            logger.error(f"Erro ao encontrar o arquivo: {e}")
            return JsonResponse({'status': 'error', 'message': 'Erro ao localizar o arquivo. Verifique se todas as dependências estão instaladas.'}, status=500)

        except Exception as e:
            logger.error(f"Erro inesperado: {e}")
            return JsonResponse({'status': 'error', 'message': f"Erro inesperado: {str(e)}"}, status=500)

    else:
        return JsonResponse({'status': 'error', 'message': 'Método não permitido.'}, status=405)
