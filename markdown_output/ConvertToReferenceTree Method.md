![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ConvertToReferenceTree Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components Namespace](topic6089.md) > [ReleaseComponentsResults Class](topic6300.md) : ConvertToReferenceTree Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_group_
    The group to use to load preexisting component reference information.

Glossary Item Box

Converts the release results to a complete component reference tree by copying across reference information from this release session, and retrieving information for precedent components that were released in other sessions from the group. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function ConvertToReferenceTree( _
       ByVal _group_ As [Group](topic2958.md) _
    ) As [IReleasedComponentReferenceTree](topic6106.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ReleaseComponentsResults](topic6300.md)
    Dim group As [Group](topic2958.md)
    Dim value As [IReleasedComponentReferenceTree](topic6106.md)
     
    value = instance.ConvertToReferenceTree(group)  
  
C#|   
---|---  
      
    
    public [IReleasedComponentReferenceTree](topic6106.md) ConvertToReferenceTree( 
       [Group](topic2958.md) _group_
    )  
  
#### Parameters

 _group_
    The group to use to load preexisting component reference information.

#### Return Value

A released component reference tree.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ReleaseComponentsResults Class](topic6300.md)   
[ReleaseComponentsResults Members](topic6301.md)


