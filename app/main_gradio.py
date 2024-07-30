from app.api.features.full_workflow_for_gradio import full_workflow
import gradio as gr

demo = gr.Interface(fn=full_workflow,
                    inputs=[gr.Textbox(label="Topic: "),
                            gr.TextArea(label="Objective: "),
                            gr.Textbox(label="Target Audience: "),
                            gr.Number(label="Number of slides: "),
                            gr.TextArea(label="Slide breakdown: "),
                            gr.Dropdown(["en", "es", "fr", "de", "it", "pt"], label="Language: "),
                            gr.Textbox(label="File URL:"),
                            gr.Dropdown(["pdf", "csv", "txt", "md", "url", "pptx", "docx", "xls", "xlsx", "xml", "gdoc", "gsheet", "gslide", "gpdf", "youtube_url", "img"], label="File Type: "),
                            ], outputs=[gr.TextArea(label="Summary: "), gr.TextArea(label="PPT Result: ")])

demo.launch(share=True, debug=True)