import json
from app.api.features.document_loaders import generate_summary_from_img, get_summary, summarize_transcript_youtube_url
from app.api.features.schemas.schemas import RequestSchema, SlidePresentationRequestArgs
from app.api.logger import setup_logger
from app.api.features.compile_chain_for_ppt import compile_chain
from app.api.features.generate_ppt import create_pptx_file, return_images

logger = setup_logger(__name__)

def full_workflow(topic, objective, target_audience, n_slides, slide_breakdown, lang, file_url, file_type):
  
    logger.info(f"File type uploaded successfully: {file_type}")
    logger.info("Generating the summary from the documents")

    if file_type == 'img':
        summary = generate_summary_from_img(file_url)
    elif file_type == 'youtube_url':
        summary = summarize_transcript_youtube_url(file_url)
    else:
        summary = get_summary(file_url, file_type)

    schema = RequestSchema(
        topic=topic,
        objective=objective,
        target_audience=target_audience,
        n_slides=n_slides,
        slide_breakdown=slide_breakdown,
        lang=lang,
        summary=summary
    )

    presentation = SlidePresentationRequestArgs(slide_schema=schema)

    logger.info(f"Summary generated successfully: {presentation.summary}")
    
    chain = compile_chain()
    
    logger.info("Generating the content for the PPT file")
    ppt_content = chain.invoke(presentation.validate_and_return())
    logger.info("PPT content generated successfully")

    create_pptx_file(ppt_content, return_images())
    return summary, json.dumps(ppt_content, indent=4)