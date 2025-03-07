Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ICommandContextHelper Interface   
[Members](topic136.md)   
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) : ICommandContextHelper Interface  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Provides a contract for an object capable of processing contextual data for commands which are context-specific. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Interface ICommandContextHelper   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ICommandContextHelper](topic135.md)  
  
C#|   
---|---  
      
    
    public interface ICommandContextHelper   
  
# Remarks

An instance of the `ICommandContextHelper` is supplied to [ICommandManager.RegisterContextualCommand](topic154.md) when registering a command which requires context.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ICommandContextHelper Members](topic136.md)   
[DriveWorks.Applications Namespace](topic16.md)


