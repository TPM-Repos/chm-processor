![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SetReadyState Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic500.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IStatusBarService Interface](topic495.md) : SetReadyState Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_newReadyState_
    The ready state to apply, or a null reference to reset the ready state to ready.

Glossary Item Box

Sets the caption displayed in the ready state panel of the status bar. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub SetReadyState( _
       ByVal _newReadyState_ As String _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IStatusBarService](topic495.md)
    Dim newReadyState As String
     
    instance.SetReadyState(newReadyState)  
  
C#|   
---|---  
      
    
    void SetReadyState( 
       string _newReadyState_
    )  
  
#### Parameters

 _newReadyState_
    The ready state to apply, or a null reference to reset the ready state to ready.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IStatusBarService Interface](topic495.md)   
[IStatusBarService Members](topic496.md)

©2024 DriveWorks Ltd. All Rights Reserved.
