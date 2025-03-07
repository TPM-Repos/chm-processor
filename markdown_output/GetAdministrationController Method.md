Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetAdministrationController Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Administrator.Extensibility.Documents Namespace](topic1507.md) > [IDocumentDesigner Interface](topic1517.md) : GetAdministrationController Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_application_
    The running application.

_document_
    The document to administer.

Glossary Item Box

Gets an administration controller for the given document. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function GetAdministrationController( _
       ByVal _application_ As [IApplication](topic24.md), _
       ByVal _document_ As [ProjectDocument](topic4356.md) _
    ) As [IDocumentAdministrationController](topic1509.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IDocumentDesigner](topic1517.md)
    Dim application As [IApplication](topic24.md)
    Dim document As [ProjectDocument](topic4356.md)
    Dim value As [IDocumentAdministrationController](topic1509.md)
     
    value = instance.GetAdministrationController(application, document)  
  
C#|   
---|---  
      
    
    [IDocumentAdministrationController](topic1509.md) GetAdministrationController( 
       [IApplication](topic24.md) _application_ ,
       [ProjectDocument](topic4356.md) _document_
    )  
  
#### Parameters

 _application_
    The running application.
_document_
    The document to administer.

#### Return Value

An instance of a type which implements the [IDocumentAdministrationController](topic1509.md) interface.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IDocumentDesigner Interface](topic1517.md)   
[IDocumentDesigner Members](topic1518.md)


