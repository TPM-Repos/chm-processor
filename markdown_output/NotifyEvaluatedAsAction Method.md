![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
NotifyEvaluatedAsAction Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components Namespace](topic6089.md) > [IReleaseTracker Interface](topic6119.md) : NotifyEvaluatedAsAction Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_action_
    The action to be taken.

_isValid_
    True if the action is valid for the type of component, otherwise false.

Glossary Item Box

Called when the current component is determined to need a non-replacement action applying. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub NotifyEvaluatedAsAction( _
       ByVal _action_ As [ReleasedComponentReferenceAction](topic6146.md), _
       ByVal _isValid_ As Boolean _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IReleaseTracker](topic6119.md)
    Dim action As [ReleasedComponentReferenceAction](topic6146.md)
    Dim isValid As Boolean
     
    instance.NotifyEvaluatedAsAction(action, isValid)  
  
C#|   
---|---  
      
    
    void NotifyEvaluatedAsAction( 
       [ReleasedComponentReferenceAction](topic6146.md) _action_ ,
       bool _isValid_
    )  
  
#### Parameters

 _action_
    The action to be taken.
_isValid_
    True if the action is valid for the type of component, otherwise false.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IReleaseTracker Interface](topic6119.md)   
[IReleaseTracker Members](topic6120.md)


