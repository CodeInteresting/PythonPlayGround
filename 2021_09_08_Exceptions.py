# Test exceptions

def example():
    try:
        int('N/A')
    except ValueError:
        raise RuntimeError('A parsing error occurred')


example()
