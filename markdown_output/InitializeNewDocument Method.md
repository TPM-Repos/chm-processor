![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
InitializeNewDocument Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Administrator.Extensibility.Documents Namespace](topic1507.md) > [IDocumentDesigner Interface](topic1517.md) : InitializeNewDocument Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_application_
    The running application.

_creationWizard_
    The creation wizard returned by [GetCreationWizard](topic1523.md).

_document_
    The document to which to apply the settings.

Glossary Item Box

Applies the settings gathered by the creation wizard returned by [GetCreationWizard](topic1523.md) to the newly created document. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub InitializeNewDocument( _
       ByVal _application_ As [IApplication](topic24.md), _
       ByVal _creationWizard_ As [IWizard](topic613.md), _
       ByVal _document_ As [ProjectDocument](topic4356.md) _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IDocumentDesigner](topic1517.md)
    Dim application As [IApplication](topic24.md)
    Dim creationWizard As [IWizard](topic613.md)
    Dim document As [ProjectDocument](topic4356.md)
     
    instance.InitializeNewDocument(application, creationWizard, document)  
  
C#|   
---|---  
      
    
    void InitializeNewDocument( 
       [IApplication](topic24.md) _application_ ,
       [IWizard](topic613.md) _creationWizard_ ,
       [ProjectDocument](topic4356.md) _document_
    )  
  
#### Parameters

 _application_
    The running application.
_creationWizard_
    The creation wizard returned by [GetCreationWizard](topic1523.md).
_document_
    The document to which to apply the settings.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IDocumentDesigner Interface](topic1517.md)   
[IDocumentDesigner Members](topic1518.md)


