![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
DocumentEventArgs Constructor(ProjectDocument)   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [DocumentEventArgs Class](topic2739.md) > [DocumentEventArgs Constructor](topic2745.md) : DocumentEventArgs Constructor(ProjectDocument)  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_document_
    The document that was changed.

Glossary Item Box

Initializes a new instance of the [DocumentEventArgs](topic2739.md) type. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _document_ As [ProjectDocument](topic4356.md) _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim document As [ProjectDocument](topic4356.md)
     
    Dim instance As New [DocumentEventArgs](topic2739.md)(document)  
  
C#|   
---|---  
      
    
    public DocumentEventArgs( 
       [ProjectDocument](topic4356.md) _document_
    )  
  
#### Parameters

 _document_
    The document that was changed.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[DocumentEventArgs Class](topic2739.md)   
[DocumentEventArgs Members](topic2740.md)   
[Overload List](topic2745.md)


