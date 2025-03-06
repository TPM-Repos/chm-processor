![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetComponents(Boolean,Boolean,Boolean,Boolean) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3255.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupReleasedComponents Class](topic3238.md) > [GetComponents Method](topic3254.md) : GetComponents(Boolean,Boolean,Boolean,Boolean) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_topLevelOnly_
    True to only get top level (root) components.

_includeGenerated_
    True to include generated components, false to exclude them.

_includeNotGenerated_
    True to include components which haven't been generated, false to exclude them.

_includeFailed_
    True to include failed components, false to exclude them.

Glossary Item Box

Gets an object which will enumerate the released components in the group. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function GetComponents( _
       ByVal _topLevelOnly_ As Boolean, _
       ByVal _includeGenerated_ As Boolean, _
       ByVal _includeNotGenerated_ As Boolean, _
       ByVal _includeFailed_ As Boolean _
    ) As [IGroupResultEnumerator(Of ReleasedComponentDetails)](topic2220.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [GroupReleasedComponents](topic3238.md)
    Dim topLevelOnly As Boolean
    Dim includeGenerated As Boolean
    Dim includeNotGenerated As Boolean
    Dim includeFailed As Boolean
    Dim value As [IGroupResultEnumerator(Of ReleasedComponentDetails)](topic2220.md)
     
    value = instance.GetComponents(topLevelOnly, includeGenerated, includeNotGenerated, includeFailed)  
  
C#|   
---|---  
      
    
    public [IGroupResultEnumerator<ReleasedComponentDetails>](topic2220.md) GetComponents( 
       bool _topLevelOnly_ ,
       bool _includeGenerated_ ,
       bool _includeNotGenerated_ ,
       bool _includeFailed_
    )  
  
#### Parameters

 _topLevelOnly_
    True to only get top level (root) components.
_includeGenerated_
    True to include generated components, false to exclude them.
_includeNotGenerated_
    True to include components which haven't been generated, false to exclude them.
_includeFailed_
    True to include failed components, false to exclude them.

#### Return Value

An enumerator over the released components in the group.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[GroupReleasedComponents Class](topic3238.md)   
[GroupReleasedComponents Members](topic3239.md)   
[Overload List](topic3254.md)

©2024 DriveWorks Ltd. All Rights Reserved.
