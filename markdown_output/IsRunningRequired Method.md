Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
IsRunningRequired Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [Task Class](topic11629.md) : IsRunningRequired Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_ctx_
    The specification context for the active specification.

Glossary Item Box

Determines whether the task requires the specification context to be open. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Overridable Function IsRunningRequired( _
       ByVal _ctx_ As [SpecificationContext](topic11149.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [Task](topic11629.md)
    Dim ctx As [SpecificationContext](topic11149.md)
    Dim value As Boolean
     
    value = instance.IsRunningRequired(ctx)  
  
C#|   
---|---  
      
    
    protected virtual bool IsRunningRequired( 
       [SpecificationContext](topic11149.md) _ctx_
    )  
  
#### Parameters

 _ctx_
    The specification context for the active specification.

#### Return Value

True if the specification needs to be running for the task to execute.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Task Class](topic11629.md)   
[Task Members](topic11630.md)


