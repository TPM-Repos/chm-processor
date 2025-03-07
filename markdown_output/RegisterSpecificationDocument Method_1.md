Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RegisterSpecificationDocument Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectDocument Class](topic4356.md) : RegisterSpecificationDocument Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_documentPath_
    The fully qualified path to the document.

_isHidden_
    True if the document is filtered from the the normal end-user view.

Glossary Item Box

Registers a new specification document with the active specification. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Function RegisterSpecificationDocument( _
       ByVal _documentPath_ As String, _
       ByVal _isHidden_ As Boolean _
    ) As [SpecificationDocumentDetails](topic11333.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectDocument](topic4356.md)
    Dim documentPath As String
    Dim isHidden As Boolean
    Dim value As [SpecificationDocumentDetails](topic11333.md)
     
    value = instance.RegisterSpecificationDocument(documentPath, isHidden)  
  
C#|   
---|---  
      
    
    protected [SpecificationDocumentDetails](topic11333.md) RegisterSpecificationDocument( 
       string _documentPath_ ,
       bool _isHidden_
    )  
  
#### Parameters

 _documentPath_
    The fully qualified path to the document.
_isHidden_
    True if the document is filtered from the the normal end-user view.

# Exceptions

Exception| Description  
---|---  
System.InvalidOperationException| Thrown if the project is not part of a running specification.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectDocument Class](topic4356.md)   
[ProjectDocument Members](topic4357.md)


