import os
from pathlib import Path
from dotenv import load_dotenv
from zeep import Client


load_dotenv()

LHI_FILES_DIR = Path(__file__).parent.resolve() / 'lhi-files'

# This is an example HotDocs answer file that LHI gave us.
XML_FILE = LHI_FILES_DIR / 'cf92740b-ed6d-4019-b358-9293e14780d9-07-03-2018.xml'

# This API endpoint appears to be a SOAP endpoint that exposes
# its interface via the Web Service Description Language (WSDL).
API_ENDPOINT = 'https://lhiutilitystage.lawhelpinteractive.org/LHIIntegration/LHIIntegration.svc'

# Customer key
# ------------
# This parameter is required. This is the id to the specific system
# Implementation linking to LHI. Each new partner wishing to integrate
# with LHI will be assigned an ID.
CUSTOMER_KEY = os.environ['LHI_CUSTOMER_KEY']

# Template ID
# -----------
# This parameter is required, which will be used as to recognise the
# template for which document and answers generates.

# AV: I'm unclear on whether this should just be "5396" or the whole URL.
# Update 10/31/2018: It looks like the endpoint now raises a fault if
# we provide the ID as a URL, so I guess it's a number we're supposed to provide.
# A number as a string, that is.
TEMPLATE_ID = "5395"
TEMPLATE_URL = f"https://rebuildqa.lawhelpinteractive.org/Interview/InterviewHome?templateId={TEMPLATE_ID}"

# HD Info
# -------
# This parameter is required. This is an XML answer set conforming to the
# HotDocs answer file format. This XML data should contain all of the CMS
# case data intended to be prepopulated into the requested interview. The
# field names must conform to the field names in the selected template in
# order for mapping to occur. At a minimum the string "<AnswerSet/>"
# must be provided.
HD_INFO = XML_FILE.read_text()

# Doc ID
# ------
# This parameter is required. This is to identify what case and document
# instance is associated with the incoming data.

# AV: I'm unclear on where this value is supposed to come from; is it
# only useful for book-keeping on our end, or does it mean something to
# LHI?
DOC_ID = "uhhhhm"

# Postback URL
# ------------
# This is the URL of the postback service provided by JustFix.nyc. LHI
# will call this to return the data.
POSTBACK_URL = os.environ['LHI_POSTBACK_URL']

if __name__ == '__main__':
    client = Client(f"{API_ENDPOINT}?wsdl")

    print(f"Calling GetAnswersAndDocuments() with PostBackUrl={POSTBACK_URL}.")

    result = client.service.GetAnswersAndDocuments(
        CustomerKey=CUSTOMER_KEY,
        TemplateId=TEMPLATE_ID,
        HDInfo=HD_INFO,
        DocID=DOC_ID,
        PostBackUrl=POSTBACK_URL
    )

    print(f"Done! The response is: {result}")
