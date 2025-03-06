ScopedTasks Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components Namespace](topic6089.md) > [ReleaseComponentsResults Class](topic6300.md) : ScopedTasks Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the scoped [DriveWorks.Components.Tasks.ComponentTask](topic6407.md)s that were released. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property ScopedTasks As [ReleasedComponentTask()](topic5061.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReleaseComponentsResults](topic6300.md)
    Dim value() As [ReleasedComponentTask](topic5061.md)
     
    value = instance.ScopedTasks  
  
C#|   
---|---  
      
    
    public [ReleasedComponentTask[]](topic5061.md) ScopedTasks {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleaseComponentsResults Class](topic6300.md)   
[ReleaseComponentsResults Members](topic6301.md)


