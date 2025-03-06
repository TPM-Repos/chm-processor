       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
UnregisterCommandOverride Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic134.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [ICommandButtonManager Interface](topic124.md) : UnregisterCommandOverride Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_command_
    the [ICommandOverride](topic180.md) to be unregistered.

Glossary Item Box

Unregisters a command override for the specified command. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub UnregisterCommandOverride( _
       ByVal _command_ As [ICommandOverride](topic180.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ICommandButtonManager](topic124.md)
    Dim command As [ICommandOverride](topic180.md)
     
    instance.UnregisterCommandOverride(command)  
  
C#|   
---|---  
      
    
    void UnregisterCommandOverride( 
       [ICommandOverride](topic180.md) _command_
    )  
  
#### Parameters

 _command_
    the [ICommandOverride](topic180.md) to be unregistered.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ICommandButtonManager Interface](topic124.md)   
[ICommandButtonManager Members](topic125.md)

©2024 DriveWorks Ltd. All Rights Reserved.
