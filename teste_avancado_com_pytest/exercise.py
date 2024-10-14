def str_to_bool(value):
    """
    Converte uma string em um valor booleano.
    A função str_to_bool segue a mesma ideia de transformação de strings para booleanos, lidando com exceções e com entradas não esperadas.
    """

    try:
        value = value.lower()
    except AttributeError:
        raise AttributeError(f'{value} deve ser uma string')

    true_values = ['y', 'yes', '1']
    false_values = ['n', 'no', '0']

    if value in true_values:
        return True
    elif value in false_values:
        return False
    else:
        raise ValueError(f'{value} não é um valor booleano válido')
