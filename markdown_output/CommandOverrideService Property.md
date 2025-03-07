Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CommandOverrideService Property   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [ViewControl Class](topic1119.md) : CommandOverrideService Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the view's command override service allowing it to override the standard implementations of commands. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected ReadOnly Property CommandOverrideService As [ICommandOverrideService](topic188.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ViewControl](topic1119.md)
    Dim value As [ICommandOverrideService](topic188.md)
     
    value = instance.CommandOverrideService  
  
C#|   
---|---  
      
    
    protected [ICommandOverrideService](topic188.md) CommandOverrideService {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ViewControl Class](topic1119.md)   
[ViewControl Members](topic1120.md)


