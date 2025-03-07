Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
IsDeleteContextTask Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [Task Class](topic11629.md) : IsDeleteContextTask Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_ctx_
    The specification context for the active specification.

Glossary Item Box

Determines whether the task will be deleting the specification context in it's execution. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Overridable Function IsDeleteContextTask( _
       ByVal _ctx_ As [SpecificationContext](topic11149.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [Task](topic11629.md)
    Dim ctx As [SpecificationContext](topic11149.md)
    Dim value As Boolean
     
    value = instance.IsDeleteContextTask(ctx)  
  
C#|   
---|---  
      
    
    protected virtual bool IsDeleteContextTask( 
       [SpecificationContext](topic11149.md) _ctx_
    )  
  
#### Parameters

 _ctx_
    The specification context for the active specification.

#### Return Value

True if the task will delete the specification context.

# Remarks

Tasks that qualify will be made to run last, despite their task ordering.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Task Class](topic11629.md)   
[Task Members](topic11630.md)


