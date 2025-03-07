Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
DocumentCreated Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectDocuments Class](topic4434.md) : DocumentCreated Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when a document is created. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event DocumentCreated As [DocumentEventHandler](topic5931.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectDocuments](topic4434.md)
    Dim handler As [DocumentEventHandler](topic5931.md)
     
    AddHandler instance.DocumentCreated, handler  
  
C#|   
---|---  
      
    
    public event [DocumentEventHandler](topic5931.md) DocumentCreated  
  
# Event Data

The event handler receives an argument of type [DocumentEventArgs](topic2739.md) containing data related to this event. The following **DocumentEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[Document](topic2749.md)| Gets the document that was changed.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectDocuments Class](topic4434.md)   
[ProjectDocuments Members](topic4435.md)


