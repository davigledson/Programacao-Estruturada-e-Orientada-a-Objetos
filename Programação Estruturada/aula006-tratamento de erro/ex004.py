try:
    import arquivo
    print('fim')
except ModuleNotFoundError:
    print('arquivo não encontrado')