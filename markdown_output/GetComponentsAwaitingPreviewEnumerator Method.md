![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetComponentsAwaitingPreviewEnumerator Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3257.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupReleasedComponents Class](topic3238.md) : GetComponentsAwaitingPreviewEnumerator Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_topLevelOnly_
    True to only get top level (root) components.

Glossary Item Box

Gets an object which will enumerate the released components that are awaiting a preview in the group. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <EditorBrowsableAttribute(EditorBrowsableState.Advanced)>
    Public Function GetComponentsAwaitingPreviewEnumerator( _
       ByVal _topLevelOnly_ As Boolean _
    ) As [IGroupResultEnumerator(Of ReleasedComponentDetails)](topic2220.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [GroupReleasedComponents](topic3238.md)
    Dim topLevelOnly As Boolean
    Dim value As [IGroupResultEnumerator(Of ReleasedComponentDetails)](topic2220.md)
     
    value = instance.GetComponentsAwaitingPreviewEnumerator(topLevelOnly)  
  
C#|   
---|---  
      
    
    [EditorBrowsableAttribute(EditorBrowsableState.Advanced)]
    public [IGroupResultEnumerator<ReleasedComponentDetails>](topic2220.md) GetComponentsAwaitingPreviewEnumerator( 
       bool _topLevelOnly_
    )  
  
#### Parameters

 _topLevelOnly_
    True to only get top level (root) components.

#### Return Value

An enumerator for released components awaiting a preview in the group.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[GroupReleasedComponents Class](topic3238.md)   
[GroupReleasedComponents Members](topic3239.md)

©2024 DriveWorks Ltd. All Rights Reserved.
