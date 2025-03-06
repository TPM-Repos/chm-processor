       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TryGetDocument Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic4446.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectDocuments Class](topic4434.md) : TryGetDocument Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the document to retrieve.

_document_
    A reference to a variable which will receive the document.

Glossary Item Box

Tries to get a document with the specified name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function TryGetDocument( _
       ByVal _name_ As String, _
       ByRef _document_ As [ProjectDocument](topic4356.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectDocuments](topic4434.md)
    Dim name As String
    Dim document As [ProjectDocument](topic4356.md)
    Dim value As Boolean
     
    value = instance.TryGetDocument(name, document)  
  
C#|   
---|---  
      
    
    public bool TryGetDocument( 
       string _name_ ,
       ref [ProjectDocument](topic4356.md) _document_
    )  
  
#### Parameters

 _name_
    The name of the document to retrieve.
_document_
    A reference to a variable which will receive the document.

#### Return Value

True if the document was found and returned, otherwise false.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectDocuments Class](topic4434.md)   
[ProjectDocuments Members](topic4435.md)

©2024 DriveWorks Ltd. All Rights Reserved.
