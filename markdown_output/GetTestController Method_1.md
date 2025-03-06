![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
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

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function GetTestController( _
       ByVal _application_ As [IApplication](topic24.md), _
       ByVal _document_ As [ProjectDocument](topic4356.md) _
    ) As [IDocumentTestController](topic1532.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
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

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IDocumentTestProvider Interface](topic1540.md)   
[IDocumentTestProvider Members](topic1541.md)


