Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetCommandMonitor Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [ICommandManager Interface](topic143.md) : GetCommandMonitor Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_commandName_
    The name of the [ICommand](topic77.md) whose monitor to retrieve.

Glossary Item Box

Gets the [ICommandMonitor](topic158.md) for the [ICommand](topic77.md) with the given name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function GetCommandMonitor( _
       ByVal _commandName_ As String _
    ) As [ICommandMonitor](topic158.md)  
  
Visual Basic (Usage)| Copy Code  
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

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ICommandManager Interface](topic143.md)   
[ICommandManager Members](topic144.md)


