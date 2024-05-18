import requests
import json
import gradio as gr

url="http://localhost:11434/api/generate"

headers={

    'Content-Type':'application/json'
}


def generate_response(prompt):

    data={
        "model":"SSCodeGT",
        "prompt":prompt,
        "stream":False
    }

    response=requests.post(url,headers=headers,data=json.dumps(data))

    if response.status_code==200:
        response=response.text
        data=json.loads(response)
        actual_response=data['response']
        return actual_response
    else:
        print("error:",response.text)


interface=gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(lines=4,placeholder="Enter your Prompt"),
    outputs="text"
)
interface.launch(share=True)

# to store the history of the prompt make a list history and in function generate_response write 
# history.append(prompt)
# final_prompt="\n".join(history)
# in data {prompt = final_prompt}