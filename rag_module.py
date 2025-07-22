
from llama_cpp import Llama
import os

def generate_report(findings, patient_context, templates):
    prompt = (
        "[INST] <<SYS>>\n"
        "You are a radiology assistant. Write a complete, professional chest X-ray report in the following format:\n\n"
        "Chest X-Ray Report\n\n"
        "Patient Information:\n"
        f"- Age: {patient_context['age']}\n"
        f"- Sex: {patient_context['sex']}\n"
        f"- Symptoms: {patient_context['symptoms'] or 'None reported'}\n"
        f"- History: {patient_context['history'] or 'None reported'}\n\n"
        "Findings:\n"
        f"{findings}\n\n"
        "Impression:\n"
        "Relevant Negatives:\n"
        "Suggested Next Steps:\n"
        "Conclusion:\n"
        "<</SYS>>\n"
        "[/INST]"
    )
    print("LLM prompt:\n", prompt)
    model_path = os.getenv('LLAMA_MODEL_PATH', 'models/llama-2-7b-chat.Q4_K_M.gguf')
    llm = Llama(model_path=model_path, n_ctx=2048)
    output = llm(prompt, max_tokens=526)
    print("LLM raw output:", output)
    return output['choices'][0]['text'].strip()