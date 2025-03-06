![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TryUpdateSpecificationDocumentDirectory Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3407.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSpecifications Class](topic3355.md) : TryUpdateSpecificationDocumentDirectory Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_specificationId_
    The identification of the specification containing the document.

_documentId_
    The identification of the specification document to update.

_newPath_
    The new specification directory.

Glossary Item Box

Attempts to update a specification document location. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function TryUpdateSpecificationDocumentDirectory( _
       ByVal _specificationId_ As Integer, _
       ByVal _documentId_ As Guid, _
       ByVal _newPath_ As String _
    ) As Boolean  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [GroupSpecifications](topic3355.md)
    Dim specificationId As Integer
    Dim documentId As Guid
    Dim newPath As String
    Dim value As Boolean
     
    value = instance.TryUpdateSpecificationDocumentDirectory(specificationId, documentId, newPath)  
  
C#|   
---|---  
      
    
    public bool TryUpdateSpecificationDocumentDirectory( 
       int _specificationId_ ,
       Guid _documentId_ ,
       string _newPath_
    )  
  
#### Parameters

 _specificationId_
    The identification of the specification containing the document.
_documentId_
    The identification of the specification document to update.
_newPath_
    The new specification directory.

#### Return Value

True if the specification directory was successfully updated.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[GroupSpecifications Class](topic3355.md)   
[GroupSpecifications Members](topic3356.md)

©2024 DriveWorks Ltd. All Rights Reserved.
