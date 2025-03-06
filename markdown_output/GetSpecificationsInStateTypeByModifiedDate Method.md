![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetSpecificationsInStateTypeByModifiedDate Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3380.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSpecifications Class](topic3355.md) : GetSpecificationsInStateTypeByModifiedDate Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_stateType_
    The type of state against which to filter the returned specifications.

_descending_
    True to retrieve specifications in reverse chronological order.

Glossary Item Box

Gets an enumerator which can be used to retrieve specifications in a given type of state in chronological order. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetSpecificationsInStateTypeByModifiedDate( _
       ByVal _stateType_ As [StateType](topic10773.md), _
       ByVal _descending_ As Boolean _
    ) As IEnumerable(Of SpecificationDetails)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [GroupSpecifications](topic3355.md)
    Dim stateType As [StateType](topic10773.md)
    Dim descending As Boolean
    Dim value As IEnumerable(Of SpecificationDetails)
     
    value = instance.GetSpecificationsInStateTypeByModifiedDate(stateType, descending)  
  
C#|   
---|---  
      
    
    public IEnumerable<SpecificationDetails> GetSpecificationsInStateTypeByModifiedDate( 
       [StateType](topic10773.md) _stateType_ ,
       bool _descending_
    )  
  
#### Parameters

 _stateType_
    The type of state against which to filter the returned specifications.
_descending_
    True to retrieve specifications in reverse chronological order.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[GroupSpecifications Class](topic3355.md)   
[GroupSpecifications Members](topic3356.md)

©2024 DriveWorks Ltd. All Rights Reserved.
