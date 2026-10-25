import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

def setup_logging():
    # Carpeta donde se guardarán los archivos de logs
    log_dir = Path(__file__).resolve().parents[2] / "logs"
    log_dir.mkdir(exist_ok=True)

    logger = logging.getLogger("smart_travel")
    logger.setLevel(logging.DEBUG)
    logger.propagate = False

    # Evitar añadir manejadores duplicados
    if logger.handlers:
        return logger

    # Formato común para todos los logs
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Mostrar mensajes en la terminal
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    # Guardar mensajes en un archivo
    file_handler = RotatingFileHandler(
        log_dir / "app.log",
        maxBytes=5_000_000,
        backupCount=3,
        encoding="utf-8"
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger