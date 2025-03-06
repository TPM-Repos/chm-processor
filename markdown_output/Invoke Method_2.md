![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Invoke Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic2309.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ISafeProjectExecutor Interface](topic2303.md) : Invoke Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_action_
    

Glossary Item Box

Invokes an action synchronously on the same thread as the dispatcher. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub Invoke( _
       ByVal _action_ As Action _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ISafeProjectExecutor](topic2303.md)
    Dim action As Action
     
    instance.Invoke(action)  
  
C#|   
---|---  
      
    
    void Invoke( 
       Action _action_
    )  
  
#### Parameters

 _action_
    

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ISafeProjectExecutor Interface](topic2303.md)   
[ISafeProjectExecutor Members](topic2304.md)

©2024 DriveWorks Ltd. All Rights Reserved.
