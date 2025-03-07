Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
IsRunningRequired Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification.StandardTasks Namespace](topic11896.md) > [RealTimeReleaseModelsTask Class](topic12405.md) : IsRunningRequired Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_ctx_
    The specification context for the active specification.

Glossary Item Box

Overridden to indicate that a running specification is required by the task to execute. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Overrides Function IsRunningRequired( _
       ByVal _ctx_ As [SpecificationContext](topic11149.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [RealTimeReleaseModelsTask](topic12405.md)
    Dim ctx As [SpecificationContext](topic11149.md)
    Dim value As Boolean
     
    value = instance.IsRunningRequired(ctx)  
  
C#|   
---|---  
      
    
    protected override bool IsRunningRequired( 
       [SpecificationContext](topic11149.md) _ctx_
    )  
  
#### Parameters

 _ctx_
    The specification context for the active specification.

#### Return Value

True

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[RealTimeReleaseModelsTask Class](topic12405.md)   
[RealTimeReleaseModelsTask Members](topic12406.md)


