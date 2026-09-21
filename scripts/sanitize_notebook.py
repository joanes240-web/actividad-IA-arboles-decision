from pathlib import Path
import sys
import nbformat


def sanitize(source: Path, target: Path) -> None:
    nb = nbformat.read(source, as_version=4)
    for cell in nb.cells:
        if cell.cell_type == "code":
            cell.outputs = []
            cell.execution_count = None
        # Evita metadatos de widgets/ejecución que pueden conservar valores.
        for key in ["execution", "collapsed", "scrolled"]:
            cell.metadata.pop(key, None)

    nb.metadata.pop("widgets", None)
    target.parent.mkdir(parents=True, exist_ok=True)
    nbformat.write(nb, target)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("Uso: python scripts/sanitize_notebook.py <origen.ipynb> <destino.ipynb>")
    source = Path(sys.argv[1])
    target = Path(sys.argv[2])
    sanitize(source, target)
    print(f"Notebook sanitizado: {target}")
    print("REVISIÓN MANUAL OBLIGATORIA: compruebe markdown, código, rutas, outputs embebidos y metadatos antes de publicar.")
