import os

def renomear_pastas_inicio(pasta_alvo_dir):
    import locale
    locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
    import datetime

    if os.path.exists(f"{pasta_alvo_dir}\\ENTRADA\\12-DEZ"):
        
        pastas = ["ENTRADA", "SAÍDA"]

        for pasta in pastas:
            for i in range(1, 13):
                if i < 10:
                    os.rename(f"{pasta_alvo_dir}\\{pasta}\\0{i}-{((datetime.date(2024, i, 1)).strftime('%b')).upper()}", f"{pasta_alvo_dir}\\{pasta}\\0{i}")
                else:
                    os.rename(f"{pasta_alvo_dir}\\{pasta}\\{i}-{((datetime.date(2024, i, 1)).strftime('%b')).upper()}", f"{pasta_alvo_dir}\\{pasta}\\{i}")
    else:
        pass

def renomear_pastas_fim(pasta_alvo_dir):
    import locale
    locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
    import datetime

    if os.path.exists(f"{pasta_alvo_dir}\\ENTRADA\\12"):

        pastas = ["ENTRADA", "SAÍDA"]

        for pasta in pastas:
            for i in range(1, 13):
                if i < 10:
                    os.rename(f"{pasta_alvo_dir}\\{pasta}\\0{i}", f"{pasta_alvo_dir}\\{pasta}\\0{i}-{((datetime.date(2024, i, 1)).strftime('%b')).upper()}")
                else:
                    os.rename(f"{pasta_alvo_dir}\\{pasta}\\{i}", f"{pasta_alvo_dir}\\{pasta}\\{i}-{((datetime.date(2024, i, 1)).strftime('%b')).upper()}")
