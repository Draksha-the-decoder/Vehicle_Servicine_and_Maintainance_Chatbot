from flask import Flask, render_template, request
from transformers import AutoModelForCausalLM, AutoTokenizer,BitsAndBytesConfig,pipeline
import torch
app = Flask(__name__)

quant_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=getattr(torch, "float16"),
    bnb_4bit_use_double_quant=False
)
model_dir = "/llama-2-7b-chat-vehicle"
fine_tuned_model = AutoModelForCausalLM.from_pretrained(
    model_dir, quantization_config=quant_config,
    device_map={"": 0}
    )
fine_tuned_tokenizer = AutoTokenizer.from_pretrained(model_dir)
pipe = pipeline(task="text-generation", model=fine_tuned_model, tokenizer=fine_tuned_tokenizer, max_length=300)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')   
    result = pipe(f"<s>[INST] {userText} [/INST]")
    return str(result[0]['generated_text'])

if __name__ == "__main__":
    app.run(debug=True)