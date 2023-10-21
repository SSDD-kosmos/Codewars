def make_readable(seconds):
    return f'{(seconds // 3600):02d}:{((seconds % 3600) // 60):02d}:{(seconds % 60):02d}'


make_readable(86399)
