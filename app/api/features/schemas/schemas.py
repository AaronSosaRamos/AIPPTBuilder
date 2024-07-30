from pydantic import BaseModel, Field, validator
from typing import List, Optional

class SlideSchema(BaseModel):
    title: str = Field(..., title="Title", description="The title of the Slide.")
    content: str = Field(..., title="Content", description="The content of the slide.")

    model_config = {
        "json_schema_extra": {
            "examples": """
                "title": "Introduction",
                "content": "This slide introduces the main topics of the presentation.",
                """
        }
    }


class PPTFileSchema(BaseModel):
    title: str = Field(..., title="Title", description="The title of the PowerPoint presentation.")
    description: str = Field(..., title="Description", description="A brief description of the PowerPoint presentation.")
    slides: List[SlideSchema] = Field(..., title="Slides", description="A list of slides in the PowerPoint presentation.")

    model_config = {
      "json_schema_extra": {
          "examples": """
              "title": "Project Presentation",
              "description": "A detailed presentation of the project including objectives, methodology, and results.",
              "slides": [
                  {
                      "title": "Introduction",
                      "content": "This slide introduces the main topics of the presentation."
                  },
                  {
                      "title": "Methodology",
                      "content": "This slide explains the methodology used in the project."
                  },
                  {
                      "title": "Results",
                      "content": "This slide presents the results of the project."
                  }
              ] """
          }
      }
    
    
class RequestSchema(BaseModel):
    topic: str = Field(..., min_length=1, max_length=100, description="The topic of the slide presentation")
    objective: str = Field(..., min_length=1, max_length=200, description="The objective of the slide presentation")
    target_audience: str = Field(..., min_length=1, max_length=100, description="The target audience of the slide presentation")
    n_slides: int = Field(..., ge=1, le=100, description="The number of slides in the presentation")
    slide_breakdown: str = Field(..., description="A breakdown of the content for each slide")
    lang: str = Field(..., min_length=2, max_length=2, pattern='^[a-zA-Z]{2}$', description="Language code for the presentation")
    summary: Optional[str] = ""

    @validator('lang')
    def validate_language(cls, v):
        if v.lower() not in ['en', 'es', 'fr', 'de', 'it', 'pt']:
            raise ValueError('Invalid language code')
        return v

    @validator('slide_breakdown')
    def validate_slide_breakdown(cls, v):
        if not v:
            raise ValueError('Slide breakdown cannot be empty')
        return v

class SlidePresentationRequestArgs:
    def __init__(self, slide_schema: RequestSchema):
        self._slide_schema = slide_schema

    @property
    def topic(self) -> str:
        return self._slide_schema.topic

    @topic.setter
    def topic(self, value: str):
        self._slide_schema.topic = value

    @property
    def objective(self) -> str:
        return self._slide_schema.objective

    @objective.setter
    def objective(self, value: str):
        self._slide_schema.objective = value

    @property
    def target_audience(self) -> str:
        return self._slide_schema.target_audience

    @target_audience.setter
    def target_audience(self, value: str):
        self._slide_schema.target_audience = value

    @property
    def n_slides(self) -> int:
        return self._slide_schema.n_slides

    @n_slides.setter
    def n_slides(self, value: int):
        self._slide_schema.n_slides = value

    @property
    def slide_breakdown(self) -> str:
        return self._slide_schema.slide_breakdown

    @slide_breakdown.setter
    def slide_breakdown(self, value: str):
        self._slide_schema.slide_breakdown = value

    @property
    def lang(self) -> str:
        return self._slide_schema.lang

    @lang.setter
    def lang(self, value: str):
        self._slide_schema.lang = value

    @property
    def summary(self) -> str:
        return self._slide_schema.summary

    @summary.setter
    def summary(self, value: str):
        self._slide_schema.summary = value

    def validate_and_return(self) -> dict:
        # Validate the SlideSchema and return the values as a dictionary
        return self._slide_schema.dict()
    
class RequestSchemaWithFiles(BaseModel):
    request_args: RequestSchema
    file_url: str
    file_type: str