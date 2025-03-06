![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RegisterSpecificationDocument Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSpecifications Class](topic3355.md) : RegisterSpecificationDocument Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_specificationId_
    The id of the specification against which to register the document.

_documentPath_
    The fully qualified path to the document.

_isHidden_
    True if the document is filtered from the the normal end-user view.

Glossary Item Box

Registers a new specification document with an existing specification. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function RegisterSpecificationDocument( _
       ByVal _specificationId_ As Integer, _
       ByVal _documentPath_ As String, _
       ByVal _isHidden_ As Boolean _
    ) As [SpecificationDocumentDetails](topic11333.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [GroupSpecifications](topic3355.md)
    Dim specificationId As Integer
    Dim documentPath As String
    Dim isHidden As Boolean
    Dim value As [SpecificationDocumentDetails](topic11333.md)
     
    value = instance.RegisterSpecificationDocument(specificationId, documentPath, isHidden)  
  
C#|   
---|---  
      
    
    public [SpecificationDocumentDetails](topic11333.md) RegisterSpecificationDocument( 
       int _specificationId_ ,
       string _documentPath_ ,
       bool _isHidden_
    )  
  
#### Parameters

 _specificationId_
    The id of the specification against which to register the document.
_documentPath_
    The fully qualified path to the document.
_isHidden_
    True if the document is filtered from the the normal end-user view.

#### Return Value

An instance of the [DriveWorks.Specification.SpecificationDocumentDetails](topic11333.md) class containing information about the document.

# ![](dotnetimages/collapse.gif)Exceptions

Exception| Description  
---|---  
System.ArgumentException| The documentPath is empty, or too long.  
  
# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[GroupSpecifications Class](topic3355.md)   
[GroupSpecifications Members](topic3356.md)


