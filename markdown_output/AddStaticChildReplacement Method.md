![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AddStaticChildReplacement Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic6264.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components Namespace](topic6089.md) > [ReleaseComponentController Class](topic6252.md) : AddStaticChildReplacement Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_childMasterPath_
    The path of the child to replace.

_childAddress_
    The address of the child (if applicable).

_alternativePath_
    The path to the alternative to swap in.

_parentId_
    The id of the parent.

Glossary Item Box

Adds a new static child replacement for the child with the given master path 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function AddStaticChildReplacement( _
       ByVal _childMasterPath_ As String, _
       ByVal _childAddress_ As String, _
       ByVal _alternativePath_ As String, _
       ByVal _parentId_ As Guid _
    ) As Boolean  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ReleaseComponentController](topic6252.md)
    Dim childMasterPath As String
    Dim childAddress As String
    Dim alternativePath As String
    Dim parentId As Guid
    Dim value As Boolean
     
    value = instance.AddStaticChildReplacement(childMasterPath, childAddress, alternativePath, parentId)  
  
C#|   
---|---  
      
    
    public bool AddStaticChildReplacement( 
       string _childMasterPath_ ,
       string _childAddress_ ,
       string _alternativePath_ ,
       Guid _parentId_
    )  
  
#### Parameters

 _childMasterPath_
    The path of the child to replace.
_childAddress_
    The address of the child (if applicable).
_alternativePath_
    The path to the alternative to swap in.
_parentId_
    The id of the parent.

#### Return Value

True if the static replacement was added, False if a replacement has already been registered for the given child.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ReleaseComponentController Class](topic6252.md)   
[ReleaseComponentController Members](topic6253.md)

©2024 DriveWorks Ltd. All Rights Reserved.
