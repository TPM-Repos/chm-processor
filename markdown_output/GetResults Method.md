Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetResults Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification.StandardTasks Namespace](topic11896.md) > [RealTimeReleaseModelsTask Class](topic12405.md) : GetResults Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_ctx_
    The specification context for the active specification.

Glossary Item Box

Releases the configured models and returns the results. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetResults( _
       ByVal _ctx_ As [SpecificationContext](topic11149.md) _
    ) As [ReleaseComponentsResults](topic6300.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [RealTimeReleaseModelsTask](topic12405.md)
    Dim ctx As [SpecificationContext](topic11149.md)
    Dim value As [ReleaseComponentsResults](topic6300.md)
     
    value = instance.GetResults(ctx)  
  
C#|   
---|---  
      
    
    public [ReleaseComponentsResults](topic6300.md) GetResults( 
       [SpecificationContext](topic11149.md) _ctx_
    )  
  
#### Parameters

 _ctx_
    The specification context for the active specification.

#### Return Value

The results of releasing the components.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[RealTimeReleaseModelsTask Class](topic12405.md)   
[RealTimeReleaseModelsTask Members](topic12406.md)


