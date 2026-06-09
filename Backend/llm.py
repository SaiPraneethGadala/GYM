from transformers import AutoTokenizer
from transformers import AutoModelForSeq2SeqLM
import streamlit as st


@st.cache_resource
def load_model():

    model_name = "google/flan-t5-base"

    tokenizer = AutoTokenizer.from_pretrained(
        model_name
    )

    model = AutoModelForSeq2SeqLM.from_pretrained(
        model_name
    )

    return tokenizer, model


tokenizer, model = load_model()


def generate_response(prompt):

    try:

        inputs = tokenizer(
            prompt,
            return_tensors="pt",
            truncation=True,
            max_length=512
        )

        outputs = model.generate(
            **inputs,
            max_new_tokens=150,
            do_sample=False
        )

        response = tokenizer.decode(
            outputs[0],
            skip_special_tokens=True
        )

        return response

    except Exception as e:
        return f"Error: {str(e)}"