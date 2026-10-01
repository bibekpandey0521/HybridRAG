from fastapi import FastAPI,UploadFile,File,HTTPException
import pymupdf4llm
import fitz
import os

app = FastAPI()

latest_pdf_path = None

@app.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):
    """Upload and save PDF"""

    global latest_pdf_path

    # Check file type
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code= 400,
            detail = "Only PDF files are allowed"
        )
    # Create uploads folder 
    upload_folder = "uploads"

    os.makedirs(
        upload_folder,
        exist_ok=True
    )

    # Create PDF Path 
    file_path = os.path.join(upload_folder,file.filename)

    # Read uploaded PDF
    file_data = await file.read()

    # Save PDF
    with open(file_path,"wb") as f:
        f.write(file_data)

    latest_pdf_path = file_path
    return {
        "message" : "PDF uploaded successfully",
        "filename" : file.filename,
        "saved_path" : file_path
    } 

# API 2 - PDF TO MARKDOWN + EXTRACT IMAGES
@app.post("/pdf-to-markdown")
async def pdf_to_markdown():
    """Convert latest uploaded PDF to Markdown
       and extract original embedded images.
    """

    global latest_pdf_path

    # Checking whether PDF was uploaded
    if latest_pdf_path is None:
        raise HTTPException(
            status_code=404,
            detail="Please upload a PDF first"
        )

    # Check whether PDF still exists
    if not os.path.exists(latest_pdf_path):
        raise HTTPException(
            status_code=404,
            detail="Uploaded PDF was not found"
        )

    # Get fileName
    fileName = os.path.basename(latest_pdf_path)
    print(fileName)
    base_name = os.path.splitext(fileName)[0]

    #  PDF -> Markdown
    markdown = pymupdf4llm.to_markdown(
        latest_pdf_path,
        force_ocr = True
    )

    #  Saving Markdown
    markdown_path = os.path.join("uploads",base_name + ".md")
    with open(markdown_path,"w",encoding="utf-8") as f:
        f.write(markdown)

    image_folder = os.path.join("uploads",base_name + "_images")

    os.makedirs(image_folder,exist_ok=True)

    # Open PDF with PyMuPDF
    pdf = fitz.open(
        latest_pdf_path
    )

    saved_images = []

    for page_number, page in enumerate(
        pdf,
        start=1
    ):

        # Get images that actually exist
        # inside the PDF page
        images = page.get_images(
            full=True
        )

        # -----------------------------------------
        # Extract each embedded image
        # -----------------------------------------

        for image_number, image in enumerate(
            images,
            start=1
        ):

            # Image reference
            xref = image[0]

            # Extract original image
            image_data = pdf.extract_image(
                xref
            )

            image_bytes = image_data["image"]

            image_extension = image_data["ext"]

            # Create image filename
            image_filename = (
                f"page_{page_number}_"
                f"image_{image_number}."
                f"{image_extension}"
            )

            image_path = os.path.join(
                image_folder,
                image_filename
            )

            # Save image
            with open(
                image_path,
                "wb"
            ) as f:

                f.write(image_bytes)

            saved_images.append(
                image_path
            )

    pdf.close()

    # RETURN RESULT
    
    return {
        "message": "PDF converted successfully",

        "pdf_file": latest_pdf_path,

        "markdown_file": markdown_path,

        "image_folder": image_folder,

        "image_count": len(saved_images),

        "images": saved_images
    }