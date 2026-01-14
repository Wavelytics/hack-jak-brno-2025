# hack-jak-brno-2025

Jednoduché demo, které:
- načítá video z webkamery přes OpenCV,
- detekuje obličej a jeho Face Mesh landmarky přes Google MediaPipe,
- vykresluje landmarky (zelené body) přímo do obrazu,
- zobrazuje živé okno s náhledem.

Soubor: `pywo_demo.py`

## Požadavky
- Python 3.9+ (doporučeno)
- Funkční webcam (integrovaná nebo USB)
- OS: Windows / macOS / Linux

## Instalace

### 1) Naklonuj repozitář
```bash
git clone git@github.com:Wavelytics/hack-jak-brno-2025.git
cd hack-jak-brno-2025
```

### 2) Nainstaluj závislosti
```bash
pip install -r requirements.txt
```

### 2) Spusť
```bash
python pywo_demo.py
```
