![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
NotifyBeginEvaluate Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components Namespace](topic6089.md) > [IReleaseTracker Interface](topic6119.md) : NotifyBeginEvaluate Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_rootComponentSet_
    The component set to which the root component belongs.

_parentTrackingId_
    The tracking identifier of the parent component if there is one.

_component_
    The component being evaluated.

_componentTrackingId_
    A unique identifier which can be used to track the component, see remarks for more details.

_componentPath_
    The path to the component.

_nameRule_
    The rule which was evaluated to generate the component's name.

_nameResult_
    The result of evaluating the component's name rule.

_pathRule_
    The rule which was evaluated to generate the component's path.

_pathResult_
    The result of evaluating the component's path rule.

Glossary Item Box

Called when the evaluation of a component has begun. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub NotifyBeginEvaluate( _
       ByVal _rootComponentSet_ As [ProjectComponentSet](topic4106.md), _
       ByVal _parentTrackingId_ As Nullable(Of Guid), _
       ByVal _component_ As [ProjectComponent](topic6183.md), _
       ByVal _componentTrackingId_ As Guid, _
       ByVal _componentPath_ As String, _
       ByVal _nameRule_ As String, _
       ByVal _nameResult_ As String, _
       ByVal _pathRule_ As String, _
       ByVal _pathResult_ As String _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IReleaseTracker](topic6119.md)
    Dim rootComponentSet As [ProjectComponentSet](topic4106.md)
    Dim parentTrackingId As Nullable(Of Guid)
    Dim component As [ProjectComponent](topic6183.md)
    Dim componentTrackingId As Guid
    Dim componentPath As String
    Dim nameRule As String
    Dim nameResult As String
    Dim pathRule As String
    Dim pathResult As String
     
    instance.NotifyBeginEvaluate(rootComponentSet, parentTrackingId, component, componentTrackingId, componentPath, nameRule, nameResult, pathRule, pathResult)  
  
C#|   
---|---  
      
    
    void NotifyBeginEvaluate( 
       [ProjectComponentSet](topic4106.md) _rootComponentSet_ ,
       Nullable<Guid> _parentTrackingId_ ,
       [ProjectComponent](topic6183.md) _component_ ,
       Guid _componentTrackingId_ ,
       string _componentPath_ ,
       string _nameRule_ ,
       string _nameResult_ ,
       string _pathRule_ ,
       string _pathResult_
    )  
  
#### Parameters

 _rootComponentSet_
    The component set to which the root component belongs.
_parentTrackingId_
    The tracking identifier of the parent component if there is one.
_component_
    The component being evaluated.
_componentTrackingId_
    A unique identifier which can be used to track the component, see remarks for more details.
_componentPath_
    The path to the component.
_nameRule_
    The rule which was evaluated to generate the component's name.
_nameResult_
    The result of evaluating the component's name rule.
_pathRule_
    The rule which was evaluated to generate the component's path.
_pathResult_
    The result of evaluating the component's path rule.

# ![](dotnetimages/collapse.gif)Remarks

The componentTrackingId can be used to track a component as it is evaluated and released. If the component is evaluated to be a new component (as opposed to an alternative, driven component, or existing component), then the tracking id is the id that is assigned to the released component.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IReleaseTracker Interface](topic6119.md)   
[IReleaseTracker Members](topic6120.md)


