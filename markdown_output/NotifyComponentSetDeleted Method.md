![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
NotifyComponentSetDeleted Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components Namespace](topic6089.md) > [IReleaseTracker Interface](topic6119.md) : NotifyComponentSetDeleted Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_componentSet_
    The component set that was evaluated.

_rule_
    The rule which resulted in the "delete" value.

_result_
    The textual version of the result.

Glossary Item Box

Called when a component set has its rule evaluated as "delete". 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub NotifyComponentSetDeleted( _
       ByVal _componentSet_ As [ProjectComponentSet](topic4106.md), _
       ByVal _rule_ As String, _
       ByVal _result_ As String _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IReleaseTracker](topic6119.md)
    Dim componentSet As [ProjectComponentSet](topic4106.md)
    Dim rule As String
    Dim result As String
     
    instance.NotifyComponentSetDeleted(componentSet, rule, result)  
  
C#|   
---|---  
      
    
    void NotifyComponentSetDeleted( 
       [ProjectComponentSet](topic4106.md) _componentSet_ ,
       string _rule_ ,
       string _result_
    )  
  
#### Parameters

 _componentSet_
    The component set that was evaluated.
_rule_
    The rule which resulted in the "delete" value.
_result_
    The textual version of the result.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IReleaseTracker Interface](topic6119.md)   
[IReleaseTracker Members](topic6120.md)


