Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CommandOverrideService Property   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IViewEnvironment Interface](topic549.md) : CommandOverrideService Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the view's command override service allowing it to override the standard implementations of commands. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    ReadOnly Property CommandOverrideService As [ICommandOverrideService](topic188.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IViewEnvironment](topic549.md)
    Dim value As [ICommandOverrideService](topic188.md)
     
    value = instance.CommandOverrideService  
  
C#|   
---|---  
      
    
    [ICommandOverrideService](topic188.md) CommandOverrideService {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IViewEnvironment Interface](topic549.md)   
[IViewEnvironment Members](topic550.md)


