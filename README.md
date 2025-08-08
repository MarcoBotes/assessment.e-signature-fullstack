# Assessment Overview

Create a simple feature in the existing application to showcase that I can capture and send PDF data to a backend service, and properly handlt the response

## Result
![Gif showing the user interface for the assessment](readme/assessment_showcase.gif)

```python
>>> python.exe validate_metadata.py 
signed_simple.pdf {'/Producer': 'PyPDF2', '/SignedBy': 'Marco', '/SignedAt': '2025-08-08 10:30:42.096198', '/Purpose': 'Test signing'}

Process finished with exit code 0
```