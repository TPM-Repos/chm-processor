![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetAdministrationController Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic1522.md)  
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

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function GetAdministrationController( _
       ByVal _application_ As [IApplication](topic24.md), _
       ByVal _document_ As [ProjectDocument](topic4356.md) _
    ) As [IDocumentAdministrationController](topic1509.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
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

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IDocumentDesigner Interface](topic1517.md)   
[IDocumentDesigner Members](topic1518.md)

©2024 DriveWorks Ltd. All Rights Reserved.
