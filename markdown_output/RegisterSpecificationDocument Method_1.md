![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RegisterSpecificationDocument Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic4381.md)  
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

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Function RegisterSpecificationDocument( _
       ByVal _documentPath_ As String, _
       ByVal _isHidden_ As Boolean _
    ) As [SpecificationDocumentDetails](topic11333.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
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

# ![](dotnetimages/collapse.gif)Exceptions

Exception| Description  
---|---  
System.InvalidOperationException| Thrown if the project is not part of a running specification.  
  
# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectDocument Class](topic4356.md)   
[ProjectDocument Members](topic4357.md)

©2024 DriveWorks Ltd. All Rights Reserved.
