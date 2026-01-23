import gradio as gr
import numpy as np
import cv2

# # 案例1：功能实现
# def reverse_text(text):
#     return text[::-1]
#
#
# # 界面配置
# demo = gr.Interface(
#     fn=reverse_text,
#     inputs='text',
#     outputs='text'
# )
#
# # 启动应用
# demo.launch()

# # 案例2：功能实现
# def hellotoPerson(name):
#     return "你好，" + name
#
#
# # 界面配置
# demo = gr.Interface(
#     fn=hellotoPerson,
#     inputs='text',
#     outputs='text'
# )
#
# # 启动应用
# demo.launch()

# # 案例3：功能实现
# def reverse_and_count(text):
#     reverse_text = text[::-1]
#     length = len(reverse_text)
#     return reverse_text, length
#
#
# demo = gr.Interface(
#     fn=reverse_and_count,
#     inputs='text',
#     outputs=['text', 'number'],
#     title='文本处理工具',
#     description='输入一段文字，查看其倒序形式及字符串',
#     examples=[['你好，世界'], ['hello,world']]
# )
#
# demo.launch()


# 案例4：功能实现
def image_to_sketch(image):
    gray_image = image.convert('L')
    inverted_image = 255 - np.array(gray_image)
    blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
    inverted_blurred = 255 - blurred
    pencil_sketch = cv2.divide(np.array(gray_image), inverted_blurred, scale=256.0)
    return pencil_sketch


# 界面配置
demo = gr.Interface(
    fn=image_to_sketch,
    inputs=[gr.Image(label='上传图片', type='pil')],
    outputs=[gr.Image(label='铅笔画')],
    title='图像转铅笔画',
    description='请上传图片转为铅笔画'
)

# 启动应用
demo.launch()


