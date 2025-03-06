![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RaiseProjectRenameFinished Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic390.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IProjectService Interface](topic382.md) : RaiseProjectRenameFinished Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_sender_
    The object raising the event.

_e_
    The [ProjectRenameEventArgs](topic907.md) containing information about the newly renamed project.

Glossary Item Box

Raises the [ProjectRenameFinished](topic401.md) event with the given parameters. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub RaiseProjectRenameFinished( _
       ByVal _sender_ As Object, _
       ByVal _e_ As [ProjectRenameEventArgs](topic907.md) _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IProjectService](topic382.md)
    Dim sender As Object
    Dim e As [ProjectRenameEventArgs](topic907.md)
     
    instance.RaiseProjectRenameFinished(sender, e)  
  
C#|   
---|---  
      
    
    void RaiseProjectRenameFinished( 
       object _sender_ ,
       [ProjectRenameEventArgs](topic907.md) _e_
    )  
  
#### Parameters

 _sender_
    The object raising the event.
_e_
    The [ProjectRenameEventArgs](topic907.md) containing information about the newly renamed project.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IProjectService Interface](topic382.md)   
[IProjectService Members](topic383.md)

©2024 DriveWorks Ltd. All Rights Reserved.
