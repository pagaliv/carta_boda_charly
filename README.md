# Carta Boda Charly

QR que enlaza a la carta de la boda (PDF) publicada vía GitHub Pages.

## Cómo funciona

1. Sube el PDF a la raíz del repo con el nombre exacto `carta-boda-charly.pdf` (sin espacios ni acentos).
2. Activa GitHub Pages en el repo (Settings → Pages → Deploy from branch `main` / `root`).
3. El QR en `qr-codes/qr_carta_boda_charly.png` apunta a:
   `https://pagaliv.github.io/carta_boda_charly/carta-boda-charly.pdf`
4. `index.html` redirige automáticamente al PDF (útil como página de entrada).

## Regenerar el QR

```bash
python3 -m venv .venv
.venv/bin/pip install -r scripts/requirements.txt
.venv/bin/python scripts/generar_qr.py
```
