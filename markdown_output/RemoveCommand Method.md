       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RemoveCommand Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [ICommandBarGroup Interface](topic99.md) : RemoveCommand Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_command_
    The command of the button to remove.

Glossary Item Box

Removes the command button from the group. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function RemoveCommand( _
       ByVal _command_ As [ICommand](topic77.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
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

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ICommandBarGroup Interface](topic99.md)   
[ICommandBarGroup Members](topic100.md)


