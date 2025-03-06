![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TryGetState(String,State) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic11624.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [States Class](topic11612.md) > [TryGetState Method](topic11622.md) : TryGetState(String,State) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_title_
    The title of the state to try find.

_state_
    The matching state or null.

Glossary Item Box

Tries to get the state with the specified title. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function TryGetState( _
       ByVal _title_ As String, _
       ByRef _state_ As [State](topic11559.md) _
    ) As Boolean  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [States](topic11612.md)
    Dim title As String
    Dim state As [State](topic11559.md)
    Dim value As Boolean
     
    value = instance.TryGetState(title, state)  
  
C#|   
---|---  
      
    
    public bool TryGetState( 
       string _title_ ,
       ref [State](topic11559.md) _state_
    )  
  
#### Parameters

 _title_
    The title of the state to try find.
_state_
    The matching state or null.

#### Return Value

True if the state is found.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[States Class](topic11612.md)   
[States Members](topic11613.md)   
[Overload List](topic11622.md)

©2024 DriveWorks Ltd. All Rights Reserved.
