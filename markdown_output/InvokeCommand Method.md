![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
InvokeCommand Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic149.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [ICommandManager Interface](topic143.md) : InvokeCommand Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_commandName_
    The name of the command to execute.

_commandContext_
    The context to be passed to the command, or a null reference (Nothing in Visual Basic).

Glossary Item Box

Invokes the specified command using the given arguments. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function InvokeCommand( _
       ByVal _commandName_ As String, _
       ByVal _commandContext_ As Object _
    ) As Boolean  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ICommandManager](topic143.md)
    Dim commandName As String
    Dim commandContext As Object
    Dim value As Boolean
     
    value = instance.InvokeCommand(commandName, commandContext)  
  
C#|   
---|---  
      
    
    bool InvokeCommand( 
       string _commandName_ ,
       object _commandContext_
    )  
  
#### Parameters

 _commandName_
    The name of the command to execute.
_commandContext_
    The context to be passed to the command, or a null reference (Nothing in Visual Basic).

#### Return Value

True if the command was found and invoked, false if the command was not registered.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ICommandManager Interface](topic143.md)   
[ICommandManager Members](topic144.md)

©2024 DriveWorks Ltd. All Rights Reserved.
