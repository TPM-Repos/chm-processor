![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RaiseProjectRenameStarted Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IProjectService Interface](topic382.md) : RaiseProjectRenameStarted Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_sender_
    The object raising the event.

_e_
    The [ProjectRenameEventArgs](topic907.md) containing information about the project being renamed.

Glossary Item Box

Raises the [ProjectRenameStarted](topic402.md) event with the given parameters. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub RaiseProjectRenameStarted( _
       ByVal _sender_ As Object, _
       ByVal _e_ As [ProjectRenameEventArgs](topic907.md) _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IProjectService](topic382.md)
    Dim sender As Object
    Dim e As [ProjectRenameEventArgs](topic907.md)
     
    instance.RaiseProjectRenameStarted(sender, e)  
  
C#|   
---|---  
      
    
    void RaiseProjectRenameStarted( 
       object _sender_ ,
       [ProjectRenameEventArgs](topic907.md) _e_
    )  
  
#### Parameters

 _sender_
    The object raising the event.
_e_
    The [ProjectRenameEventArgs](topic907.md) containing information about the project being renamed.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IProjectService Interface](topic382.md)   
[IProjectService Members](topic383.md)


