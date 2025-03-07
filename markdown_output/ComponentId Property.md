Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ComponentId Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components.Tasks Namespace](topic6391.md) > [ComponentTask Class](topic6407.md) : ComponentId Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the id of the component this task is associated with. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property ComponentId As Nullable(Of Guid)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ComponentTask](topic6407.md)
    Dim value As Nullable(Of Guid)
     
    value = instance.ComponentId  
  
C#|   
---|---  
      
    
    public Nullable<Guid> ComponentId {get;}  
  
# Remarks

If this task is not associated with a component, this will return null. In which case the [Scope](topic6421.md) property should be used instead.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ComponentTask Class](topic6407.md)   
[ComponentTask Members](topic6408.md)


