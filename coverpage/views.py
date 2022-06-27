from django.shortcuts import render
from django.http import HttpResponse
from docxtpl import DocxTemplate
from django.http import FileResponse

# Create your views here.


def create_cover(request):
    doc = DocxTemplate("templates/research_Cover.docx")
    project_title = "MEEGU – FOR AN EASY AND MEANINGFUL RESEARCH JOURNEY"
    project_collegeDept = "College of Computer, Information and Communication Technology Department"
    project_course = "Bachelor of Science in Information Technology"
    project_authors = ["Aplacador, Jonathan D.", "Sinogaya, Ma. Thania T."]
    project_adviser = "Gibe S. Tirol"
    context = {
        "project_title": project_title,
        "project_collegeDept": project_collegeDept,
        "project_course": project_course,
        "project_authors": project_authors,
        "project_adviser": project_adviser,
    }
    print(context.items())
    doc.render(context)
    doc.save("templates/generated_doc.docx")

    return FileResponse(open("templates/generated_doc.docx", "rb"))
    pass
