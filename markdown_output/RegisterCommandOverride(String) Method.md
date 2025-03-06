![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RegisterCommandOverride(String) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic132.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [ICommandButtonManager Interface](topic124.md) > [RegisterCommandOverride Method](topic131.md) : RegisterCommandOverride(String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_commandName_
    The name of the command for which to get a command override.

Glossary Item Box

Creates a command override object for the specified command. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Overloads Function RegisterCommandOverride( _
       ByVal _commandName_ As String _
    ) As [ICommandOverride](topic180.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ICommandButtonManager](topic124.md)
    Dim commandName As String
    Dim value As [ICommandOverride](topic180.md)
     
    value = instance.RegisterCommandOverride(commandName)  
  
C#|   
---|---  
      
    
    [ICommandOverride](topic180.md) RegisterCommandOverride( 
       string _commandName_
    )  
  
#### Parameters

 _commandName_
    The name of the command for which to get a command override.

#### Return Value

A command override object for the specified command, allowing the caller to override the behavior of the specified command.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ICommandButtonManager Interface](topic124.md)   
[ICommandButtonManager Members](topic125.md)   
[Overload List](topic131.md)

©2024 DriveWorks Ltd. All Rights Reserved.
