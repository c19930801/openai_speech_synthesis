from pathlib import Path
from openai import OpenAI

def generate_speech(api_key,text,model,voice,file_path):
    client=OpenAI(api_key=api_key)
    response = client.audio.speech.create(
        model=model,
        voice=voice,
        input=text
    )
    path_obj = Path(file_path)
    with open(path_obj, 'wb') as file:
        file.write(response.content)
    return f'save to: {path_obj}'

api_key="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"
model='tts-1-hd'
voice="nova"
file_path=r"openai.mp3"

text="注意看這個男人太狠了!這個男人叫做小忠哥,搞遍樹德無敵手,後人稱呼為小忠搞哥"

print(generate_speech(api_key,text,model,voice,file_path))
