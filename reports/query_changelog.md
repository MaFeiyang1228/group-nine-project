# Query Design Rationale

## Research Question

What are the research trends and technological developments in RISC-V CPU architecture and processor design?

This project aims to analyze the academic literature related to RISC-V processors using bibliometric methods in order to identify research hotspots, collaboration networks, and emerging trends.

---

## Concept Decomposition

Following the Object–Method–Context framework used in bibliometric query design:

Object  
RISC-V processor architecture

Method  
Processor architecture design and microarchitecture

Context  
Computer architecture and embedded systems

Constraint  
Time window: 2020–2025

---

## Time Window

2020–2025

Reason:

RISC-V has experienced rapid development in recent years, especially after its growing adoption in industry and academia.  
Restricting the time window to recent years allows us to capture current research trends.

---

## Document Types

Article  
Review

Reason:

Articles represent original research contributions, while review papers summarize important developments in the field.

---

## Field Restrictions

title  
abstract  
keyword

Reason:

Searching within these fields provides a balance between precision and recall.

Title search increases precision while abstract and keyword search improves coverage of relevant literature.

---

## Synonym Strategy

To improve recall, synonyms and related expressions are grouped within each concept using the OR operator.

Object synonyms

RISC-V  
RISC V  
RISC-V processor  
RISC-V CPU  
RISC-V architecture  

Method synonyms

processor design  
cpu architecture  
microarchitecture  
processor architecture  
instruction set architecture  

Context synonyms

computer architecture  
embedded system  
system on chip  
SoC  
hardware design  

---

## Boolean Logic Structure

The query follows the structure:

(Object synonyms) AND (Method synonyms) AND (Context synonyms)

Example query expression:

("RISC-V" OR "RISC V" OR "RISC-V processor" OR "RISC-V CPU" OR "RISC-V architecture")

AND

("processor design" OR "cpu architecture" OR "microarchitecture" OR "instruction set architecture")

AND

("embedded system" OR "computer architecture" OR "system on chip" OR "SoC")

---

## Expected Results

The query is expected to retrieve literature focusing on:

- RISC-V CPU architecture design
- processor microarchitecture
- hardware implementation of RISC-V
- applications in embedded and computer systems

The retrieved dataset will be used for bibliometric analysis including:

- keyword co-occurrence
- collaboration networks
- research trend detection