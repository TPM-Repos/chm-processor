Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetTestController Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Administrator.Extensibility.Documents Namespace](topic1507.md) > [IDocumentTestProvider Interface](topic1540.md) : GetTestController Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_application_
    The running application.

_document_
    The document to be tested.

Glossary Item Box

Creates a new test controller suitable for the document. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function GetTestController( _
       ByVal _application_ As [IApplication](topic24.md), _
       ByVal _document_ As [ProjectDocument](topic4356.md) _
    ) As [IDocumentTestController](topic1532.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IDocumentTestProvider](topic1540.md)
    Dim application As [IApplication](topic24.md)
    Dim document As [ProjectDocument](topic4356.md)
    Dim value As [IDocumentTestController](topic1532.md)
     
    value = instance.GetTestController(application, document)  
  
C#|   
---|---  
      
    
    [IDocumentTestController](topic1532.md) GetTestController( 
       [IApplication](topic24.md) _application_ ,
       [ProjectDocument](topic4356.md) _document_
    )  
  
#### Parameters

 _application_
    The running application.
_document_
    The document to be tested.

#### Return Value

An instance of a type which implements the [IDocumentTestController](topic1532.md) interface.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IDocumentTestProvider Interface](topic1540.md)   
[IDocumentTestProvider Members](topic1541.md)


