from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine

# 1. Detect PII
analyzer = AnalyzerEngine()
results = analyzer.analyze(text="Patient John Doe has a heart condition.", entities=["PERSON"])

# 2. Redact/Anonymize
anonymizer = AnonymizerEngine()
anonymized_result = anonymizer.anonymize(
    text="Patient John Doe has a heart condition.",
    analyzer_results=results
)
# Output: "Patient <PERSON> has a heart condition."