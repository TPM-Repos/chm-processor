Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
DocumentRegistered Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [SpecificationContext Class](topic11149.md) : DocumentRegistered Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when a specification document is registered. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event DocumentRegistered As [SpecificationDocumentEventHandler](topic11822.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationContext](topic11149.md)
    Dim handler As [SpecificationDocumentEventHandler](topic11822.md)
     
    AddHandler instance.DocumentRegistered, handler  
  
C#|   
---|---  
      
    
    public event [SpecificationDocumentEventHandler](topic11822.md) DocumentRegistered  
  
# Event Data

The event handler receives an argument of type [SpecificationDocumentEventArgs](topic11344.md) containing data related to this event. The following **SpecificationDocumentEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[DocumentDetails](topic11354.md)| Gets the document details.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationContext Class](topic11149.md)   
[SpecificationContext Members](topic11150.md)


