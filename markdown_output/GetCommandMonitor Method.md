![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetCommandMonitor Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic148.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [ICommandManager Interface](topic143.md) : GetCommandMonitor Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_commandName_
    The name of the [ICommand](topic77.md) whose monitor to retrieve.

Glossary Item Box

Gets the [ICommandMonitor](topic158.md) for the [ICommand](topic77.md) with the given name. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function GetCommandMonitor( _
       ByVal _commandName_ As String _
    ) As [ICommandMonitor](topic158.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ICommandManager](topic143.md)
    Dim commandName As String
    Dim value As [ICommandMonitor](topic158.md)
     
    value = instance.GetCommandMonitor(commandName)  
  
C#|   
---|---  
      
    
    [ICommandMonitor](topic158.md) GetCommandMonitor( 
       string _commandName_
    )  
  
#### Parameters

 _commandName_
    The name of the [ICommand](topic77.md) whose monitor to retrieve.

#### Return Value

The [ICommandMonitor](topic158.md) for the command, or a null reference (Nothing in Visual Basic) if a command with the given name has not been registered on this [ICommandManager](topic143.md).

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ICommandManager Interface](topic143.md)   
[ICommandManager Members](topic144.md)

©2024 DriveWorks Ltd. All Rights Reserved.
