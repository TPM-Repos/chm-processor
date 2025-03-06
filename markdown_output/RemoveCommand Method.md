![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RemoveCommand Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic108.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [ICommandBarGroup Interface](topic99.md) : RemoveCommand Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_command_
    The command of the button to remove.

Glossary Item Box

Removes the command button from the group. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function RemoveCommand( _
       ByVal _command_ As [ICommand](topic77.md) _
    ) As Boolean  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ICommandBarGroup](topic99.md)
    Dim command As [ICommand](topic77.md)
    Dim value As Boolean
     
    value = instance.RemoveCommand(command)  
  
C#|   
---|---  
      
    
    bool RemoveCommand( 
       [ICommand](topic77.md) _command_
    )  
  
#### Parameters

 _command_
    The command of the button to remove.

#### Return Value

True if the command button was removed.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ICommandBarGroup Interface](topic99.md)   
[ICommandBarGroup Members](topic100.md)

©2024 DriveWorks Ltd. All Rights Reserved.
