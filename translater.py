# Use a pipeline as a high-level helper
from transformers import pipeline

translater = pipeline("translation", model="Helsinki-NLP/opus-mt-en-ru")


translater ("I believe I can fly")
