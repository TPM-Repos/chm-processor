![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TransitionEventArgs Constructor(Transition)   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic11783.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [TransitionEventArgs Class](topic11776.md) > [TransitionEventArgs Constructor](topic11782.md) : TransitionEventArgs Constructor(Transition)  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_transition_
    The transition which is the target of the event.

Glossary Item Box

Initializes a new instance of the [TransitionEventArgs](topic11776.md) type. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _transition_ As [Transition](topic11757.md) _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim transition As [Transition](topic11757.md)
     
    Dim instance As New [TransitionEventArgs](topic11776.md)(transition)  
  
C#|   
---|---  
      
    
    public TransitionEventArgs( 
       [Transition](topic11757.md) _transition_
    )  
  
#### Parameters

 _transition_
    The transition which is the target of the event.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[TransitionEventArgs Class](topic11776.md)   
[TransitionEventArgs Members](topic11777.md)   
[Overload List](topic11782.md)

©2024 DriveWorks Ltd. All Rights Reserved.
