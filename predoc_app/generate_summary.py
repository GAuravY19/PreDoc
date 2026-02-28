import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

class SummaryPipeLine():
    def __init__(self):
        load_dotenv()

        os.environ['GOOGLE_API_KEY'] = os.getenv('GOOGLE_GEMINI_API_KEY')

        self.model = ChatGoogleGenerativeAI(
            model = 'models/gemini-2.5-flash',
            temperature = 0.3
        )

        self.template = PromptTemplate(
            input_variables=['text'],
            template="""
            You're a medical assistant.
            Summarize the following patient reported symptoms into a concise clinical note without having subsections.

            Patient Input:
            {text}

            Return a structured Summary.

            Note :- The answer should not have markdown text. It should be in plain text format.
            """
        )


    def summarize(self, patient_details:dict):
        content = "\n".join(
            f"{q} -> {a}" for q,a in patient_details.items()
        )

        # doc = Document(
        #     page_content = content,
        #     metadata = {"source", "patient form"}
        # )

        final_prompt = self.template.format(text=content)

        response = self.model.invoke(final_prompt)

        return response.content


