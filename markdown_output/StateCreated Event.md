![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
StateCreated Event   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic11627.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [States Class](topic11612.md) : StateCreated Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Occurs when a state is created. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event StateCreated As [StateEventHandler](topic11825.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [States](topic11612.md)
    Dim handler As [StateEventHandler](topic11825.md)
     
    AddHandler instance.StateCreated, handler  
  
C#|   
---|---  
      
    
    public event [StateEventHandler](topic11825.md) StateCreated  
  
# ![](dotnetimages/collapse.gif)Event Data

The event handler receives an argument of type [StateEventArgs](topic11590.md) containing data related to this event. The following **StateEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[State](topic11600.md)| Gets the state which is the target of the event.   
  
# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[States Class](topic11612.md)   
[States Members](topic11613.md)

©2024 DriveWorks Ltd. All Rights Reserved.
