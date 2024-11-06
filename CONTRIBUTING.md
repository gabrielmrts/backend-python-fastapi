# Guia de Code Style
Este guia define as convenções de estilo de código que devem ser seguidas neste projeto Python. O objetivo é garantir que todo o código seja legível, consistente e fácil de manter.

1. Comprimento Máximo de Linha:
O comprimento máximo de linha deve ser de 88 caracteres.
Evite linhas longas sempre que possível, quebrando-as de forma legível.
2. Estilo de Docstrings:
Usamos o padrão de docstrings sugerido pelo plugin flake8-docstrings.

Ignoramos os seguintes erros de docstrings:

- D401: Exigência de que as docstrings sejam escritas no estilo imperativo.
- D400: Exigência de que as docstrings terminem com um ponto final.
- D100: Exigência de docstrings em definições de módulo.
- Apesar disso, é fortemente recomendado que todas as funções e classes tenham docstrings explicativas, seguindo o formato Google.

3. Anotações de Tipos
Anotações de tipos são obrigatórias para todas as funções e métodos.

* Usamos o plugin flake8-annotations para garantir que todas as funções estejam devidamente anotadas com tipos.
Sempre use as anotações de tipos apropriadas, como Optional, List, e Dict quando necessário.

4. Código Limpo e Otimizado
* Usamos o plugin flake8-bugbear para detectar padrões comuns de código que podem levar a bugs.
Preste atenção a warnings do Bugbear e refatore o código para eliminar riscos potenciais.

5. Nomes de Variáveis
* Evite o uso de nomes de variáveis conflitantes com palavras reservadas do Python, como list, dict, etc.
O Flake8 está configurado para identificar os seguintes conflitos:
A001 a A006: Nomes de variáveis que coincidem com palavras reservadas devem ser evitados.

6. Seleção de Erros
* As verificações do Flake8 incluem uma série de categorias de erros (C, E, F, W, B, ANN, D, N), garantindo que o código siga boas práticas e evite erros comuns.
Devemos prestar atenção às seguintes categorias selecionadas:
C, E, F, W: Convenções de código, erros, falhas e warnings gerais.
B: Checagens de Bugs com o Flake8 Bugbear.
ANN: Verificações de anotações de tipos.
D: Docstrings, com as exceções mencionadas.
N: Verificações de boas práticas de nomenclatura.

7. Exclusões
* Arquivos __init__.py são excluídos da verificação do Flake8.

8. Versão do Python
* Este projeto utiliza Python 3.11. Certifique-se de usar essa versão para compatibilidade e novas funcionalidades de linguagem.

Exemplo de Anotações de Tipo e Docstrings (Google Style):
````python
def add_numbers(a: int, b: int) -> int:
    """
    Soma dois números inteiros.

    Args:
        a (int): O primeiro número.
        b (int): O segundo número.

    Returns:
        int: A soma de `a` e `b`.
    """
    return a + b
````