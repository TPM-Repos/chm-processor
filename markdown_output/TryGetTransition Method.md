![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TryGetTransition Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic11799.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [Transitions Class](topic11787.md) : TryGetTransition Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the transition to get.

_transition_
    Receives the transition.

Glossary Item Box

Gets the transition with the specified name. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function TryGetTransition( _
       ByVal _name_ As String, _
       ByRef _transition_ As [Transition](topic11757.md) _
    ) As Boolean  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [Transitions](topic11787.md)
    Dim name As String
    Dim transition As [Transition](topic11757.md)
    Dim value As Boolean
     
    value = instance.TryGetTransition(name, transition)  
  
C#|   
---|---  
      
    
    public bool TryGetTransition( 
       string _name_ ,
       ref [Transition](topic11757.md) _transition_
    )  
  
#### Parameters

 _name_
    The name of the transition to get.
_transition_
    Receives the transition.

#### Return Value

True if the transition was found and returned, otherwise false.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[Transitions Class](topic11787.md)   
[Transitions Members](topic11788.md)

©2024 DriveWorks Ltd. All Rights Reserved.
