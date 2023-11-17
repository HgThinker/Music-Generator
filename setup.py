import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    # long_description=long_description,
    name="Music-Generator",
    packages=setuptools.find_packages(),
    install_requires = [
        'num2words',
        'numpy',
        'sentencepiece',
        'spacy==3.5.2',
        'torch>=2.0.0',
        'torchaudio>=2.0.0',
        'huggingface_hub',
        'tqdm',
        'transformers>=4.31.0',  # need Encodec there.
        'librosa',
        'gradio',
        'torchmetrics',
        'encodec',
        'datasets',
        'yt-dlp',
        'ffmpeg',
    ]
)