from app.api.features.compile_chain_for_ppt import compile_chain
from app.api.features.generate_ppt import create_pptx_file, return_images
from app.api.features.document_loaders import generate_summary_from_img, get_summary, summarize_transcript_youtube_url
from fastapi import APIRouter, Depends
from app.api.logger import setup_logger
from app.api.features.schemas.schemas import RequestSchemaWithFiles, SlidePresentationRequestArgs
from app.api.auth.auth import key_check

logger = setup_logger(__name__)
router = APIRouter()

@router.get("/")
def read_root():
    return {"Hello": "World"}

@router.post("/generate-ppt")
async def submit_tool( data: RequestSchemaWithFiles, _ = Depends(key_check)):

    logger.info(f"File type uploaded successfully: {data.file_type}")

    args = SlidePresentationRequestArgs(slide_schema=data.request_args)

    logger.info("Generating the summary from the documents")

    if data.file_type == 'img':
        summary = generate_summary_from_img(data.file_url)
    elif data.file_type == 'youtube_url':
        summary = summarize_transcript_youtube_url(data.file_url)
    else:
        summary = get_summary(data.file_url, data.file_type)

    chain = compile_chain()

    args.summary = summary

    logger.info(f"Summary generated successfully: {args.summary}")

    logger.info("Generating the content for the PPT file")
    ppt_content = chain.invoke(args.validate_and_return())
    logger.info("PPT content generated successfully")

    create_pptx_file(ppt_content, return_images()) 

    return ppt_content