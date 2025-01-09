import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Candidate
from .serializers import CandidateSerializer
from .helper import extract_text_from_pdf, parse_resume_with_openai  
import openai




class ResumeExtractionView(APIView):
    def post(self, request, *args, **kwargs):
        # Check if file is provided
        file = request.FILES.get('resume')
        if not file:
            return Response({"error": "No resume file provided."}, status=status.HTTP_400_BAD_REQUEST)

        # Extract text from PDF
        resume_text = extract_text_from_pdf(file)
        print(f'resume_test : {resume_text}')

        if not resume_text:
            return Response({"error": "Failed to extract text from resume."}, status=status.HTTP_400_BAD_REQUEST)

        # Parse resume text with OpenAI
        parsed_data = str(parse_resume_with_openai(resume_text))
        print(f'data : {parsed_data}')


        # Extract individual pieces of data (Assuming OpenAI returns them in the desired format)
        lines = parsed_data.split('\n')
        first_name = lines[0] if lines else "Unknown"
        email = lines[1] if len(lines) > 1 else "Unknown"
        mobile_number = lines[2] if len(lines) > 2 else "Unknown"

        # Save candidate details to the database
        candidate = Candidate.objects.create(
            first_name=first_name,
            email=email,
            mobile_number=mobile_number
        )

        # Serialize and return response
        serializer = CandidateSerializer(candidate)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        

        