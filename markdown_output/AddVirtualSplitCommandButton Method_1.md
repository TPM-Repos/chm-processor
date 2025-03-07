Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AddVirtualSplitCommandButton Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IQuickBarManager Interface](topic403.md) : AddVirtualSplitCommandButton Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_commandName_
    The name of the command to invoke when the command button is clicked.

_commandContext_
    The context to pass to the command when the command button is clicked.

_unavailableBehavior_
    The behavior of the command button element when the command is unavailable.

Glossary Item Box

Adds a new split command button, which has virtualized drop down items, to the group. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function AddVirtualSplitCommandButton( _
       ByVal _commandName_ As String, _
       ByVal _commandContext_ As Object, _
       ByVal _unavailableBehavior_ As [CommandUnavailableBehavior](topic659.md) _
    ) As [IVirtualSplitCommandButton](topic598.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IQuickBarManager](topic403.md)
    Dim commandName As String
    Dim commandContext As Object
    Dim unavailableBehavior As [CommandUnavailableBehavior](topic659.md)
    Dim value As [IVirtualSplitCommandButton](topic598.md)
     
    value = instance.AddVirtualSplitCommandButton(commandName, commandContext, unavailableBehavior)  
  
C#|   
---|---  
      
    
    [IVirtualSplitCommandButton](topic598.md) AddVirtualSplitCommandButton( 
       string _commandName_ ,
       object _commandContext_ ,
       [CommandUnavailableBehavior](topic659.md) _unavailableBehavior_
    )  
  
#### Parameters

 _commandName_
    The name of the command to invoke when the command button is clicked.
_commandContext_
    The context to pass to the command when the command button is clicked.
_unavailableBehavior_
    The behavior of the command button element when the command is unavailable.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IQuickBarManager Interface](topic403.md)   
[IQuickBarManager Members](topic404.md)


