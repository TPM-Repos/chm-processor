Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CommandManager Property   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IViewEnvironment Interface](topic549.md) : CommandManager Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the view's local command manager 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    ReadOnly Property CommandManager As [ICommandManager](topic143.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IViewEnvironment](topic549.md)
    Dim value As [ICommandManager](topic143.md)
     
    value = instance.CommandManager  
  
C#|   
---|---  
      
    
    [ICommandManager](topic143.md) CommandManager {get;}  
  
# Remarks

Commands registered by a view are local to the view and not accessible outside of the view.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IViewEnvironment Interface](topic549.md)   
[IViewEnvironment Members](topic550.md)


