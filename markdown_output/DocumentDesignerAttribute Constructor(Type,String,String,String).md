![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
DocumentDesignerAttribute Constructor(Type,String,String,String)   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Administrator.Extensibility.Documents Namespace](topic1507.md) > [DocumentDesignerAttribute Class](topic1568.md) > [DocumentDesignerAttribute Constructor](topic1574.md) : DocumentDesignerAttribute Constructor(Type,String,String,String)  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_documentType_
    The type of document supported by the designer (must be derived from [DriveWorks.ProjectDocument](topic4356.md)).

_displayName_
    The localizable display name of the document type.

_image_
    The localizable image of the document type.

_descriptionHtml_
    The localizable description of the document.

Glossary Item Box

Initializes a new instance of the [DocumentDesignerAttribute](topic1568.md) attribute class. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _documentType_ As Type, _
       ByVal _displayName_ As String, _
       ByVal _image_ As String, _
       ByVal _descriptionHtml_ As String _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim documentType As Type
    Dim displayName As String
    Dim image As String
    Dim descriptionHtml As String
     
    Dim instance As New [DocumentDesignerAttribute](topic1568.md)(documentType, displayName, image, descriptionHtml)  
  
C#|   
---|---  
      
    
    public DocumentDesignerAttribute( 
       Type _documentType_ ,
       string _displayName_ ,
       string _image_ ,
       string _descriptionHtml_
    )  
  
#### Parameters

 _documentType_
    The type of document supported by the designer (must be derived from [DriveWorks.ProjectDocument](topic4356.md)).
_displayName_
    The localizable display name of the document type.
_image_
    The localizable image of the document type.
_descriptionHtml_
    The localizable description of the document.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[DocumentDesignerAttribute Class](topic1568.md)   
[DocumentDesignerAttribute Members](topic1569.md)   
[Overload List](topic1574.md)


