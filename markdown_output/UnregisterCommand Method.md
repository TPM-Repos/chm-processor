       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
UnregisterCommand Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic156.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [ICommandManager Interface](topic143.md) : UnregisterCommand Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_command_
    The command to unregister.

Glossary Item Box

Unregisters the specified command with the command manager. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function UnregisterCommand( _
       ByVal _command_ As [ICommand](topic77.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ICommandManager](topic143.md)
    Dim command As [ICommand](topic77.md)
    Dim value As Boolean
     
    value = instance.UnregisterCommand(command)  
  
C#|   
---|---  
      
    
    bool UnregisterCommand( 
       [ICommand](topic77.md) _command_
    )  
  
#### Parameters

 _command_
    The command to unregister.

#### Return Value

True if the command was unregistered.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ICommandManager Interface](topic143.md)   
[ICommandManager Members](topic144.md)

©2024 DriveWorks Ltd. All Rights Reserved.
