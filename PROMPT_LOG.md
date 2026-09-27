# Appendix A: Full AI Prompt Log

**Exercise ID:** HW01-AI  
**Student Name:** Phan Trung Tin (ID: 23120372)  
**Date:** September 27, 2026  

---

## Log Entry 1: Mindmap Generation for CLO G9.1
- **Timestamp:** 10:15 27/09/2026
- **Tool:** Gemini 1.5 Pro
- **Model Parameters:** Default temperature (0.7), web search enabled
- **Prompt:**
  ```text
  Act as a Senior QA Architect and generate a comprehensive mindmap in Mermaid format representing the QA/QC roles, responsibilities, and the end-to-end software test process according to the latest ISTQB Foundation Level syllabus. Structure it into major branches covering QA vs QC, test levels, test types, and sequential activities in the test process.
  ```
- **Response Received:** Mindmap generated with 4 branches (Quality Control & Assurance, Test Levels, Test Types, Test Process).
- **Student Action / Audit:** Found 3 major errors (inverted QA/QC definitions, omitted Static Testing, and mispositioned Test Monitoring as sequential step #4). Manually corrected into ISTQB CTFL v4.0 aligned mindmap.

---

## Log Entry 2: Verification of Software Defects 2022–2026 for Requirement 2
- **Timestamp:** 10:48 27/09/2026
- **Tool:** ChatGPT (GPT-4o)
- **Prompt:**
  ```text
  Provide a technical breakdown of 20 high-profile publicized software defects between 2022 and 2026, including at least 5 AI/LLM defects (such as hallucinations, prompt injections, safety guardrail failures). For each, give the date, organization, root cause, severity, impact, and solution.
  ```
- **Response Received:** List of 20 defects with descriptions and root causes.
- **Student Action / Audit:** Analyzed the AI response for hallucinations, bias, and technical confabulations across all 20 entries. Identified specific hallucinations (such as attributing the CrowdStrike incident to a kernel C++ null pointer exception rather than an out-of-bounds read in Channel File 291 content parser, or claiming Air Canada's chatbot hallucination had a valid disclaimers defense upheld in court). Replaced inaccuracies with verified primary post-mortem reports.

---

## Log Entry 3: Initial Physical Device Test Cases for Requirement 3
- **Timestamp:** 11:30 27/09/2026
- **Tool:** ChatGPT (GPT-4o)
- **Prompt:**
  ```text
  I have a USB-powered adjustable LED desk lamp with 4 inline buttons: Power (ON/OFF), Brightness (-), Light Mode (Yellow, White, Warm White), and Brightness (+). Design a comprehensive 15 test case suite for this physical device following standard QA test case format (ID, Objective, Input, Steps, Expected Result). Include edge cases.
  ```
- **Response Received:** 15 test cases focusing on trivial button clicks and generic duration tests.
- **Student Action / Audit:** Identified complete absence of electrical (inrush current, undervoltage brownout), optical (PWM frequency strobe effect), and mechanical physics (cantilever torque droop). Formulated the 3 missed edge cases and overhauled all 15 test cases with physical measurements and real execution steps.
